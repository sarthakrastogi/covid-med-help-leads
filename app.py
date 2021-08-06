#import os
import tweepy as tw
#import pandas as pd
import streamlit as st

consumer_key = api_key = "REMOVED"
consumer_secret = api_secret_key = "REMOVED"

auth = tw.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token()
api = tw.API(auth, wait_on_rate_limit = True)

st.title("Search for medical equipment leads")
st.header("Enter your location and requirements below and hit Search.")
st.write("The app scrapes data from Twitter for phone numbers and other contact info where you can get leads.")


location = st.text_input('Location')
st.write("If nothing helpful shows up for your exact location, try the nearest big city")

required_option = st.radio('You require: ', ('Oxygen Cylinders'
                                            , 'Remdivisir'
                                            #, 'Favipravir', 'Fabiflu'
                                            ))
if required_option == 'Oxygen Cylinders':
    required = 'oxygen'
if required_option == 'Remdivisir':
    required = 'remdivisir'
    st.write("There are much fewer leads for Remdivisir than Oxygen cylinders, so try unverified sources if you don't get good results.")
#if required_option == 'Favipravir':
#    required = 'favipravir'
#if required_option == 'Fabiflu':
#    required = 'fabiflu'


verified = st.checkbox('Only verified sources')

if st.button('Search'):
    if verified:
        search_words = "Min_faves:10 " + str(required) + " " + str(location) + " verified"

    else:
        search_words = "Min_faves:10 " + str(required) + " " + str(location)

    date_since = "2021-03-01"

    tweets = tw.Cursor(api.search,
                  q=search_words,
                  lang="en",
                  since=date_since).items(10)

    st.write("Searching for " + search_words)
    for tweet in tweets:
        st.write(tweet.text)
        st.write("---")

st.success("For bug reports and suggesting more features, please message me on LinkedIn: [Sarthak Rastogi](https://www.linkedin.com/in/sarthakrastogi)")
st.warning("I do not take responsibility for the authenticity of the sources this app produces.")
