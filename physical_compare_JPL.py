import matplotlib.pyplot as plt
import pandas as pd

def physical_compare_JPL(df, playerName, position, season, squadName):    
    # Filter de speler
    player_row = df[
        (df['playerName'] == playerName) &
        (df['position'] == position) &
        (df['season'] == season) &
        (df['squadName'] == squadName)
    ]
    
    if player_row.empty:
        print("Speler niet gevonden in dataset")
        return
    
    player_row = player_row.iloc[0]
    
    # Kolommen en labels
    metrics = ['SPR_count_per_90',
               'HI_count_per_90',
               'SPRD_per_90',
               'HID_per_90',
               'RD_per_90',
               'TD_per_90',
               'psv99_top5'
              ]

    jpl_cols = ['SPR_count_per_90_JPL',
               'HI_count_per_90_JPL',
               'SPRD_per_90_JPL',
                'HID_per_90_JPL',
                'RD_per_90_JPL', 
                'TD_per_90_JPL', 
                'psv99_top5_JPL'
               ]

    
    labels = {
        'psv99_top5': "Max. Sprint Speed",
        'TD_per_90': "Total Distance",
        'RD_per_90': "Total Running Distance",
        'HID_per_90': "High Intensity Distance",
        'HI_count_per_90': "High Intensity Count",
        'SPRD_per_90': "Sprint Distance",
        'SPR_count_per_90': "Sprint Count"
    }
    
    # Gebruik de _JPL kolommen als percentage, vermenigvuldig met 100
    percentages = []
    for jpl in jpl_cols:
        pct = player_row[jpl] * 100  # van 0-1 naar 0-100
        percentages.append(int(round(pct)))
    
    # Kleur gradatie: rood < 90%, geel 90-110%, groen >110%
    colors = []
    for p, m in zip(percentages, metrics):
    
        # ✅ Speciaal kleurenschema voor Max. Sprint speed
        if m == 'psv99_top5':
            if p < 94:
                colors.append('#CC2F2F')
            elif 94 <= p <= 96:
                colors.append('#E38888')
            elif 96 <= p <= 98:
                colors.append('#FFEB94')
            elif 98 <= p <= 102:
                colors.append('#EDFF94')
            elif 102 <= p <= 104:
                colors.append('#42A849')
            elif 104 <= p <= 106:
                colors.append('#218F29')
            else:
                colors.append('#06660D')
            continue  # sla de rest van de normale logica over
    
        # ✅ Normaal kleurenschema voor alle andere metrics
        if p < 75:
            colors.append('#CC2F2F')
        elif 75 <= p <= 85:
            colors.append('#E38888')
        elif 85 <= p <= 95:
            colors.append('#FFEB94')
        elif 95 <= p <= 105:
            colors.append('#EDFF94')
        elif 105 <= p <= 115:
            colors.append('#42A849')
        elif 115 <= p <= 125:
            colors.append('#218F29')
        else:
            colors.append('#06660D')
    
    # Plot
    fig, ax = plt.subplots(figsize=(6,6))
    bars = ax.barh([labels[m] for m in metrics], percentages, color=colors)



    units = {
        'psv99_top5': 'km/h',
        'TD_per_90': 'meter',
        'RD_per_90': 'meter',
        'HID_per_90': 'meter',
        'SPRD_per_90': 'meter',
        'HI_count_per_90': '',
        'SPR_count_per_90': '',
    }
    
    # 2) Aantal decimalen per metric
    decimals = {
        'psv99_top5': 1,  # max speed met 1 decimaal
        # alle andere default 0
    }
    
    # 3) Waardelabels renderen met juiste decimalen + eenheid
    for bar, m in zip(bars, metrics):
        width = bar.get_width()
        val = player_row[m]
    
        dec = decimals.get(m, 0)
        unit = units.get(m, '')
        val_str = f"{val:,.{dec}f}"  # dynamische afronding
    
        # Spatie + unit enkel als unit bestaat
        label = f"{val_str} {unit}".strip()
    
        ax.text(
            width + 1, 
            bar.get_y() + bar.get_height()/2,
            label,
            va='center', ha='left', fontsize=9
        )
        
    # Stippellijn op 100%
    ax.axvline(100, color='gray', linestyle='--', linewidth=1)
    
    ax.set_xlabel('% Jupiler Pro League')
    ax.set_xlim(0, max(percentages) * 1.2)
    plt.tight_layout()
    return fig
