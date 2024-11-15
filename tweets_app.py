# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Airline Tweets Analysis")

# Load the dataset
@st.cache
def load_data():
    url = 'https://raw.githubusercontent.com/ncit17153/Utsav-analy/refs/heads/main/Tweets.csv'
    data = pd.read_csv(url)
    return data

# Load the data
tweets = load_data()

# Display the dataset
st.write("### Dataset Preview:")
st.dataframe(tweets.head())

# Bargraph for airline sentiment
st.write("### Count of Airline Sentiments")
sentiment_counts = tweets['airline_sentiment'].value_counts()

# Plot bar chart using Matplotlib
fig, ax = plt.subplots(figsize=(8, 6))
sentiment_counts.plot(kind='bar', ax=ax, color='skyblue')
ax.set_title('Count of Airline Sentiments')
ax.set_xlabel('Sentiment')
ax.set_ylabel('Number of Tweets')
ax.set_xticklabels(sentiment_counts.index, rotation=0)

# Display the bar chart in Streamlit
st.pyplot(fig)

# Pie chart for airline sentiment
st.write("### Pie Chart: Distribution of Airline Sentiments")
fig2, ax2 = plt.subplots(figsize=(8, 8))
ax2.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90, colors=['red', 'blue', 'green'])
ax2.set_title('Distribution of Airline Sentiments')

# Display the pie chart in Streamlit
st.pyplot(fig2)

# Bargraph for airline column
st.write("### Tweet Counts by Airline")
airline_counts = tweets['airline'].value_counts()

fig3, ax3 = plt.subplots(figsize=(8, 6))
airline_counts.plot(kind='bar', ax=ax3, color='orange')
ax3.set_title('Tweet Counts by Airline')
ax3.set_xlabel('Airline')
ax3.set_ylabel('Number of Tweets')
ax3.set_xticklabels(airline_counts.index, rotation=0)

# Display the airline bar chart in Streamlit
st.pyplot(fig3)
