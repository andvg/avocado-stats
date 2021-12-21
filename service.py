import requests
import json
import pandas as pd

sso_token = 'x'
cookies = {'ACT_SSO_COOKIE': sso_token}
resp_profile = requests.get('https://my.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/uno/uno/11633078933998920206/profile/type/wz', cookies=cookies)
data = resp_profile.json()['data']['lifetime']['all']['properties']
username = resp_profile.json()['data']['username']
print('%s stats'%username)
df = pd.DataFrame(list(data.items()),columns = ['property','value'])
print(df)

