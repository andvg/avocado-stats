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
    st.table(df)
else:
    st.write('No data, insert sso_token')

st.subheader('soldier search')
soldier = st.text_input('Soldier ID')

if soldier:
    resp_soldier = requests.get('https://my.callofduty.com/api/papi-client/crm/cod/v2/platform/uno/username/%s/search'%soldier, cookies=cookies)
    soldier_data = resp_soldier.json()
    st.json(soldier_data)
else:
    st.write('No data, insert soldier ID')