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