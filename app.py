import streamlit as st
import requests

st.title('🥑 Avocado Team')
st.write('CoD Warzone stats')

sso_token = st.text_input('Enter sso_token')

def connect():
    cookies = {'ACT_SSO_COOKIE': sso_token}
    resp_profile = requests.get('https://my.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/uno/uno/11633078933998920206/matches/wz/start/0/end/0/details', cookies=cookies)
    uno = resp_profile.json()['data']['matches']
    st.json(uno)