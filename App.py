import streamlit as st
import pandas as pd
import openpyxl
from data_loader import load_all_player_data
from pizza_charts import defensive_pizza_chart, offensive_pizza_chart
from physical_pizza_charts import physical_pizza_chart
from league_team_charts import league_strength, team_position
from physical_compare_JPL import physical_compare_JPL


# --- Pagina instellingen ---
st.set_page_config(layout="wide", page_title="Player Pizza Charts Dashboard")

# --- Data inladen ---
@st.cache_data
def get_player_data():
    return load_all_player_data()

df_all = get_player_data()

# --- Helper functies ---
def apply_filters(df, **filters):
    """Pas alle filters toe op de dataset"""
    result = df.copy()
    
    for filter_name, filter_value in filters.items():
        if not filter_value:
            continue
            
        if filter_name == 'age_range':
            result = result[(result['age'] >= filter_value[0]) & (result['age'] <= filter_value[1])]
        elif filter_name == 'nineties_range':
            low, high = filter_value
            if 'matchShare_x' in result.columns:
                result = result[(result['matchShare_x'] >= low) & (result['matchShare_x'] <= high)]
        elif filter_name == 'leg' and filter_value:
            result = result[result['leg'] == filter_value]          
        elif filter_name == 'percentiles':
            for col, (low, high) in filter_value.items():
                if col in result.columns:
                    result = result[(result[col] >= low) & (result[col] <= high)]
        elif filter_name == 'league_strength':
            low, high = filter_value
            if 'competition_avg' in result.columns:
                result = result[(result['competition_avg'] >= low) & (result['competition_avg'] <= high)]
        elif filter_name == 'team_position' and filter_value:
            if 'league_position_squad_rating' in result.columns:
                result = result[result['league_position_squad_rating'] == filter_value]
        elif filter_name == 'season' and filter_value:
            # Multiselect voor seizoenen
            result = result[result['season'].isin(filter_value)]
        elif filter_name == 'playerName' and filter_value:
            # Multiselect voor spelers
            result = result[result['playerName'].isin(filter_value)]
        elif filter_value:
            result = result[result[filter_name] == filter_value]
    
    return result

def get_available_options(df, column):
    return sorted(df[column].dropna().unique().tolist())

# --- Georganiseerde percentile columns ---
percentile_groups = {
    "Defending" : {
        "DEFENSIVE_TOUCHES_BY_ACTION_DUEL_percentile": "Number of Ground Duels",
        "defensive_ground_duels_win_percentage_percentile": "Defensive Ground Duels Win Percentage",
        "offensive_ground_duels_win_percentage_percentile": "Total Ground Duels Win Percentage",
        "important_ground_duels_won": "Important Ground Duels Won",
        "DEFENSIVE_TOUCHES_BY_ACTION_HEADER_percentile": "Number of Defensive Headers",
        "defensive_aerial_duels_win_percentage_percentile": "Defensive Aerial Duels Win Percentage",
        "offensive_aerial_duels_win_percentage_percentile": "Total Aerial Duels Win Percentage",
        "DEFENSIVE_TOUCHES_BY_ACTION_BLOCK_percentile": "Number of Blocks",
    },
    "High Pressure":{
        "bal_win_removed_opponents": "Ball Wins Removed Opponents",
        "ball_win_removed_defenders_percentile": "Ball Wins Removed Defenders",
        "NUMBER_OF_PRESSES_percentile": "Number of Presses",
        "pressing_intensity": "Pressing Intensity",
        "important_interceptions": "Important Interceptions"
    },   
    "Building Up": {
        "passing_accuracy_low_pass_percentile": "Passing Accuracy",
        "BALL_LOSS_NUMBER_percentile": "Ball Losses",
        "critical_ball_loss": "Critical Ball Losses",
        "ball_progression": "Ball Progression",
        "bypassed_opponents_through_passing_percentile": "Bypassed Opponents Through Passing",
        "passes_to_final_third": "Passes to Final Third",
        "succesful_long_passes_played_percentile": "Successful Long Passes",
        "directness_percentile": "Directness",
        "total_progressive_carries_percentile": "Progressive Carries",
        "BYPASSED_OPPONENTS_BY_ACTION_DRIBBLE_percentile": "Bypassed Opponents by Dribble",
        "BYPASSED_OPPONENTS_RECEIVING_percentile": "Bypassed Opponents Receiving",
        "HOLD_UP_PLAY_SCORE_percentile": "Hold-Up Play"
    },
    "Chance Creation": {
        "bypassed_defenders_through_passing_percentile": "Bypassed Defenders Through Passing",
        "passes_into_penalty_area": "Passes into Penalty Area",
        "succesful_passes_in_behind_percentile": "Successful Passes in Behind",
        "successful_crosses_percentile": "Successful Crosses",
        "chance_creation": "Chance Creation",
        "BYPASSED_DEFENDERS_BY_ACTION_DRIBBLE_percentile": "Bypassed Defenders by Dribble",
        "total_caries_to_box_percentile": "Total Carries to Box",
        "availability_between_the_lines": "Availability Between the Lines"
    },
    "Finishing": {
        "SHOT_XG_percentile": "Shot xG",
        "SHOT_AT_GOAL_NUMBER_percentile": "Shots on Goal",
        "OFFENSIVE_TOUCHES_IN_PITCH_POSITION_OPPONENT_BOX_percentile": "Touches in Penalty Area",
        "running_in_behind": "Running in Behind"
    },
    "Transition": {
        "total_vertical_actions_in_transition_percentile": "Verticality in Offensive Transition",
        "total_defensive_actions_in_counterpress_percentile": "Defensive Actions in Counterpress"
    },
    "Set-Pieces": {
        "SHOT_XG_AT_PHASE_SET_PIECE_percentile": "Set-Piece xG",
        "DEFENSIVE_TOUCHES_AT_PHASE_SET_PIECE_percentile": "Defensive Touches at Set-Pieces"
    },
    "Physical": {
        'psv99_top5_percentile': "Max. Sprint Speed",
        'TD_per_90_percentile': "Total Distance",
        'RD_per_90_percentile': "Total Running Distance",
        'HID_per_90_percentile': "High Intensity Distance",
        'HI_count_per_90_percentile': "High Intensity Count",
        'SPRD_per_90_percentile': "Sprint Distance",
        'SPR_count_per_90_percentile': "Sprint Count",
        'acc_count_per_90_percentile': "Accelerations",
        'dec_count_per_90_percentile': "Decelerations"
    },
    "Overall": {
        'OFFENSIVE_TOUCHES_percentile': 'Offensive Involvement',
        'defensive_involvement': 'Defensive Involvement',
        'defensive_match': "Defensive Match",
        'offensive_match': "Offensive Match",
        'essevee_match': 'Profile Match'
    }
}

# --- Sidebar filters ---
st.sidebar.header("🎯 Basic Filters")

# Reset knop - gebruik deze versie
if st.sidebar.button("🔄 Reset All Filters"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# Basis filters - allemaal onafhankelijk
age_min, age_max = float(df_all['age'].min()), float(df_all['age'].max())
nineties_min, nineties_max = float(df_all['matchShare_x'].min()), float(df_all['matchShare_x'].max())

# Season filter - MULTISELECT
available_seasons = get_available_options(df_all, 'season')
selected_seasons = st.sidebar.multiselect(
    "Season",
    options=available_seasons,
    default=[],  # Altijd leeg beginnen
    key='filter_season'
)

# Team filter
available_teams = get_available_options(df_all, 'squadName')
team = st.sidebar.selectbox(
    "Team",
    options=[''] + available_teams,
    index=0,
    key='filter_squadName'
) or ''

# Position filter  
available_positions = get_available_options(df_all, 'position')
position = st.sidebar.selectbox(
    "Position",
    options=[''] + available_positions,
    index=0,
    key='filter_position'
) or ''

# Foot filter
available_legs = get_available_options(df_all, 'leg')
leg = st.sidebar.selectbox(
    "Preferred Foot",
    options=[''] + available_legs,
    index=0,
    key='filter_leg'
) or ''

# League Strength filter
min_strength = float(df_all['competition_avg'].min())
max_strength = float(df_all['competition_avg'].max())

league_strength_range = st.sidebar.slider(
    "League Strength",
    min_value=round(min_strength, 2),
    max_value=round(max_strength, 2),
    value=(round(min_strength, 2), round(max_strength, 2)),
    step=0.01,
    key='filter_league_strength'
)

# Team Position filter
position_options = [''] + ['TOP', 'AVERAGE', 'BOTTOM']
selected_team_position = st.sidebar.selectbox(
    "Team Position (League Ranking)",
    options=position_options,
    index=0,  # Zorg dat index 0 is (lege selectie)
    key='filter_team_position'
)

# Age filter
age_range = st.sidebar.slider(
    "Age",
    min_value=age_min,
    max_value=age_max,
    value=(age_min, age_max),
    step=0.1,
    key='filter_age_range'
)

# 90's filter
nineties_range = st.sidebar.slider(
    "90s (Match Share)",
    min_value=nineties_min,
    max_value=nineties_max,
    value=(nineties_min, nineties_max),
    step=0.1,
    key='filter_nineties_range'
)

# Player filter - MULTISELECT
available_players = get_available_options(df_all, 'playerName')
selected_players = st.sidebar.multiselect(
    "Player", 
    options=available_players,
    default=[],  # Altijd leeg beginnen
    key='filter_playerName'
)

# --- Percentile filters ---
st.sidebar.markdown("---")
st.sidebar.subheader("📊 Percentile Filters")

active_groups = st.sidebar.multiselect(
    "Selecteer filter categorieën:",
    options=list(percentile_groups.keys()),
    default=[],
    help="Kies welke percentile filters je wilt gebruiken"
)

percentile_filters = {}


for group_name in active_groups:
    with st.sidebar.expander(f"{group_name} ({len(percentile_groups[group_name])} filters)"):
        for col, label in percentile_groups[group_name].items():
            if col in df_all.columns:
                valid_values = df_all[col].dropna()
                if not valid_values.empty:
                    # Specifieke slider range voor deze 3 kolommen
                    if col in ['essevee_match', 'defensive_match', 'offensive_match']:
                        min_val, max_val = 0, 10
                    else:
                        min_val, max_val = 0, 100
                    default = st.session_state.get(f"filter_{col}", (min_val, max_val))
                    percentile_filters[col] = st.slider(
                        label,
                        min_val, max_val,
                        default,
                        key=f"filter_{col}",
                        help=f"Filter op {label} percentile"
                    )



# --- Finale gefilterde data ---
current_filters = {
    'season': selected_seasons,  # Nu een list
    'squadName': team,
    'playerName': selected_players,  # Nu een list
    'position': position,
    'leg': leg,
    'age_range': age_range,
    'nineties_range': nineties_range,
    'league_strength': league_strength_range,
    'team_position': selected_team_position,
    'percentiles': percentile_filters
}

# Dataset met ALLE filters (voor tabel en selectie)
final_df = apply_filters(df_all, **current_filters)

# --- Hoofdscherm ---
# Filter info
col_info1, col_info2, col_info3 = st.columns(3)

with col_info1:
    st.markdown(f"<p style='font-size:14px'>Totaal spelers<br><b>{len(df_all)}</b></p>", unsafe_allow_html=True)

with col_info2:
    st.markdown(f"<p style='font-size:14px'>Na filters<br><b>{len(final_df)}</b></p>", unsafe_allow_html=True)

with col_info3:
    st.markdown(f"<p style='font-size:14px'>Actieve percentile filters<br><b>{len(percentile_filters)}</b></p>", unsafe_allow_html=True)

# Toon geselecteerde seizoenen en spelers
if selected_seasons:
    st.sidebar.info(f"Geselecteerde seizoenen: {', '.join(selected_seasons)}")
if selected_players:
    st.sidebar.info(f"Geselecteerde spelers: {len(selected_players)}")

if len(percentile_filters) > 0:
    with st.expander("🔍 Actieve Percentile Filters"):
        for col, (low, high) in percentile_filters.items():
            group_name = next((group for group, cols in percentile_groups.items() if col in cols), "Unknown")
            label = next((label for c, label in percentile_groups[group_name].items() if c == col), col)
            st.write(f"**{label}**: {low}-{high}%")

# --- Klikbare tabel of charts ---
if len(final_df) > 0:
    # Maak display dataframe met unieke index
    final_df["90's"] = final_df["matchShare_x"].astype(float).round(1)
    final_df["Country"] = final_df["playerCountry"]

    display_df = final_df[['season', 'playerName', "Country", 'age', 'squadName',
                           'competitionName', 'value', 'position', 'essevee_match', "90's"]].drop_duplicates().reset_index(drop=True)
    display_df = display_df.sort_values(['playerName'])

    # Hernoem kolommen
    display_df = display_df.rename(columns={
        'competitionName': 'Competition',
        'value': 'League Strength',
        'squadName': 'Team',
        'playerName': 'Player Name',
        'season': 'Season',
        'age': 'Age',
        'position': 'Position',
        'essevee_match': 'Profile Match'
    })
    display_df["League Strength"] = display_df["League Strength"].astype(float).round(2)

    # Klikbare tabel (werkt ook bij 1 rij)
    selected_rows = st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True,
        on_select="rerun",
        selection_mode="single-row"
    )

    # Als er een rij geselecteerd is
    if selected_rows.selection.rows:
        selected_idx = selected_rows.selection.rows[0]
        selected_row = display_df.iloc[selected_idx]

        # Vind de exacte match in final_df
        selected_player_data = final_df[
            (final_df['playerName'] == selected_row['Player Name']) &
            (final_df['position'] == selected_row['Position']) &
            (final_df['squadName'] == selected_row['Team']) &
            (final_df['season'] == selected_row['Season'])
        ].iloc[0]

        st.success(f"✅ Geselecteerd: {selected_row['Player Name']}")

        # --- Team charts ---
        st.subheader("🌍 League & Team Context")

        # League Strength → toon alle competities
        fig_league = league_strength(df_all, selected_player_data['competitionName'])
        st.pyplot(fig_league, use_container_width=True)

        # Team Position → toon alle teams binnen alle competities
        fig_team = team_position(df_all, selected_player_data['squadId'], selected_player_data['competitionName'], selected_player_data['season'])
        st.pyplot(fig_team, use_container_width=True)

        # --- Pizza charts ---
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            st.subheader("⚔️ Offensive")
            fig_off = offensive_pizza_chart(final_df, selected_player_data['playerName'],
                                            selected_player_data['position'], selected_player_data['season'],
                                            selected_player_data['squadName'])
            st.pyplot(fig_off, use_container_width=True)

        with col2:
            st.subheader("🛡️ Defensive")
            fig_def = defensive_pizza_chart(final_df, selected_player_data['playerName'],
                                            selected_player_data['position'], selected_player_data['season'],
                                            selected_player_data['squadName'])
            st.pyplot(fig_def, use_container_width=True)

        with col3:
            st.subheader("🏃 Physical")
            fig_phy = physical_pizza_chart(final_df, selected_player_data['playerName'],
                                            selected_player_data['position'], selected_player_data['season'],
                                            selected_player_data['squadName'])
            st.pyplot(fig_phy, use_container_width=True)

            st.subheader("📊 Physical vs JPL")
            fig_compare = physical_compare_JPL(
                final_df,
                selected_player_data['playerName'],
                selected_player_data['position'],
                selected_player_data['season'],
                selected_player_data['squadName']
            )
            st.pyplot(fig_compare, use_container_width=True)

else:
    st.warning("🚫 Geen spelers voldoen aan de huidige filters")
    st.info("💡 Probeer minder restrictieve filters")