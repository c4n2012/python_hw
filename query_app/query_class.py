import requests
import yaml

class Query(object):
    def __init__(self,symbols,query_type,day_range = 0,time_interval = 0):
        self.symbols = symbols
        self.query_type = query_type
        self.day_range = day_range
        self.time_interval = time_interval

    def make_query(self):
        res = requests.get(self.url_constructor())
        # decoded_response = res.decode("UTF-8")
        data = res.json()
        yml_data = yaml.dump(data)
        return yml_data

    def url_constructor(self):
        if self.query_type == 'realtime':
            api_url = "https://api.worldtradingdata.com/api/v1/stock?" + 'symbol=' + ','.join(self.symbols)+ "&api_token=" + "KFzAzKDWU88IAG2uQHp3i3kBa9RCkd3JAWJulicwGNHssxEwq0wElClEUACM"
            return api_url
        elif self.query_type == 'intraday':
            api_url = "https://api.worldtradingdata.com/api/v1/stock?" + 'symbol=' + ','.join(self.symbols) + "&api_token=" + "KFzAzKDWU88IAG2uQHp3i3kBa9RCkd3JAWJulicwGNHssxEwq0wElClEUACM"
            return api_url
        else:
            return 'ERROR IN URL'

