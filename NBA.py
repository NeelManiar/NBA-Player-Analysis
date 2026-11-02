import urllib3
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import base64
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Page Title
st.title('NBA Player Analysis')

st.markdown('''
This app analyzes NBA player statistics.

* **Libraries Used:** Streamlit, Pandas, Matplotlib
* **Dataset Source:** player_index.csv
''')

# Sidebar
st.sidebar.header('Input Queries')

selected_year = st.sidebar.selectbox(
    'Year',
    list(reversed(range(1950, 2026)))
)

# Load Data
@st.cache_data
def load_data(year):

    df = pd.read_csv("player_index.csv")

    df = df.fillna(0)

    return df

playerstats = load_data(selected_year)

# Team Selection
sorted_unique_team = sorted(playerstats['TEAM_ABBREVIATION'].astype(str).unique())

selected_team = st.sidebar.multiselect(
    'Team',
    sorted_unique_team,
    sorted_unique_team
)

# Position Selection
unique_pos = sorted(playerstats['POSITION'].astype(str).unique())

selected_pos = st.sidebar.multiselect(
    'Position',
    unique_pos,
    unique_pos
)

# Filtering Data
df_selected_team = playerstats[
    (playerstats['TEAM_ABBREVIATION'].astype(str).isin(selected_team)) &
    (playerstats['POSITION'].astype(str).isin(selected_pos))
]

# Display Data
st.header('Player Statistics')

st.write(
    'Data Dimension: ' +
    str(df_selected_team.shape[0]) +
    ' rows and ' +
    str(df_selected_team.shape[1]) +
    ' columns.'
)

st.dataframe(df_selected_team)

# Graph Selection
numeric_columns = df_selected_team.select_dtypes(
    include=['float64', 'int64']
).columns

selected_graph = st.sidebar.selectbox(
    'Select Statistical Column',
    numeric_columns
)

# Visualization
st.subheader(f'{selected_graph} Distribution')

fig, ax = plt.subplots(figsize=(10, 5))

df_selected_team[selected_graph].hist(ax=ax)

ax.set_xlabel(selected_graph)
ax.set_ylabel('Frequency')

st.pyplot(fig)

# Download CSV
def filedownload(df):

    csv = df.to_csv(index=False)

    b64 = base64.b64encode(csv.encode()).decode()

    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'

    return href

st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)