import random
import streamlit as st
import pandas as pd

clubs_df = pd.read_csv("data/clubs.csv", usecols= ['Name', 'Overall', 'League'])
clubs = clubs_df.to_dict("records")

national_df = pd.read_csv("data/national.csv", usecols= ['Name', 'Overall', 'League'])
national = national_df.to_dict("records")

def ov_to_stars(overall):
    if overall >= 83:
        stars = 5
    elif overall >= 79:
        stars = 4.5
    elif overall >= 75:
        stars = 4
    elif overall >= 71:
        stars = 3.5
    elif overall >= 69:
        stars = 3
    elif overall >= 67:
        stars = 2.5
    elif overall >= 65:
        stars = 2
    elif overall >= 63:
        stars = 1.5
    elif overall >= 60:
        stars = 1
    else:
        stars = 0.5

    return stars

def format_teams(raw_list, team_type):
    formatted = []
    for team in raw_list:
        dic = {"name": team["Name"], "division": team["League"], "stars": ov_to_stars(team["Overall"]), "type": team_type}
        formatted.append(dic)
    return formatted

clubs_formatted = format_teams(clubs, "club")
national_formatted = format_teams(national, "national")
all_teams = clubs_formatted + national_formatted

st.set_page_config(page_title="FIFA Random Team Generator", layout="centered")

st.html('<html lang="en">')
st.markdown("""
<style>
    p { margin: 1px;}
    .right { text-align: right;}
    .title { color: gray;}
    .stApp { background: #14161c; color: white; }
    .team { text-align: center; }
    .label { color: #888; font-size: 0.75rem; margin-top: 0.7rem; }
    .value { font-weight: 800; }
    .stars { color: #f5c518; font-size: 1.2rem; }
</style>
""", unsafe_allow_html=True)

def filter_teams(star_range, team_type, teams):
    matching_teams = []
    for element in teams:
        if team_type == "Clubs":
            matches_type = element["type"] == "club"
        elif team_type == "National teams":
            matches_type = element["type"] == "national"
        else:
            matches_type = True
        if element["stars"] >= star_range[0] and element["stars"] <= star_range[1]:
            matches_star = True
        else:
            matches_star = False
        if matches_star and matches_type == True:
            matching_teams.append(element)

    return matching_teams

if 'randomteam1' not in st.session_state:
    st.session_state['randomteam1'] = []
    
if 'randomteam2' not in st.session_state:
    st.session_state['randomteam2'] = []

def random_team():

    team1_options = filter_teams(st.session_state['star_range_1'], st.session_state['team_type'], all_teams)
    team2_options = filter_teams(st.session_state['star_range_2'], st.session_state['team_type'], all_teams)

    if not team1_options or not team2_options:
        st.error("No teams in selected range")
    else:
        st.session_state['randomteam1'] = random.choice(team1_options)
        st.session_state['randomteam2'] = random.choice(team2_options)

if 'page' not in st.session_state:
    st.session_state['page'] = "settings"

if st.session_state['page'] == "settings":
    st.markdown("## FIFA 23 RANDOM TEAM GENERATOR")
    star_range_1 = st.slider(label="Choose the star range of the 1st team", min_value=0.5, max_value=5.0, step=0.5, value=st.session_state.get('star_range_1',(3.0, 5.0)))
    star_range_2 = st.slider(label="Choose the star range of the 2nd team", min_value=0.5, max_value=5.0, step=0.5, value=st.session_state.get('star_range_2',(3.0, 5.0)))

    saved_team_type = st.session_state.get('team_type', "Clubs")
    options = ["Clubs", "National teams", "Both"]
    saved_index = options.index(saved_team_type)
    team_type = st.radio("Choose the teams type", options, index=saved_index)

    clicked = st.button("Randomize")

    if clicked == True:
        st.session_state['star_range_1'] = star_range_1
        st.session_state['star_range_2'] = star_range_2
        st.session_state['team_type'] = team_type
        random_team()
        st.session_state['page'] = "result"
        st.rerun()

elif st.session_state['page'] == "result":
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'''
        <div class="left">
        <p class="title">TEAM NAME</p> <br>
        <p>{st.session_state['randomteam1']['name']}</p> <br>
        <p class="title">DIVISION</p> <br>
        <p>{st.session_state['randomteam1']['division']}</p>
        </div>
        ''', unsafe_allow_html=True) 
            
    with col2:
        st.markdown(f'''
        <div class="right">
        <p class="title">TEAM NAME</p> <br>
        <p>{st.session_state['randomteam2']['name']}</p> <br>
        <p class="title">DIVISION</p> <br>
        <p>{st.session_state['randomteam2']['division']}</p>
        </div>
        ''', unsafe_allow_html=True) 

    comeback = st.button("Back to settings")
    reroll = st.button("Reroll teams")

    if reroll == True:
        random_team()
        st.rerun()

    if comeback == True:
        st.session_state['page'] = "settings"
        st.rerun()