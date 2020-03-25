import requests
import json


hash_data = ['4de24330a881d360a84a1faea1eb161a4e9a52664269e6ca07d6c7422651b7f6','9e244a09567ff082c62a32ce938279bc2585dac4f1a2956d367f99b67b3291c6']

for check_hash in hash_data:

    header = {"Accept": "application/json"}
    url = "http://asset-test.88gongxiang.com/service/tx/hash?" + f"hash={check_hash}&ts=1584426366989"
    r = requests.get(url=url,headers=header)
    bumo_token = r.json()["data"]["operation"]["payAssetOpertion"][0]["amount"]
    bumo_token = eval(bumo_token)
    bumo_token = round(bumo_token/100000000,6)
    print(bumo_token == 0.716250)