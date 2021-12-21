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
sso_token = st.text_input('Enter sso_token')
if sso_token:
    cookies = {'ACT_SSO_COOKIE': sso_token}
    resp_profile = requests.get('https://my.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/uno/uno/11633078933998920206/profile/type/wz', cookies=cookies)
    myData = resp_profile.json()['data']
    resp_friends_info = requests.get('https://my.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/uno/gamer/iugav/profile/friends/type/wz', cookies=cookies)
    flData = resp_friends_info.json()

    # ltA short hand for lifetime All
    ltA = pd.DataFrame(myData['lifetime']['all']['properties'].items()).transpose()
    ltA.columns = ltA.iloc[0]
    ltA = ltA.drop([0])
    ltA = ltA.reset_index(drop=True)

    #ltM short hand for lifetime Mode
    ltM = pd.DataFrame()
    for key in myData['lifetime']['mode'].keys():
        df = pd.DataFrame(myData['lifetime']['mode'][key]['properties'].items()).transpose()
        df.columns = [key + j for j in df.iloc[0]]
        df = df.drop([0])
        df = df.reset_index(drop=True)
        ltM = pd.concat([ltM, df], sort=False, axis=1)

    #ltW short hand for lifetime Weapon
    ltW = pd.DataFrame()
    weaponClassDict = {
        'Snipers': ['AX-50', 'HDR', 'Dragunov'],
        'Lethals': ['Frag', 'Thermite', 'Semtex', 'Claymore', 'C4', 'Trip Mine', 'Throwing Knife', 'Molotov'],
        'LMGs': ['M91', 'MG34', 'SA87', 'PKM', 'Holger-26'],
        'Launchers': ['PILA', 'RPG-7', 'JOKR', 'STRELA-P', 'UNKNOWN Launcher'],
        'Pistols': ['.357', '1911', 'X16', '.50 GS', 'M19'],
        'Assault Rifles': ['FAL', 'RAM-7', 'M4A1', 'FR 5.56', 'M13', 'AK-47', 'Kilo-141', 'FN Scar 17', 'Oden'],
        'Melee Primary': ['Riot Shield'],
        'Shotguns': ['725', 'Origin 12', 'Model 680', 'R9-0 Shotgun'],
        'Submachine Guns': ['MP7', 'AUG', 'P90', 'MP5', 'PP19 Bizon', 'Uzi'],
        'Marksman Rifles': ['MK2 Carbine', 'Kar98K', 'EBR-14'],
        'Melee Secondary': ['Knife']
    }
    weaponClassList = []
    for key in weaponClassDict:
        for wp in weaponClassDict[key]:
            weaponClassList.append(wp)
    n = 0
    for wc in myData['lifetime']['itemData'].keys():
        if not wc == 'tacticals':
            for key in myData['lifetime']['itemData'][wc]:
                df = pd.DataFrame(myData['lifetime']['itemData'][wc][key]['properties'].items()).transpose()
                df.columns = [weaponClassList[n] + j for j in df.iloc[0]]
                df = df.drop([0])
                df = df.reset_index(drop=True)
                ltW = pd.concat([ltW, df], sort=False, axis=1)
                n += 1

    #loop for adding friends to data ltA, ltM, ltW DataFrames
    for i in flData:
        usernames.append(i['username'])
        ltA = ltA.append(pd.Series(list(i['lifetime']['all']['properties'].values()), index=ltA.columns), ignore_index=True)
        modeList = []
        for mode in i['lifetime']['mode'].keys():
            for j in i['lifetime']['mode'][mode]['properties'].values():
                modeList.append(j)
        weaponList = []
        for wc in i['lifetime']['itemData'].keys():
            if not wc == 'tacticals':
                for wp in i['lifetime']['itemData'][wc].keys():
                    for j in i['lifetime']['itemData'][wc][wp]['properties'].values():
                        weaponList.append(j)
        ltM = ltM.append(pd.Series(modeList, index=ltM.columns), ignore_index=True)
        ltW = ltW.append(pd.Series(weaponList, index=ltW.columns), ignore_index=True)

    # removes # Activision Account Identifier:x
    usernames = [x[:x.find("#")] if x.find("#") > -1 else x for x in usernames]

    ltA.insert(loc=0, column='usernames', value=pd.Series(usernames))
    ltM.insert(loc=0, column='usernames', value=pd.Series(usernames))
    ltW.insert(loc=0, column='usernames', value=pd.Series(usernames))


    st.dataframe(ltW)

else:
    st.write('No data.')