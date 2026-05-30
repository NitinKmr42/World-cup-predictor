from Confederations import get_confederation

CONFEDERATION_BASE_ELO = {
    "UEFA": 1000,
    "CONMEBOL": 1000,
    "CONCACAF": 950,
    "CAF": 950,
    "AFC": 930,
    "OFC": 900,
    "Unknown": 900
}

K=30
HOME_ADVANTAGE =100

elo_ratings ={}
succession={
    "Czech Republic":"Czechoslovakia",
    "Czechia": "Czechoslovakia",
    "Serbia": "Yugoslavia",  
}
def get_starting_elo(team):
    conf = get_confederation(team)
    return CONFEDERATION_BASE_ELO.get(conf, 900)

def get_elo(team):
    if team not in elo_ratings:
        if team in succession and succession[team] in elo_ratings:
            elo_ratings[team]=elo_ratings[succession[team]]
        else:
            elo_ratings[team]=get_starting_elo(team)
    return elo_ratings[team]

def expected_score(elo_a , elo_b):
    return 1/(1+10 ** ((elo_b-elo_a)/400))

def update_elo(home_team,away_team,home_score,away_score,weight,neutral):
    home_elo=get_elo(home_team)
    away_elo=get_elo(away_team)
    
    home_elo_effective = home_elo if neutral else home_elo + HOME_ADVANTAGE
    home_expected = expected_score(home_elo_effective,away_elo)
    away_expected=1-home_expected

    if home_score>away_score:
        home_actual, away_actual = 1.0, 0.0
    elif home_score == away_score:
        home_actual,away_actual =0.5 , 0.5
    else:
        home_actual, away_actual = 0.0, 1.0
        
    elo_ratings[home_team] = home_elo + K * weight * (home_actual - home_expected)
    elo_ratings[away_team] = away_elo + K * weight * (away_actual - away_expected)
    