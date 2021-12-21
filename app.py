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
    st.dataframe(df)
else:
    st.write('No data. Insert sso_token.')

st.subheader('Soldier search')
st.write('Insert tagname')
soldier_tagname = st.text_input('Soldier tagname')
if soldier_tagname:
    resp_soldier_tagname = requests.get('https://my.callofduty.com/api/papi-client/crm/cod/v2/platform/uno/username/%s/search'%soldier_tagname, cookies=cookies)
    tagname_data = resp_soldier_tagname.json()
    print(tagname_data)
else:
    st.write('No data. Insert tagname to search.')

if soldier_id:
    resp_soldier_id = requests.get('https://my.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/uno/gamer/%s/profile/type/wz'%soldier_id, cookies=cookies)
    id_data = resp_soldier_id.json()
    st.json(id_data)
else:
    st.write('No data. Look for a soldier, insert ID.')