import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import base64 #For Downloading data as a CSV file

st.title('NBA Player Analysis')

st.markdown('''
This App performs webscraping for finding and analysing on individual player stats in the NBA
* **Python Libraries:** Streamlit, Pandas, Numpy, Matplotlib, Seaborn, base64
* **Source:** Basketball Reference - https://www.basketball-reference.com/
''')
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

st.sidebar.header('Input Queries')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950, 2024))))

#Scraping for Datas
@st.cache_data
def load_data(year):
    url = 'https://www.basketball-reference.com/leagues/NBA_' + str(year) + '_per_game.html'
    html = pd.read_html(url, header=0)
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index) #Deletes Repeated Headings in Content
    raw = raw.fillna(0)
    playerstats = raw.drop(['Rk'], axis=1)
    return playerstats
playerstats = load_data(selected_year)


#Sidebar - Team Selection
sorted_unique_team = sorted(playerstats.Tm.unique())
selected_team = st.sidebar.multiselect('Team', sorted_unique_team)

#Sidebar - Position Selection
unique_pos = ['C', 'PF', 'SF', 'PG', 'SG']
selected_pos = st.sidebar.multiselect('Position', unique_pos)

#Filtering Data
df_selected_team = playerstats[(playerstats.Tm.isin(selected_team)) & (playerstats.Pos.isin(selected_pos))]

st.header('Display Player Stats of Selected Team(s)')
st.write('Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.')
st.dataframe(df_selected_team)

#Sidebar - Category Selection for Chart/Charts
unique_c = playerstats.columns
c_category = st.sidebar.multiselect('1st Chart', unique_c)


#Visualising Data

#unique_c = list(c_category)
print(list(enumerate(c_category)))
plt.figure(figsize= (30,45))
for i in enumerate(c_category):
    display = plt.subplot(2,1,i[0]+1)
    display = plt.figure()
    df_selected_team[c_category].value_counts().plot(kind='bar', color='orange')
    plt.show()
    st.pyplot(display)

graph = st.sidebar.multiselect('Graph', unique_c)
print(list(enumerate(graph)))
plt.figure(figsize= (30,45))
for i in enumerate(graph):
    display = plt.subplot(2,1,i[0]+1)
    display = plt.figure()
    df_selected_team[graph].value_counts().plot(kind='bar', color='orange')
    plt.show()
    st.pyplot(display)
else:
    graph = []

def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)
