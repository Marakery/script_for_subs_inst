import requests
import time
import random



device_id = '8560953769'
username = 'ur_nickname_inst'
url = 'https://followmania.vip/Send?postTag=c2VsYW1rYW5rYWJ1YmlyYmFzZTY0&device_id=' + device_id
url_get = 'https://followmania.vip/GetUserInfo?postTag=c2VsYW1rYW5rYWJ1YmlyYmFzZTY0&device_id=' + device_id

payload_info = {"device_id": device_id}
followers = 'followers'
followers_count = '1'
credi_count = '2'

for x in range(0, 500):
    for i in range(0, 25):
        random_subs_value = random.randint(1,15)
        user_info = requests.get(url_get)
 
        resp = requests.post(
            url,
            json=dict(
                      device_id=device_id, 
                      username=username, 
                      type=followers, 
                      followers_count=random_subs_value, 
                      credi_count=credi_count
                      ),
            #verify=False,
        )
        data = resp.text
        # or if you expect json response
        data = resp.json()
        print(username,' ', user_info.text,' : ', data) 
        time.sleep(10)
    time.sleep(1800)
