import streamlit as st
import requests

st.set_page_config(
     page_title="CoD Warzone stats - Avocado Team",
     page_icon="🔫",
     layout="centered",
     initial_sidebar_state="auto",
     menu_items={
         'andreavaghi.it': "https://andreavaghi.it"
     }
 )

st.title('🥑 Avocado Team')
st.write('CoD Warzone stats')

sso_token = st.text_input('Enter sso_token')

if st.button('Go!'):
    cookies = {'ACT_SSO_COOKIE': sso_token}
    resp_profile = requests.get('https://my.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/uno/uno/11633078933998920206/profile/type/wz', cookies=cookies)
    data = resp_profile.json()['data']['lifetime']['all']['properties']
    username = resp_profile.json()['data']['username']
    st.write('%s stats'%username)
    df = pd.DataFrame(list(data.items()),columns = ['property','value'])
    st.dataframe(df)
else:
    st.write('No data')