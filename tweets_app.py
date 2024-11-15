import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Title of the app
st.title("Airline Sentiment Analysis")

# Load the dataset
@st.cache
def load_data():
    url = 'https://raw.githubusercontent.com/ncit17153/Utsav-analy/refs/heads/main/Tweets.csv'
    data = pd.read_csv(url)
    return data

# Load the dataset
tweets = load_data()

# Display the dataset
st.write("### Dataset Preview:")
st.dataframe(tweets.head())

# Display the shape of the dataset
st.write("### Dataset Shape:")
st.write(tweets.shape)

# Display value counts of 'airline_sentiment'
st.write("### Count of Airline Sentiments:")
sentiment_counts = tweets['airline_sentiment'].value_counts()
st.write(sentiment_counts)

# Display bar chart of airline sentiments using Matplotlib
st.write("### Bar Graph: Count of Airline Sentiments (Matplotlib)")
fig, ax = plt.subplots(figsize=(8, 6))
sentiment_counts.plot(kind='bar', ax=ax, color='skyblue')
ax.set_title('Count of Airline Sentiments')
ax.set_xlabel('Sentiment')
ax.set_ylabel('Number of Tweets')
ax.set_xticklabels(sentiment_counts.index, rotation=0)
st.pyplot(fig)

# Display bar chart of airline sentiments using Plotly
st.write("### Bar Graph: Count of Airline Sentiments (Plotly)")
fig2 = px.bar(sentiment_counts,
              x=sentiment_counts.index,
              y=sentiment_counts.values,
              labels={'x': 'Sentiment', 'y': 'Number of Tweets'},
              title='Count of Airline Sentiments')
st.plotly_chart(fig2)

# Display pie chart of airline sentiments using Matplotlib
st.write("### Pie Chart: Distribution of Airline Sentiments")
fig3, ax3 = plt.subplots(figsize=(8, 8))
ax3.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90, colors=['red', 'blue', 'green'])
ax3.set_title('Distribution of Airline Sentiments')
ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig3)

# Display bar chart of tweets by airline
st.write("### Bar Graph: Tweet Counts by Airline")
airline_counts = tweets['airline'].value_counts()

fig4, ax4 = plt.subplots(figsize=(8, 6))
airline_counts.plot(kind='bar', ax=ax4, color='orange')
ax4.set_title('Tweet Counts by Airline')
ax4.set_xlabel('Airline')
ax4.set_ylabel('Number of Tweets')
ax4.set_xticklabels(airline_counts.index, rotation=0)
st.pyplot(fig4)
