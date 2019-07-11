import requests, json
import yaml

api_url = "https://api.worldtradingdata.com/api/v1/mutualfund?symbol=AAAAX,AAADX,AAAGX&api_token=demo"

def get_data_from_remote_api(api_url):
    res = requests.get(api_url)
    # decoded_response = res.decode("UTF-8")
    data = res.json()
    yml_data = yaml.dump(data)
    print(yml_data)
    print(res.status_code)

get_data_from_remote_api(api_url)

# get_response = requests.post('https://api.worldtradingdata.com/api/v1/stock?symbol=AMZN&api_token=0tkx6y1tk3MUvuaNBrye2iIhBACthLoa0gcLHTUSvON2qU7nHKHgmaHMucGn')
# requests.post('https://httpbin.org/post', data={'key':'value'})
# print(get_response.text)
# print(post_resonse.status_code)


