import requests
import json

headers = {'User-Agent': 'com.ss.android.ugc.trill/584 (Linux; U; Android 5.1.1; en_US; LG-H961N;',
           'X-SS-REQ-TICKET': '1541500434739',
           'X-Tt-Token': '002447bd7d6a5c792cb223b1151e399e0402e5fdcf768ab9f96930b63dc169d353480340ec7abaa1856d8133dcfe12363b42',
           'sdk-version': '1',
           'X-SS-TC': '0',
}

#payload = {}

payload = {
    "source": "discover",
    "ts": "1556178331",
    "js_sdk_version": "",
    "app_type": "normal",
    "manifest_version_code": "583",
    "_rticket": "1556178332328",
    "app_language": "en",
    "iid": "6683055906148435713",
    "channel": "googleplay",
    "device_type": "MIX%202",
    "language": "en",
    "account_region": "VN",
    "resolution": "1080*2030",
    "openudid": "b19f5ff713b925ef",
    "update_version_code": "5830",
    "sys_region": "US",
    "os_api": "26",
    "uoo": "0",
    "is_my_cn": "0",
    "timezone_name": "Asia%2FHo_Chi_Minh",
    "dpi": "440",
    "carrier_region": "VN",
    "ac": "wifi",
    "device_id": "6620810330052445697",
    "pass-route": "1",
    "mcc_mnc": "45204",
    "os_version": "8.0.0",
    "timezone_offset": "25200",
    "version_code": "583",
    "carrier_region_v2": "452",
    "app_name": "trill",
    "ab_version": "5.8.3",
    "version_name": "5.8.3",
    "device_brand": "Xiaomi",
    "ssmix": "a",
    "pass-region": "1",
    "device_platform": "android",
    "build_number": "5.8.3",
    "region": "US",
    "aid": "1180",
    "as": "a1qwert123",
    "cp": "cbfhckdckkde1"
}

API_URL = "https://api2.musical.ly/passport/user/login/"
params = {
    "mix_mode": "1",
    "username": "",
    "email": "",}

print(requests.post(API_URL, data=json.dumps(payload), headers=headers).content)
