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
st.write('CoD Warzone stats')

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