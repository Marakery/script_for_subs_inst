import requests
import time


device_id = '10584148734'
username = 'mrak91'
url = 'https://followmania.vip/Send?postTag=c2VsYW1rYW5rYWJ1YmlyYmFzZTY0&device_id=' + device_id
url_get = 'https://followmania.vip/GetUserInfo?postTag=c2VsYW1rYW5rYWJ1YmlyYmFzZTY0&device_id=' + device_id

payload_info = {"device_id": device_id}
followers = 'followers'
followers_count = '20'
credi_count = '2'

for i in range(0, 25):
    user_info = requests.get(url_get)
    
    resp = requests.post(
        url,
        json=dict(
                  device_id=device_id, 
                  username=username, 
                  type=followers, 
                  followers_count=followers_count, 
                  credi_count=credi_count
                  ),
        #verify=False,
    )
    data = resp.text
    # or if you expect json response
    data = resp.json()
    print(username,' ', user_info.text,' : ', data) 
    time.sleep(10)
