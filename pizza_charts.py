import pandas as pd
from mplsoccer import PyPizza, add_image, FontManager
import matplotlib.pyplot as plt


font_normal = FontManager('https://raw.githubusercontent.com/googlefonts/roboto/main/'
                          'src/hinted/Roboto-Regular.ttf')
font_italic = FontManager('https://raw.githubusercontent.com/googlefonts/roboto/main/'
                          'src/hinted/Roboto-Italic.ttf')
font_bold = FontManager('https://raw.githubusercontent.com/google/fonts/main/apache/robotoslab/'
                        'RobotoSlab[wght].ttf')

POSITIONS_CONFIG = {
    "CENTRAL_DEFENDER": {
        "offensive": {
            "params": [
                "OFFENSIVE_TOUCHES_percentile",
                "bypassed_opponents_through_passing_percentile",
                "ball_progression",
                "passes_to_final_third",
                "passing_accuracy_low_pass_percentile",
                "BALL_LOSS_NUMBER_percentile",
                "critical_ball_loss",
                "total_progressive_carries_percentile",
                "BYPASSED_OPPONENTS_BY_ACTION_DRIBBLE_percentile",
                "succesful_long_passes_played_percentile",
                "directness_percentile",
                "total_vertical_actions_in_transition_percentile",
                "SHOT_XG_AT_PHASE_SET_PIECE_percentile"
            ],
            "labels": {
                "OFFENSIVE_TOUCHES_percentile": "Offensive\nTouches",
                "bypassed_opponents_through_passing_percentile": "Bypassed\nOpponents\n(passing)",
                "ball_progression": "Ball Progression",
                "passes_to_final_third": "Passes to\nFinal Third",
                "passing_accuracy_low_pass_percentile": "Passing\nAccuracy",
                "BALL_LOSS_NUMBER_percentile": "Ball Losses",
                "critical_ball_loss": "Critical\nBall Losses",
                "total_progressive_carries_percentile": "Progressive\nCarries",
                "BYPASSED_OPPONENTS_BY_ACTION_DRIBBLE_percentile": "Bypassed\nOpponents\n(dribbling)",
                "succesful_long_passes_played_percentile": "Succesful\nLong Passes",
                "directness_percentile": "Directness",
                "total_vertical_actions_in_transition_percentile": "Verticality\nIn Transition",
                "SHOT_XG_AT_PHASE_SET_PIECE_percentile": "Set-Piece xG"
            },
            "colors": ["#91E4FF"] * 1 + ["#B0FF91"] * 10 + ["#78C95D"] * 0 + ["#448C2D"] * 0 + ["#114F13"] * 1 + ["#2051B3"] * 1
        },
        "defensive": {
            "params": [
                "defensive_involvement",
                "important_ground_duels_won",
                "DEFENSIVE_TOUCHES_BY_ACTION_DUEL_percentile",
                "defensive_ground_duels_win_percentage_percentile",
                "DEFENSIVE_TOUCHES_BY_ACTION_HEADER_percentile",
                "defensive_aerial_duels_win_percentage_percentile",
                "DEFENSIVE_TOUCHES_BY_ACTION_BLOCK_percentile",
                "important_interceptions",
                "bal_win_removed_opponents",
                "NUMBER_OF_PRESSES_percentile",
                "total_defensive_actions_in_counterpress_percentile",
                "DEFENSIVE_TOUCHES_AT_PHASE_SET_PIECE_percentile"
            ],
            "labels": {
                "defensive_involvement": "Defensive\nInvolvement",
                "important_ground_duels_won": "Important Ground\nDuels Won",
                "DEFENSIVE_TOUCHES_BY_ACTION_DUEL_percentile": "Number of\nGround Duels",
                "defensive_ground_duels_win_percentage_percentile": "Ground Duel\nWin Percentage",
                "DEFENSIVE_TOUCHES_BY_ACTION_HEADER_percentile": "Number of\nDefensive Headers",
                "defensive_aerial_duels_win_percentage_percentile": "Aerial Duel\nWin Percentage",
                "DEFENSIVE_TOUCHES_BY_ACTION_BLOCK_percentile": "Number of Blocks",
                "important_interceptions": "Important\nInterceptions",
                "bal_win_removed_opponents": "Ball Win\nRemoved Opponents",
                "NUMBER_OF_PRESSES_percentile": "Number of\nPresses",
                "total_defensive_actions_in_counterpress_percentile": "Defensive Actions\nin Counterpress",
                "DEFENSIVE_TOUCHES_AT_PHASE_SET_PIECE_percentile": "Defensive Touches\nat Set-Pieces"
            },
            "colors": ["#91E4FF"] * 1 + ["#FAB4B4"] * 6 + ["#D42F2F"] * 3 + ["#961111"] * 1 + ["#CD70DB"] * 1
        }
    },
    "RIGHT_WINGBACK_DEFENDER": {
        "defensive": {
            "params": [
                "defensive_involvement",
                "important_ground_duels_won",
                "DEFENSIVE_TOUCHES_BY_ACTION_DUEL_percentile",
                "defensive_ground_duels_win_percentage_percentile",
                "DEFENSIVE_TOUCHES_BY_ACTION_HEADER_percentile",
                "defensive_aerial_duels_win_percentage_percentile",
                "DEFENSIVE_TOUCHES_BY_ACTION_BLOCK_percentile",
                "important_interceptions",
                "bal_win_removed_opponents",
                "pressing_intensity",
                "total_defensive_actions_in_counterpress_percentile",
                "DEFENSIVE_TOUCHES_AT_PHASE_SET_PIECE_percentile"
            ],
            "labels": {
                "defensive_involvement": "Defensive\nInvolvement",
                "important_ground_duels_won": "Important Ground\nDuels Won",
                "DEFENSIVE_TOUCHES_BY_ACTION_DUEL_percentile": "Number of\nGround Duels",
                "defensive_ground_duels_win_percentage_percentile": "Ground Duel\nWin Percentage",
                "DEFENSIVE_TOUCHES_BY_ACTION_HEADER_percentile": "Number of\nDefensive Headers",
                "defensive_aerial_duels_win_percentage_percentile": "Aerial Duel\nWin Percentage",
                "DEFENSIVE_TOUCHES_BY_ACTION_BLOCK_percentile": "Number of Blocks",
                "important_interceptions": "Important\nInterceptions",
                "bal_win_removed_opponents": "Ball Win\nRemoved Opponents",
                "pressing_intensity": "Pressing\nIntensity",
                "total_defensive_actions_in_counterpress_percentile": "Defensive Actions\nin Counterpress",
                "DEFENSIVE_TOUCHES_AT_PHASE_SET_PIECE_percentile": "Defensive Touches\nat Set-Pieces"
            },
            "colors": ["#91E4FF"] * 1 + ["#FAB4B4"] * 6 + ["#D42F2F"] * 3 + ["#961111"] * 1 + ["#CD70DB"] * 1
        },
        "offensive": {
            "params": [
                "OFFENSIVE_TOUCHES_percentile",
                "bypassed_opponents_through_passing_percentile",
                "BYPASSED_OPPONENTS_RECEIVING_percentile",
                "ball_progression",
                "passes_to_final_third",
                "passing_accuracy_low_pass_percentile",
                "BALL_LOSS_NUMBER_percentile",
                "critical_ball_loss",
                "total_progressive_carries_percentile",
                "BYPASSED_OPPONENTS_BY_ACTION_DRIBBLE_percentile",
                "succesful_long_passes_played_percentile",
                "directness_percentile",
                "chance_creation",
                "BYPASSED_DEFENDERS_BY_ACTION_DRIBBLE_percentile",
                "total_caries_to_box_percentile",
                "bypassed_defenders_through_passing_percentile",
                "succesful_passes_in_behind_percentile",
                "successful_crosses_percentile",
                "running_in_behind",
                "total_vertical_actions_in_transition_percentile"
            ],
            "labels": {
                "OFFENSIVE_TOUCHES_percentile": "Offensive\nTouches",
                "bypassed_opponents_through_passing_percentile": "Bypassed\nOpponents\n(passing)",
                "BYPASSED_OPPONENTS_RECEIVING_percentile": "Bypassed\nOpponents\nReceiving",
                "ball_progression": "Ball Progression",
                "passes_to_final_third": "Passes to\nFinal Third",
                "passing_accuracy_low_pass_percentile": "Passing\nAccuracy",
                "BALL_LOSS_NUMBER_percentile": "Ball Losses",
                "critical_ball_loss": "Critical\nBall Losses",
                "total_progressive_carries_percentile": "Progressive\nCarries",
                "BYPASSED_OPPONENTS_BY_ACTION_DRIBBLE_percentile": "Bypassed\nOpponents\n(dribbling)",
                "succesful_long_passes_played_percentile": "Succesful\nLong Passes",
                "directness_percentile": "Directness",
                "chance_creation": "Chance\nCreation",
                "BYPASSED_DEFENDERS_BY_ACTION_DRIBBLE_percentile": "Bypassed\nDefenders\n(dribbling)",
                "total_caries_to_box_percentile": "Carries into\nPenalty Area",
                "bypassed_defenders_through_passing_percentile": "Bypassed\nDefenders\n(passing)",
                "succesful_passes_in_behind_percentile": "Passing\nin Behind",
                "successful_crosses_percentile": "Succesful\nCrosses",
                "running_in_behind": "Running\nin Behind",
                "total_vertical_actions_in_transition_percentile": "Verticality\nIn Transition"
            },
            "colors": ["#91E4FF"] * 1 + ["#B0FF91"] * 11  + ["#78C95D"] * 6 + ["#448C2D"] * 1 + ["#114F13"] * 1 + ["#2051B3"] * 0
        }
    },
    "LEFT_WINGBACK_DEFENDER": {
        "defensive": {
            "params": [
                "defensive_involvement",
                "important_ground_duels_won",
                "DEFENSIVE_TOUCHES_BY_ACTION_DUEL_percentile",
                "defensive_ground_duels_win_percentage_percentile",
                "DEFENSIVE_TOUCHES_BY_ACTION_HEADER_percentile",
                "defensive_aerial_duels_win_percentage_percentile",
                "DEFENSIVE_TOUCHES_BY_ACTION_BLOCK_percentile",
                "important_interceptions",
                "bal_win_removed_opponents",
                "pressing_intensity",
                "total_defensive_actions_in_counterpress_percentile",
                "DEFENSIVE_TOUCHES_AT_PHASE_SET_PIECE_percentile"
            ],
            "labels": {
                "defensive_involvement": "Defensive\nInvolvement",
                "important_ground_duels_won": "Important Ground\nDuels Won",
                "DEFENSIVE_TOUCHES_BY_ACTION_DUEL_percentile": "Number of\nGround Duels",
                "defensive_ground_duels_win_percentage_percentile": "Ground Duel\nWin Percentage",
                "DEFENSIVE_TOUCHES_BY_ACTION_HEADER_percentile": "Number of\nDefensive Headers",
                "defensive_aerial_duels_win_percentage_percentile": "Aerial Duel\nWin Percentage",
                "DEFENSIVE_TOUCHES_BY_ACTION_BLOCK_percentile": "Number of Blocks",
                "important_interceptions": "Important\nInterceptions",
                "bal_win_removed_opponents": "Ball Win\nRemoved Opponents",
                "pressing_intensity": "Pressing\nIntensity",
                "total_defensive_actions_in_counterpress_percentile": "Defensive Actions\nin Counterpress",
                "DEFENSIVE_TOUCHES_AT_PHASE_SET_PIECE_percentile": "Defensive Touches\nat Set-Pieces"
            },
            "colors": ["#91E4FF"] * 1 + ["#FAB4B4"] * 6 + ["#D42F2F"] * 3 + ["#961111"] * 1 + ["#CD70DB"] * 1
        },
        "offensive": {
            "params": [
                "OFFENSIVE_TOUCHES_percentile",
                "bypassed_opponents_through_passing_percentile",
                "BYPASSED_OPPONENTS_RECEIVING_percentile",
                "ball_progression",
                "passes_to_final_third",
                "passing_accuracy_low_pass_percentile",
                "BALL_LOSS_NUMBER_percentile",
                "critical_ball_loss",
                "total_progressive_carries_percentile",
                "BYPASSED_OPPONENTS_BY_ACTION_DRIBBLE_percentile",
                "succesful_long_passes_played_percentile",
                "directness_percentile",
                "chance_creation",
                "BYPASSED_DEFENDERS_BY_ACTION_DRIBBLE_percentile",
                "total_caries_to_box_percentile",
                "bypassed_defenders_through_passing_percentile",
                "succesful_passes_in_behind_percentile",
                "successful_crosses_percentile",
                "running_in_behind",
                "total_vertical_actions_in_transition_percentile"
            ],
            "labels": {
                "OFFENSIVE_TOUCHES_percentile": "Offensive\nTouches",
                "bypassed_opponents_through_passing_percentile": "Bypassed\nOpponents\n(passing)",
                "BYPASSED_OPPONENTS_RECEIVING_percentile": "Bypassed\nOpponents\nReceiving",
                "ball_progression": "Ball\nProgression",
                "passes_to_final_third": "Passes to\nFinal Third",
                "passing_accuracy_low_pass_percentile": "Passing\nAccuracy",
                "BALL_LOSS_NUMBER_percentile": "Ball Losses",
                "critical_ball_loss": "Critical\nBall Losses",
                "total_progressive_carries_percentile": "Progressive\nCarries",
                "BYPASSED_OPPONENTS_BY_ACTION_DRIBBLE_percentile": "Bypassed\nOpponents\n(dribbling)",
                "succesful_long_passes_played_percentile": "Succesful\nLong Passes",
                "directness_percentile": "Directness",
                "chance_creation": "Chance\nCreation",
                "BYPASSED_DEFENDERS_BY_ACTION_DRIBBLE_percentile": "Bypassed\nDefenders\n(dribbling)",
                "total_caries_to_box_percentile": "Carries into\nPenalty Area",
                "bypassed_defenders_through_passing_percentile": "Bypassed\nDefenders\n(passing)",
                "succesful_passes_in_behind_percentile": "Passing\nin Behind",
                "successful_crosses_percentile": "Succesful\nCrosses",
                "running_in_behind": "Running\nin Behind",
                "total_vertical_actions_in_transition_percentile": "Verticality\nIn Transition"
            },
            "colors": ["#91E4FF"] * 1 + ["#B0FF91"] * 11  + ["#78C95D"] * 6 + ["#448C2D"] * 1 + ["#114F13"] * 1 + ["#2051B3"] * 0
        }
    },
    "DEFENSE_MIDFIELD": {
        "defensive": {
            "params": [
                "defensive_involvement",
                "important_ground_duels_won",
                "DEFENSIVE_TOUCHES_BY_ACTION_DUEL_percentile",
                "defensive_ground_duels_win_percentage_percentile",
                "DEFENSIVE_TOUCHES_BY_ACTION_HEADER_percentile",
                "defensive_aerial_duels_win_percentage_percentile",
                "DEFENSIVE_TOUCHES_BY_ACTION_BLOCK_percentile",
                "important_interceptions",
                "bal_win_removed_opponents",
                "NUMBER_OF_PRESSES_percentile",
                "total_defensive_actions_in_counterpress_percentile",
                "DEFENSIVE_TOUCHES_AT_PHASE_SET_PIECE_percentile"
            ],
            "labels": {
                "defensive_involvement": "Defensive\nInvolvement",
                "important_ground_duels_won": "Important Ground\nDuels Won",
                "DEFENSIVE_TOUCHES_BY_ACTION_DUEL_percentile": "Number of\nGround Duels",
                "defensive_ground_duels_win_percentage_percentile": "Ground Duel\nWin Percentage",
                "DEFENSIVE_TOUCHES_BY_ACTION_HEADER_percentile": "Number of\nDefensive Headers",
                "defensive_aerial_duels_win_percentage_percentile": "Aerial Duel\nWin Percentage",
                "DEFENSIVE_TOUCHES_BY_ACTION_BLOCK_percentile": "Number of\nBlocks",
                "important_interceptions": "Important\nInterceptions",
                "bal_win_removed_opponents": "Ball Win\nRemoved Opponents",
                "NUMBER_OF_PRESSES_percentile": "Number of\nPresses",
                "total_defensive_actions_in_counterpress_percentile": "Defensive Actions\nin Counterpress",
                "DEFENSIVE_TOUCHES_AT_PHASE_SET_PIECE_percentile": "Defensive Touches\nat Set-Pieces"
            },
            "colors": ["#91E4FF"] * 1 + ["#FAB4B4"] * 6 + ["#D42F2F"] * 3 + ["#961111"] * 1 + ["#CD70DB"] * 1
        },
        "offensive": {
            "params": [
                "OFFENSIVE_TOUCHES_percentile",
                "bypassed_opponents_through_passing_percentile",
                "BYPASSED_OPPONENTS_RECEIVING_percentile",
                "ball_progression",
                "passes_to_final_third",
                "passing_accuracy_low_pass_percentile",
                "BALL_LOSS_NUMBER_percentile",
                "critical_ball_loss",
                "total_progressive_carries_percentile",
                "BYPASSED_OPPONENTS_BY_ACTION_DRIBBLE_percentile",
                "succesful_long_passes_played_percentile",
                "directness_percentile",
                "BYPASSED_DEFENDERS_BY_ACTION_DRIBBLE_percentile",
                "total_caries_to_box_percentile",
                "total_vertical_actions_in_transition_percentile"
            ],
            "labels": {
                "OFFENSIVE_TOUCHES_percentile": "Offensive\nTouches",
                "bypassed_opponents_through_passing_percentile": "Bypassed\nOpponents\n(passing)",
                "BYPASSED_OPPONENTS_RECEIVING_percentile": "Bypassed\nOpponents\nReceiving",
                "ball_progression": "Ball\nProgression",
                "passes_to_final_third": "Passes to\nFinal Third",
                "passing_accuracy_low_pass_percentile": "Passing\nAccuracy",
                "BALL_LOSS_NUMBER_percentile": "Ball Losses",
                "critical_ball_loss": "Critical\nBall Losses",
                "total_progressive_carries_percentile": "Progressive\nCarries",
                "BYPASSED_OPPONENTS_BY_ACTION_DRIBBLE_percentile": "Bypassed\nOpponents\n(dribbling)",
                "succesful_long_passes_played_percentile": "Succesful\nLong Passes",
                "directness_percentile": "Directness",
                "BYPASSED_DEFENDERS_BY_ACTION_DRIBBLE_percentile": "Bypassed\nDefenders\n(dribbling)",
                "total_caries_to_box_percentile": "Carries into\nPenalty Area",
                "total_vertical_actions_in_transition_percentile": "Verticality\nIn Transition"
            },
            "colors": ["#91E4FF"] * 1 + ["#B0FF91"] * 11  + ["#78C95D"] * 2 + ["#448C2D"] * 0 + ["#114F13"] * 1 + ["#2051B3"] * 0
        }
    },
    "CENTRAL_MIDFIELD": {
        "defensive": {
            "params": [
                "defensive_involvement",
                "important_ground_duels_won",
                "DEFENSIVE_TOUCHES_BY_ACTION_DUEL_percentile",
                "defensive_ground_duels_win_percentage_percentile",
                "DEFENSIVE_TOUCHES_BY_ACTION_HEADER_percentile",
                "defensive_aerial_duels_win_percentage_percentile",
                "DEFENSIVE_TOUCHES_BY_ACTION_BLOCK_percentile",
                "important_interceptions",
                "bal_win_removed_opponents",
                "pressing_intensity",
                "total_defensive_actions_in_counterpress_percentile",
                "DEFENSIVE_TOUCHES_AT_PHASE_SET_PIECE_percentile"                
            ],
            "labels": {
                "defensive_involvement": "Defensive\nInvolvement",
                "important_ground_duels_won": "Important Ground\nDuels Won",
                "DEFENSIVE_TOUCHES_BY_ACTION_DUEL_percentile": "Number of\nGround Duels",
                "defensive_ground_duels_win_percentage_percentile": "Ground Duel\nWin Percentage",
                "DEFENSIVE_TOUCHES_BY_ACTION_HEADER_percentile": "Number of\nDefensive Headers",
                "defensive_aerial_duels_win_percentage_percentile": "Aerial Duel\nWin Percentage",
                "DEFENSIVE_TOUCHES_BY_ACTION_BLOCK_percentile": "Number of\nBlocks",
                "important_interceptions": "Important\nInterceptions",
                "bal_win_removed_opponents": "Ball Win\nRemoved Opponents",
                "pressing_intensity": "Pressing\nIntensity",
                "total_defensive_actions_in_counterpress_percentile": "Defensive Actions\nin Counterpress",
                "DEFENSIVE_TOUCHES_AT_PHASE_SET_PIECE_percentile": "Defensive Touches\nat Set-Pieces"
            },
            "colors": ["#91E4FF"] * 1 + ["#FAB4B4"] * 6 + ["#D42F2F"] * 3 + ["#961111"] * 1 + ["#CD70DB"] * 1
            # colors: involvement   +  Defending   +      High pressure    + Transition    + Set-Piece
        },
        "offensive": {
            "params": [
                "OFFENSIVE_TOUCHES_percentile",
                "bypassed_opponents_through_passing_percentile",
                "BYPASSED_OPPONENTS_RECEIVING_percentile",
                "ball_progression",
                "passes_to_final_third",
                "passing_accuracy_low_pass_percentile",
                "BALL_LOSS_NUMBER_percentile",
                "critical_ball_loss",
                "total_progressive_carries_percentile",
                "BYPASSED_OPPONENTS_BY_ACTION_DRIBBLE_percentile",
                "succesful_long_passes_played_percentile",
                "BYPASSED_DEFENDERS_BY_ACTION_DRIBBLE_percentile",
                "total_caries_to_box_percentile",
                "bypassed_defenders_through_passing_percentile",
                "chance_creation",
                "passes_into_penalty_area",
                "succesful_passes_in_behind_percentile",
                "SHOT_XG_percentile",
                "OFFENSIVE_TOUCHES_IN_PITCH_POSITION_OPPONENT_BOX_percentile",
                "total_vertical_actions_in_transition_percentile" 
            ],
            "labels": {
                "OFFENSIVE_TOUCHES_percentile": "Offensive\nTouches",
                "bypassed_opponents_through_passing_percentile": "Bypassed\nOpponents\n(passing)",
                "BYPASSED_OPPONENTS_RECEIVING_percentile": "Bypassed\nOpponents\nReceiving",
                "ball_progression": "Ball\nProgression",
                "passes_to_final_third": "Passes to\nFinal Third",
                "passing_accuracy_low_pass_percentile": "Passing\nAccuracy",
                "BALL_LOSS_NUMBER_percentile": "Ball Losses",
                "critical_ball_loss": "Critical\nBall Losses",
                "total_progressive_carries_percentile": "Progressive\nCarries",
                "BYPASSED_OPPONENTS_BY_ACTION_DRIBBLE_percentile": "Bypassed\nOpponents\n(dribbling)",
                "succesful_long_passes_played_percentile": "Succesful\nLong Passes",
                "BYPASSED_DEFENDERS_BY_ACTION_DRIBBLE_percentile": "Bypassed\nDefenders\n(dribbling)",
                "total_caries_to_box_percentile": "Carries into\nPenalty Area",
                "bypassed_defenders_through_passing_percentile" : "Bypassed\nDefenders\n(passing)",
                "chance_creation": "Chance\nCreation", 
                "passes_into_penalty_area" : "Passes into\nPenalty Area", 
                "succesful_passes_in_behind_percentile" : "Passing\nin Behind", 
                "SHOT_XG_percentile" : "xG", 
                "OFFENSIVE_TOUCHES_IN_PITCH_POSITION_OPPONENT_BOX_percentile" : "Offensive\nTouches in\nPenalty Area", 
                "total_vertical_actions_in_transition_percentile": "Verticality\nIn Transition"
            },
            "colors": ["#91E4FF"] * 1 + ["#B0FF91"] * 10  + ["#78C95D"] * 6 + ["#448C2D"] * 2 + ["#114F13"] * 1 + ["#2051B3"] * 0
            # colors: involvement   +  build-up   +       Chance Creation    + Finishing      +  Transition     +   Set-Piece
        }
    },
    "ATTACKING_MIDFIELD": {
        "defensive": {
            "params": [
                "defensive_involvement",
                "DEFENSIVE_TOUCHES_BY_ACTION_DUEL_percentile",
                "offensive_ground_duels_win_percentage_percentile",
                "DEFENSIVE_TOUCHES_BY_ACTION_HEADER_percentile",
                "offensive_aerial_duels_win_percentage_percentile",
                "ball_win_removed_defenders_percentile",
                "pressing_intensity",
                "total_defensive_actions_in_counterpress_percentile"               
            ],
            "labels": {
                "defensive_involvement": "Defensive\nInvolvement",
                "DEFENSIVE_TOUCHES_BY_ACTION_DUEL_percentile": "Number of\nGround Duels",
                "offensive_ground_duels_win_percentage_percentile": "Ground Duel\nWin Percentage",
                "DEFENSIVE_TOUCHES_BY_ACTION_HEADER_percentile": "Number of\nDefensive Headers",
                "offensive_aerial_duels_win_percentage_percentile": "Aerial Duel\nWin Percentage",
                "ball_win_removed_defenders_percentile": "Ball Win\nRemoved Defenders",
                "pressing_intensity": "Pressing\nIntensity",
                "total_defensive_actions_in_counterpress_percentile": "Defensive Actions\nin Counterpress"
            },
            "colors": ["#91E4FF"] * 1 + ["#FAB4B4"] * 4 + ["#D42F2F"] * 2 + ["#961111"] * 1 + ["#CD70DB"] * 0
            # colors: involvement   +  Defending   +      High pressure    + Transition    + Set-Piece
        },
        "offensive": {
            "params": [
                "OFFENSIVE_TOUCHES_percentile",
                "bypassed_opponents_through_passing_percentile",
                "BYPASSED_OPPONENTS_RECEIVING_percentile",
                "ball_progression",
                "passing_accuracy_low_pass_percentile",
                "BALL_LOSS_NUMBER_percentile",
                "total_progressive_carries_percentile",
                "BYPASSED_OPPONENTS_BY_ACTION_DRIBBLE_percentile",
                "succesful_long_passes_played_percentile",
                "BYPASSED_DEFENDERS_BY_ACTION_DRIBBLE_percentile",
                "total_caries_to_box_percentile",
                "availability_between_the_lines",
                "bypassed_defenders_through_passing_percentile",
                "chance_creation",
                "passes_into_penalty_area",
                "succesful_passes_in_behind_percentile",
                "SHOT_XG_percentile",
                "SHOT_AT_GOAL_NUMBER_percentile",
                "running_in_behind",
                "OFFENSIVE_TOUCHES_IN_PITCH_POSITION_OPPONENT_BOX_percentile",
                "total_vertical_actions_in_transition_percentile",
                "SHOT_XG_AT_PHASE_SET_PIECE_percentile" 
            ],
            "labels": {
                "OFFENSIVE_TOUCHES_percentile": "Offensive\nTouches",
                "bypassed_opponents_through_passing_percentile": "Bypassed\nOpponents\n(passing)",
                "BYPASSED_OPPONENTS_RECEIVING_percentile": "Bypassed\nOpponents\nReceiving",
                "ball_progression": "Ball\nProgression",
                "passing_accuracy_low_pass_percentile": "Passing\nAccuracy",
                "BALL_LOSS_NUMBER_percentile": "Ball\nLosses",
                "total_progressive_carries_percentile": "Progressive\nCarries",
                "BYPASSED_OPPONENTS_BY_ACTION_DRIBBLE_percentile": "Bypassed\nOpponents\n(dribbling)",
                "succesful_long_passes_played_percentile": "Succesful\nLong Passes",
                "BYPASSED_DEFENDERS_BY_ACTION_DRIBBLE_percentile": "Bypassed\nDefenders\n(dribbling)",
                "total_caries_to_box_percentile": "Carries into\nPenalty Area",
                "availability_between_the_lines": "Availability\nBetween\nthe Lines",
                "bypassed_defenders_through_passing_percentile" : "Bypassed\nDefenders\n(passing)",
                "chance_creation": "Chance\nCreation",
                "passes_into_penalty_area" : "Passes into\nPenalty Area", 
                "succesful_passes_in_behind_percentile" : "Passing\nin Behind", 
                "SHOT_XG_percentile" : "xG", 
                "SHOT_AT_GOAL_NUMBER_percentile": "Shot\nVolume",
                "running_in_behind": "Running\nIn Behind",
                "OFFENSIVE_TOUCHES_IN_PITCH_POSITION_OPPONENT_BOX_percentile" : "Offensive\nTouches in\nPenalty Area", 
                "total_vertical_actions_in_transition_percentile": "Verticality\nIn Transition",
                "SHOT_XG_AT_PHASE_SET_PIECE_percentile": "Set-Piece xG"
            },
            "colors": ["#91E4FF"] * 1 + ["#B0FF91"] * 8  + ["#78C95D"] * 7 + ["#448C2D"] * 4 + ["#114F13"] * 1 + ["#2051B3"] * 1
            # colors: involvement   +  build-up   +       Chance Creation    + Finishing      +  Transition     +   Set-Piece
        }
    },
    "RIGHT_WINGER": {
        "defensive": {
            "params": [
                "defensive_involvement",
                "DEFENSIVE_TOUCHES_BY_ACTION_DUEL_percentile",
                "offensive_ground_duels_win_percentage_percentile",
                "DEFENSIVE_TOUCHES_BY_ACTION_HEADER_percentile",
                "offensive_aerial_duels_win_percentage_percentile",
                "ball_win_removed_defenders_percentile",
                "pressing_intensity",
                "total_defensive_actions_in_counterpress_percentile"               
            ],
            "labels": {
                "defensive_involvement": "Defensive\nInvolvement",
                "DEFENSIVE_TOUCHES_BY_ACTION_DUEL_percentile": "Number of\nGround Duels",
                "offensive_ground_duels_win_percentage_percentile": "Ground Duel\nWin Percentage",
                "DEFENSIVE_TOUCHES_BY_ACTION_HEADER_percentile": "Number of\nDefensive Headers",
                "offensive_aerial_duels_win_percentage_percentile": "Aerial Duel\nWin Percentage",
                "ball_win_removed_defenders_percentile": "Ball Win\nRemoved Defenders",
                "pressing_intensity": "Pressing\nIntensity",
                "total_defensive_actions_in_counterpress_percentile": "Defensive Actions\nin Counterpress"
            },
            "colors": ["#91E4FF"] * 1 + ["#FAB4B4"] * 4 + ["#D42F2F"] * 2 + ["#961111"] * 1 + ["#CD70DB"] * 0
            # colors: involvement   +  Defending   +      High pressure    + Transition    + Set-Piece
        },
        "offensive": {
            "params": [
                "OFFENSIVE_TOUCHES_percentile",
                "bypassed_opponents_through_passing_percentile",
                "BYPASSED_OPPONENTS_RECEIVING_percentile",
                "ball_progression",
                "passing_accuracy_low_pass_percentile",
                "BALL_LOSS_NUMBER_percentile",
                "total_progressive_carries_percentile",
                "BYPASSED_OPPONENTS_BY_ACTION_DRIBBLE_percentile",
                
                "BYPASSED_DEFENDERS_BY_ACTION_DRIBBLE_percentile",
                "total_caries_to_box_percentile",
                "availability_between_the_lines",
                "bypassed_defenders_through_passing_percentile",
                "chance_creation",
                "successful_crosses_percentile",
                "passes_into_penalty_area",
                "succesful_passes_in_behind_percentile",
                "SHOT_XG_percentile",
                "SHOT_AT_GOAL_NUMBER_percentile",
                "running_in_behind",
                "OFFENSIVE_TOUCHES_IN_PITCH_POSITION_OPPONENT_BOX_percentile",
                "total_vertical_actions_in_transition_percentile"
            ],
            "labels": {
                "OFFENSIVE_TOUCHES_percentile": "Offensive\nTouches",
                "bypassed_opponents_through_passing_percentile": "Bypassed\nOpponents\n(passing)",
                "BYPASSED_OPPONENTS_RECEIVING_percentile": "Bypassed\nOpponents\nReceiving",
                "ball_progression": "Ball\nProgression",
                "passing_accuracy_low_pass_percentile": "Passing\nAccuracy",
                "BALL_LOSS_NUMBER_percentile": "Ball Losses",
                "total_progressive_carries_percentile": "Progressive\nCarries",
                "BYPASSED_OPPONENTS_BY_ACTION_DRIBBLE_percentile": "Bypassed\nOpponents\n(dribbling)",
                "BYPASSED_DEFENDERS_BY_ACTION_DRIBBLE_percentile": "Bypassed\nDefenders\n(dribbling)",
                "total_caries_to_box_percentile": "Carries into\nPenalty Area",
                "availability_between_the_lines": "Availability Between\nthe Lines",
                "bypassed_defenders_through_passing_percentile" : "Bypassed\nDefenders\n(passing)",
                "chance_creation": "Chance\nCreation",
                "successful_crosses_percentile": "Succesful\nCrosses",
                "passes_into_penalty_area" : "Passes into\nPenalty Area", 
                "succesful_passes_in_behind_percentile" : "Passing\nin Behind", 
                "SHOT_XG_percentile" : "xG", 
                "SHOT_AT_GOAL_NUMBER_percentile": "Shot\nVolume",
                "running_in_behind": "Running\nIn Behind",
                "OFFENSIVE_TOUCHES_IN_PITCH_POSITION_OPPONENT_BOX_percentile" : "Offensive\nTouches in\nPenalty Area", 
                "total_vertical_actions_in_transition_percentile": "Verticality\nIn Transition"
            },
            "colors": ["#91E4FF"] * 1 + ["#B0FF91"] * 7  + ["#78C95D"] * 8 + ["#448C2D"] * 4 + ["#114F13"] * 1 + ["#2051B3"] * 0
            # colors: involvement   +  build-up   +       Chance Creation    + Finishing      +  Transition     +   Set-Piece
        }
    },
    "LEFT_WINGER": {
        "defensive": {
            "params": [
                "defensive_involvement",
                "DEFENSIVE_TOUCHES_BY_ACTION_DUEL_percentile",
                "offensive_ground_duels_win_percentage_percentile",
                "DEFENSIVE_TOUCHES_BY_ACTION_HEADER_percentile",
                "offensive_aerial_duels_win_percentage_percentile",
                "ball_win_removed_defenders_percentile",
                "pressing_intensity",
                "total_defensive_actions_in_counterpress_percentile"               
            ],
            "labels": {
                "defensive_involvement": "Defensive\nInvolvement",
                "DEFENSIVE_TOUCHES_BY_ACTION_DUEL_percentile": "Number of\nGround Duels",
                "offensive_ground_duels_win_percentage_percentile": "Ground Duel\nWin Percentage",
                "DEFENSIVE_TOUCHES_BY_ACTION_HEADER_percentile": "Number of\nDefensive Headers",
                "offensive_aerial_duels_win_percentage_percentile": "Aerial Duel\nWin Percentage",
                "ball_win_removed_defenders_percentile": "Ball Win\nRemoved Defenders",
                "pressing_intensity": "Pressing\nIntensity",
                "total_defensive_actions_in_counterpress_percentile": "Defensive Actions\nin Counterpress"
            },
            "colors": ["#91E4FF"] * 1 + ["#FAB4B4"] * 4 + ["#D42F2F"] * 2 + ["#961111"] * 1 + ["#CD70DB"] * 0
            # colors: involvement   +  Defending   +      High pressure    + Transition    + Set-Piece
        },
        "offensive": {
            "params": [
                "OFFENSIVE_TOUCHES_percentile",
                "bypassed_opponents_through_passing_percentile",
                "BYPASSED_OPPONENTS_RECEIVING_percentile",
                "ball_progression",
                "passing_accuracy_low_pass_percentile",
                "BALL_LOSS_NUMBER_percentile",
                "total_progressive_carries_percentile",
                "BYPASSED_OPPONENTS_BY_ACTION_DRIBBLE_percentile",
                "BYPASSED_DEFENDERS_BY_ACTION_DRIBBLE_percentile",
                "total_caries_to_box_percentile",
                "availability_between_the_lines",
                "bypassed_defenders_through_passing_percentile",
                "chance_creation",
                "successful_crosses_percentile",
                "passes_into_penalty_area",
                "succesful_passes_in_behind_percentile",
                "SHOT_XG_percentile",
                "SHOT_AT_GOAL_NUMBER_percentile",
                "running_in_behind",
                "OFFENSIVE_TOUCHES_IN_PITCH_POSITION_OPPONENT_BOX_percentile",
                "total_vertical_actions_in_transition_percentile"
            ],
            "labels": {
                "OFFENSIVE_TOUCHES_percentile": "Offensive\nTouches",
                "bypassed_opponents_through_passing_percentile": "Bypassed\nOpponents\n(passing)",
                "BYPASSED_OPPONENTS_RECEIVING_percentile": "Bypassed\nOpponents\nReceiving",
                "ball_progression": "Ball\nProgression",
                "passing_accuracy_low_pass_percentile": "Passing\nAccuracy",
                "BALL_LOSS_NUMBER_percentile": "Ball Losses",
                "total_progressive_carries_percentile": "Progressive\nCarries",
                "BYPASSED_OPPONENTS_BY_ACTION_DRIBBLE_percentile": "Bypassed\nOpponents\n(dribbling)",
                "BYPASSED_DEFENDERS_BY_ACTION_DRIBBLE_percentile": "Bypassed\nDefenders\n(dribbling)",
                "total_caries_to_box_percentile": "Carries\ninto\nPenalty Area",
                "availability_between_the_lines": "Availability\nBetween\nthe Lines",
                "bypassed_defenders_through_passing_percentile" : "Bypassed\nDefenders\n(passing)",
                "chance_creation": "Chance\nCreation",
                "successful_crosses_percentile": "Succesful\nCrosses",
                "passes_into_penalty_area" : "Passes into\nPenalty Area", 
                "succesful_passes_in_behind_percentile" : "Passing\nin Behind", 
                "SHOT_XG_percentile" : "xG", 
                "SHOT_AT_GOAL_NUMBER_percentile": "Shot\nVolume",
                "running_in_behind": "Running\nIn Behind",
                "OFFENSIVE_TOUCHES_IN_PITCH_POSITION_OPPONENT_BOX_percentile" : "Offensive\nTouches in\nPenalty Area", 
                "total_vertical_actions_in_transition_percentile": "Verticality\nIn Transition"
            },
            "colors": ["#91E4FF"] * 1 + ["#B0FF91"] * 7  + ["#78C95D"] * 8 + ["#448C2D"] * 4 + ["#114F13"] * 1 + ["#2051B3"] * 0
            # colors: involvement   +  build-up   +       Chance Creation    + Finishing      +  Transition     +   Set-Piece
        }
    },
    "CENTER_FORWARD": {
        "defensive": {
            "params": [
                "defensive_involvement",
                "DEFENSIVE_TOUCHES_BY_ACTION_DUEL_percentile",
                "offensive_ground_duels_win_percentage_percentile",
                "DEFENSIVE_TOUCHES_BY_ACTION_HEADER_percentile",
                "offensive_aerial_duels_win_percentage_percentile",
                "ball_win_removed_defenders_percentile",
                "pressing_intensity",
                "total_defensive_actions_in_counterpress_percentile"               
            ],
            "labels": {
                "defensive_involvement": "Defensive\nInvolvement",
                "DEFENSIVE_TOUCHES_BY_ACTION_DUEL_percentile": "Number of\nGround Duels",
                "offensive_ground_duels_win_percentage_percentile": "Ground Duel\nWin Percentage",
                "DEFENSIVE_TOUCHES_BY_ACTION_HEADER_percentile": "Number of\nDefensive Headers",
                "offensive_aerial_duels_win_percentage_percentile": "Aerial Duel\nWin Percentage",
                "ball_win_removed_defenders_percentile": "Ball Win\nRemoved Defenders",
                "pressing_intensity": "Pressing\nIntensity",
                "total_defensive_actions_in_counterpress_percentile": "Defensive Actions\nin Counterpress"
            },
            "colors": ["#91E4FF"] * 1 + ["#FAB4B4"] * 4 + ["#D42F2F"] * 2 + ["#961111"] * 1 + ["#CD70DB"] * 0
            # colors: involvement   +  Defending   +      High pressure    + Transition    + Set-Piece
        },
        "offensive": {
            "params": [
                "OFFENSIVE_TOUCHES_percentile",
                "BYPASSED_OPPONENTS_RECEIVING_percentile",
                "HOLD_UP_PLAY_SCORE_percentile",
                "passing_accuracy_low_pass_percentile",
                "BALL_LOSS_NUMBER_percentile",
                "BYPASSED_DEFENDERS_BY_ACTION_DRIBBLE_percentile",
                "total_caries_to_box_percentile",
                "availability_between_the_lines",
                "bypassed_defenders_through_passing_percentile",
                "chance_creation",
                "passes_into_penalty_area",
                "succesful_passes_in_behind_percentile",
                "SHOT_XG_percentile",
                "SHOT_AT_GOAL_NUMBER_percentile",
                "running_in_behind",
                "OFFENSIVE_TOUCHES_IN_PITCH_POSITION_OPPONENT_BOX_percentile",
                "total_vertical_actions_in_transition_percentile",
                "SHOT_XG_AT_PHASE_SET_PIECE_percentile"
            ],
            "labels": {
                "OFFENSIVE_TOUCHES_percentile": "Offensive\nTouches",
                "BYPASSED_OPPONENTS_RECEIVING_percentile": "Bypassed\nOpponents\nReceiving",
                "HOLD_UP_PLAY_SCORE_percentile": "Hold-up\nPlay",
                "passing_accuracy_low_pass_percentile": "Passing\nAccuracy",
                "BALL_LOSS_NUMBER_percentile": "Ball Losses",
                "BYPASSED_DEFENDERS_BY_ACTION_DRIBBLE_percentile": "Bypassed\nDefenders\n(dribbling)",
                "total_caries_to_box_percentile": "Carries into\nPenalty Area",
                "availability_between_the_lines": "Availability\nBetween\nthe Lines",
                "bypassed_defenders_through_passing_percentile" : "Bypassed\nDefenders\n(passing)",
                "chance_creation": "Chance\nCreation",
                "passes_into_penalty_area" : "Passes into\nPenalty Area", 
                "succesful_passes_in_behind_percentile" : "Passing\nin Behind", 
                "SHOT_XG_percentile" : "xG", 
                "SHOT_AT_GOAL_NUMBER_percentile": "Shot\nVolume",
                "running_in_behind": "Running\nIn Behind",
                "OFFENSIVE_TOUCHES_IN_PITCH_POSITION_OPPONENT_BOX_percentile" : "Offensive\nTouches in\nPenalty Area", 
                "total_vertical_actions_in_transition_percentile": "Verticality\nIn Transition",
                "SHOT_XG_AT_PHASE_SET_PIECE_percentile": "Set-Piece xG"
            },
            "colors": ["#91E4FF"] * 1 + ["#B0FF91"] * 4  + ["#78C95D"] * 7 + ["#448C2D"] * 4 + ["#114F13"] * 1 + ["#2051B3"] * 1
            # colors: involvement   +  build-up   +       Chance Creation    + Finishing      +  Transition     +   Set-Piece
        }
    }
}


def offensive_pizza_chart(df, playerName, position, season, squadName):
    config = POSITIONS_CONFIG.get(position, {}).get('offensive')
    if not config:
        raise ValueError(f"Geen config voor {'offensive'} in {position}")
    
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

    fig.text(
        0.12, 0.92, "Involvement", size=11,
        fontproperties=font_bold.prop, color="#000000"
    )
    fig.text(
        0.29, 0.92, "Build-up", size=11,
        fontproperties=font_bold.prop, color="#000000"
    )
    fig.text(
        0.42, 0.92, "Chance Creation", size=9,
        fontproperties=font_bold.prop, color="#000000"
    )
    fig.text(
        0.59, 0.92, "Finishing", size=11,
        fontproperties=font_bold.prop, color="#000000"
    )
    fig.text(
        0.74, 0.91, "Offensive\nTransition", size=10,
        fontproperties=font_bold.prop, color="#000000"
    )
    fig.text(
        0.88, 0.92, "Set-Piece", size=11,
        fontproperties=font_bold.prop, color="#000000"
    )
    
    # En dan gaan we kleurtjes toevoegen
    fig.patches.extend([
        plt.Rectangle(
            (0.08, 0.91), 0.03, 0.03, fill=True, color="#91E4FF",
            transform=fig.transFigure, figure=fig),
        plt.Rectangle(
            (0.25, 0.91), 0.03, 0.03, fill=True, color="#B0FF91",
            transform=fig.transFigure, figure=fig),
        plt.Rectangle(
            (0.38, 0.91), 0.03, 0.03, fill=True, color="#78C95D",
            transform=fig.transFigure, figure=fig),
        plt.Rectangle(
            (0.55, 0.91), 0.03, 0.03, fill=True, color="#448C2D",
            transform=fig.transFigure, figure=fig),
        plt.Rectangle(
            (0.70, 0.91), 0.03, 0.03, fill=True, color="#114F13",
            transform=fig.transFigure, figure=fig),
        plt.Rectangle(
            (0.84, 0.91), 0.03, 0.03, fill=True, color="#2051B3",
            transform=fig.transFigure, figure=fig)])

    return fig

def defensive_pizza_chart(df, playerName, position, season, squadName):
    config = POSITIONS_CONFIG.get(position, {}).get('defensive')
    if not config:
        raise ValueError(f"Geen config voor {'defensive'} in {position}")
    
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

    fig.text(
        0.13, 0.92, "Involvement", size=11,
        fontproperties=font_bold.prop, color="#000000"
    )
    fig.text(
        0.30, 0.92, "Defending", size=11,
        fontproperties=font_bold.prop, color="#000000"
    )
    fig.text(
        0.48, 0.92, "Pressing", size=11,
        fontproperties=font_bold.prop, color="#000000"
    )
    fig.text(
        0.64, 0.91, "Defensive\nTransition", size=10,
        fontproperties=font_bold.prop, color="#000000"
    )
    fig.text(
        0.82, 0.92, "Set-Piece", size=11,
        fontproperties=font_bold.prop, color="#000000"
    )
    
    # En dan gaan we kleurtjes toevoegen
    fig.patches.extend([
        plt.Rectangle(
            (0.09, 0.91), 0.03, 0.03, fill=True, color="#91E4FF",
            transform=fig.transFigure, figure=fig),
        plt.Rectangle(
            (0.25, 0.91), 0.03, 0.03, fill=True, color="#FAB4B4",
            transform=fig.transFigure, figure=fig),
        plt.Rectangle(
            (0.43, 0.91), 0.03, 0.03, fill=True, color="#D42F2F",
            transform=fig.transFigure, figure=fig),
        plt.Rectangle(
            (0.60, 0.91), 0.03, 0.03, fill=True, color="#961111",
            transform=fig.transFigure, figure=fig),
        plt.Rectangle(
            (0.78, 0.91), 0.03, 0.03, fill=True, color="#CD70DB",
            transform=fig.transFigure, figure=fig)])

    return fig