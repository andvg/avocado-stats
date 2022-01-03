import requests
import json
import pandas as pd

sso_token = 'MTE2MzMwNzg5MzM5OTg5MjAyMDY6MTY0MTIyNDA1MzExMjo4MjY3NTZiYjA4YTI5ODgyNDY0MGZjM2E3OTk1YTk1YQ'
cookies = {'ACT_SSO_COOKIE': sso_token}
resp_profile = requests.get('https://my.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/uno/uno/11633078933998920206/profile/type/wz', cookies=cookies)
data = resp_profile.json()['data']['lifetime']['all']['properties']
username = resp_profile.json()['data']['username']
print('%s stats'%username)
df = pd.DataFrame(list(data.items()),columns = ['property','value'])
print(df)
                 

identity = 'https://www.callofduty.com/api/papi-client/crm/cod/:version/identities'
friends = 'https://my.callofduty.com/api/papi-client/codfriends/:version/compendium'
friends_info = 'https://my.callofduty.com/api/papi-client/stats/cod/:version/title/:game/platform/:platform/gamer/:username/profile/friends/type/:mode'
wz_profile = 'https://my.callofduty.com/api/papi-client/stats/cod/:version/title/:game/platform/:platform/gamer/:username/profile/type/:mode'
wz_matches = 'https://my.callofduty.com/api/papi-client/crm/cod/:version/title/:game/platform/:platform/gamer/:username/matches/:mode/start/:start/end/:end/details'


'''
FUNZIONA!
resp_profile = requests.get('https://my.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/uno/uno/11633078933998920206/profile/type/wz', cookies=cookies)
    myData = resp_profile.json()['data']
    resp_friends_info = requests.get('https://my.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/uno/gamer/iugav/profile/friends/type/wz', cookies=cookies)
    flData = resp_friends_info.json()

    # ltA short hand for lifetime All
    ltA = pd.DataFrame(myData['lifetime']['all']['properties'].items()).transpose()
    ltA.columns = ltA.iloc[0]
    ltA = ltA.drop([0])
    ltA = ltA.reset_index(drop=True)

    st.dataframe(ltA)

    tagnames = ['Iugav']
    for i in flData['data']:
        tagnames.append(i['username'].replace('#', '%23'))
    
    url = 'https://my.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/uno/gamer/tagname/profile/type/mp'
    for i in tagnames:
        resp = requests.get(url.replace('tagname', i), cookies=cookies)
        data = resp.json()['data']
        ltA = ltA.append(pd.Series(list(data['lifetime']['all']['properties'].values()), index=ltA.columns), ignore_index=True)

    st.dataframe(ltA)
'''