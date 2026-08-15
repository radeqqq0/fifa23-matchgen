import random
import streamlit as st

teams = [
    {"name": "Widzew Łódź", "stars": 2.0, "type": "club"},
    {"name": "Polska", "stars": 4.0, "type": "national"},
    {"name": "Legia Warszawa", "stars": 3.5, "type": "club"}
]

st.set_page_config(page_title="FIFA Random Team Generator", layout="centered")

st.html('<html lang="en">')
st.markdown("""
<style>
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

    team1_options = filter_teams(star_range_1, team_type, teams)
    team2_options = filter_teams(star_range_2, team_type, teams)

    if not team1_options or not team2_options:
        st.error("No teams in selected range")
    else:
        st.session_state['randomteam1'] = random.choice(team1_options)
        st.session_state['randomteam2'] = random.choice(team2_options)

if 'page' not in st.session_state:
    st.session_state['page'] = "settings"

if st.session_state['page'] == "settings":
    st.markdown("## FIFA 23 RANDOM TEAM GENERATOR")
    star_range_1 = st.slider(label="Choose the star range of the 1st team", min_value=0.5, max_value=5.0, step=0.5, value=(3.0, 5.0))
    star_range_2 = st.slider(label="Choose the star range of the 2nd team", min_value=0.5, max_value=5.0, step=0.5, value=(3.0, 5.0))

    team_type = st.radio("Choose the teams type", ["Clubs", "National teams", "Both"])

    clicked = st.button("Randomize")

    if clicked == True:
        random_team()
        st.session_state['page'] = "result"
        st.rerun()

elif st.session_state['page'] == "result":
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### TEAM 1")
        st.write(st.session_state['randomteam1']["name"])
            
    with col2:
        st.markdown("#### TEAM 2")
        st.write(st.session_state['randomteam2']["name"])

    comeback = st.button("Back to settings")

    if comeback == True:
        st.session_state['page'] = "settings"
        st.rerun()