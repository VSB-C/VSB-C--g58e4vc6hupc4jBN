import pandas as pd
from mplsoccer import PyPizza, add_image, FontManager
import matplotlib.pyplot as plt


font_normal = FontManager('https://raw.githubusercontent.com/googlefonts/roboto/main/'
                          'src/hinted/Roboto-Regular.ttf')
font_italic = FontManager('https://raw.githubusercontent.com/googlefonts/roboto/main/'
                          'src/hinted/Roboto-Italic.ttf')
font_bold = FontManager('https://raw.githubusercontent.com/google/fonts/main/apache/robotoslab/'
                        'RobotoSlab[wght].ttf')

PHYSICAL = {
    "params": [
        'psv99_top5_percentile',

        'TD_per_90_percentile',
        'RD_per_90_percentile',

        'HID_per_90_percentile',
        'HI_count_per_90_percentile',

        'SPRD_per_90_percentile',
        'SPR_count_per_90_percentile',

        'acc_count_per_90_percentile',
        'dec_count_per_90_percentile'
        ],
     "labels": {
        'psv99_top5_percentile': "Max.\nSprint\nspeed",

        'TD_per_90_percentile': "Total\nDistance",
        'RD_per_90_percentile': "Total\nRunning\nDistance",

        'HID_per_90_percentile': "High\nIntensity\nDistance",
        'HI_count_per_90_percentile': "High\nIntensity\nCount",

        'SPRD_per_90_percentile': "Sprint\nDistance",
        'SPR_count_per_90_percentile': "Sprint\nCount",

        'acc_count_per_90_percentile': "Accelerations",
        'dec_count_per_90_percentile': "Decelerations"
        },
    "colors": ["#91E4FF"] * 1 + ["#FEFFBF"] * 1 + ["#F0FFBF"] * 1 + ["#CAFFBF"] * 2 + ["#22AB2F"] * 2 + ["#FFE6BF"] * 2
}



def physical_pizza_chart(df, playerName, position, season, squadName):
    config = PHYSICAL
    if not config:
        raise ValueError(f"Geen configuratie")
    
    # Filter de juiste speler en positie
    row_filtered = df[(df['playerName'] == playerName) & (df['position'] == position) & (df['squadName'] == squadName) & (df['season'] == season)]
    if row_filtered.empty:
        raise ValueError(f"Geen data gevonden voor {playerName} ({position})")
    row = row_filtered.iloc[0]

    # Haal de parameters en labels uit de config
    params = config["params"]
    param_labels = config["labels"]

    # Selecteer de waarden uit de gefilterde rij
    values = row[params].values.flatten().tolist()

    # Maak de labels voor de pizza chart
    params_display = [param_labels.get(param, param) for param in params]

    slice_colors = config['colors']
    text_colors = ["#000000"] * len(params_display)

    baker = PyPizza(
        params=params_display,          # list of parameters. Hier moeten we dus onze nieuwe lijst gebruiken!!!!!
        #background_color="#D4D4D4",     # background color
        straight_line_color="#000000",  # color for straight lines
        straight_line_lw=0.5,             # linewidth for straight lines
        last_circle_lw=3,               # linewidth of last circle
        last_circle_color = "#000000",
        other_circle_lw=0.2,              # linewidth for other circles
        other_circle_color = "#000000",
        inner_circle_size=20            # size of inner circle
    )


    fig, ax = baker.make_pizza(
        values,                          # list of values
        figsize=(8, 8.5),                # adjust figsize according to your need
        color_blank_space="same",        # use same color to fill blank space
        slice_colors=slice_colors,       # color for individual slices
        value_colors=text_colors,        # color for the value-text
        value_bck_colors=slice_colors,   # color for the blank spaces
        blank_alpha=0,                 # alpha for blank-space colors
        kwargs_slices=dict(
            edgecolor="#000000", zorder=2, linewidth=0.5
        ),                               # values to be used when plotting slices
        kwargs_params=dict(
            color="#000000", fontsize=9,
            fontproperties=font_normal.prop, va="center"
        ),                               # values to be used when adding parameter
        kwargs_values=dict(
            color="#000000", fontsize=10,
            fontproperties=font_normal.prop, zorder=3,
            bbox=dict(
                edgecolor="#000000", facecolor="cornflowerblue",
                boxstyle="round,pad=0.2", lw=1
            )
        )                                # values to be used when adding parameter-values
    )

    return fig