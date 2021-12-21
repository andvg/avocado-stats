import streamlit as st
import requests
import pandas as pd
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
    for i in friends['data']['uno']:
    st.write(i['username'])
    st.json(friends)

def get_friends_info():
    resp_friends_info = requests.get('https://my.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/uno/gamer/iugav/profile/friends/type/wz', cookies=cookies)
    friends_info = resp_friends_info.json()
    st.json(friends_info)

st.title('🥑 Avocado Team')
st.header('CoD Warzone stats')
sso_token = st.text_input('Enter sso_token')
if sso_token:
    cookies = {'ACT_SSO_COOKIE': sso_token}
    resp_profile = requests.get('https://my.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/uno/uno/11633078933998920206/profile/type/wz', cookies=cookies)
    data = resp_profile.json()['data']['lifetime']['all']['properties']
    username = resp_profile.json()['data']['username']
    st.write('%s stats'%username)
    df = pd.DataFrame(list(data.items()),columns = ['property','value'])
    st.dataframe(df)
    get_friends()
    get_friends_info()
else:
    st.write('No data. Insert sso_token.')

st.subheader('Soldier search')
soldier_tagname = st.text_input('Soldier tagname')
if soldier_tagname:
    soldier_tagname = soldier_tagname.replace('#', '%23')
    resp_soldier_tagname = requests.get('https://my.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/uno/gamer/%s/profile/type/wz'%soldier_tagname, cookies=cookies)
    tagname_data = resp_soldier_tagname.json()
    st.json(tagname_data)
else:
    st.write('No data. Look for a soldier, insert ID.')