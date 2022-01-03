import streamlit as st
import pandas as pd
import requests
import json

st.set_page_config(
     page_title="CoD Warzone stats - Avocado Team",
     page_icon="🔫",
     layout="centered",
     initial_sidebar_state="auto"
 )

def get_friends():
    resp_friends = requests.get('https://my.callofduty.com/api/papi-client/codfriends/v1/compendium', cookies=cookies)
    friends = resp_friends.json()
    st.json(friends)

def get_friends_info():
    resp_friends_info = requests.get('https://my.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/uno/gamer/iugav/profile/friends/type/wz', cookies=cookies)
    friends_info = resp_friends_info.json()
    st.json(friends_info)

st.header('CoD Warzone stats')
version = st.selectbox('API version', ['v1', 'v2'])
game = st.selectbox('Game', ['mw', 'wwii', 'boa'])
platform = st.selectbox('Platform', ['uno', 'battle', 'steam'])
username = st.text_input('Username')
mode = st.selectbox('Mode', ['wz', 'mp'])
start = '0' #Useless param - can always remain at 0
end = '0' #UTC timestamp in microseconds, defaults to 0

identity = 'https://www.callofduty.com/api/papi-client/crm/cod/v2/identities'
friends = 'https://my.callofduty.com/api/papi-client/codfriends/v1/compendium'
friends_info = 'https://my.callofduty.com/api/papi-client/stats/cod/v1/title/'+game+'/platform/'+platform+'/gamer/'+username+'/profile/friends/type/'+mode+''
wz_profile = 'https://my.callofduty.com/api/papi-client/stats/cod/v1/title/'+game+'/platform/'+platform+'/gamer/'+username+'/profile/type/'+mode+''
wz_matches = 'https://my.callofduty.com/api/papi-client/crm/cod/v2/title/'+game+'/platform/'+platform+'/gamer/'+username+'/matches/'+mode+'/start/'+start+'/end/'+end+'/details'

sso_token = st.text_input('Enter sso_token')
if sso_token:
    cookies = {'ACT_SSO_COOKIE': sso_token}

    resp_identity = requests.get(identity, cookies=cookies)
    identityData = resp_identity.json()
    st.json(identity_data)


else:
    st.write('No data.')