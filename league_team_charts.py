import matplotlib.pyplot as plt
import pandas as pd

def league_strength(df_squad_ratings, competitionName):
    """Toont de relatieve sterkte van alle competities, met highlight van de target competitie."""
    league_avg = df_squad_ratings.groupby('competitionName')['competition_avg'].mean().reset_index()
    league_avg = league_avg.sort_values('competition_avg')
    
    plt.figure(figsize=(20, 1))
    plt.scatter(league_avg['competition_avg'], [0]*len(league_avg), color='grey', s=100)
    
    # Highlight de target competitie
    target = league_avg[league_avg['competitionName'] == competitionName]
    if not target.empty:
        plt.scatter(target['competition_avg'], [0], color='red', s=150)
        plt.text(target['competition_avg'].values[0], 0.03, target['competitionName'].values[0],
                 ha='center', color='red')

    # Highlight Jupiler Pro League
    own = league_avg[league_avg['competitionName'] == 'Jupiler Pro League']
    if not own.empty:
        plt.scatter(own['competition_avg'], [0], color='blue', s=150)
        plt.text(own['competition_avg'].values[0], -0.04, 'Jupiler Pro League',
                 ha='center', color='blue')

    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.xlabel('League Strength (average squad value)')
    return plt.gcf()  # return de figure i.p.v. plt.show()


def team_position(df_squad_ratings, squadId, competitionName, season):
    """Toont de relatieve sterkte van het team binnen zijn competitie."""
    league_teams = df_squad_ratings[
        (df_squad_ratings['competitionName'] == competitionName) &
        (df_squad_ratings['season'] == season)
    ].sort_values('value')
    
    plt.figure(figsize=(20, 1))
    plt.scatter(league_teams['value'], [0]*len(league_teams), color='grey', s=100)
    
    team = league_teams[league_teams['squadId'] == squadId]
    if not team.empty:
        x = team['value'].values[0]  # één enkele float
        y = 0
        plt.scatter(x, y, color='green', s=150)
        plt.text(x, 0.03, team['squadName'].values[0], ha='center', color='green')

    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.xlabel('Team Strength (squad value)')
    return plt.gcf()
