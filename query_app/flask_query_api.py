from flask import Flask, request, jsonify, render_template
import yaml
from query_class import Query


app = Flask(__name__)


@app.route('/query/yml_data', methods=['POST'])
def receive_yml_data():
    if request.method == 'POST':

        yml_req_src = request.get_data(cache=True, as_text=True)
        yml_data = yaml.load(yml_req_src,Loader=yaml.FullLoader)
    #    yaml_from_logic = yaml.dump(yml_data)
        print (yml_data)
        query_obj = Query(yml_data['symbols'],yml_data['query_type'])
        print(query_obj.symbols)
        if query_obj.query_type == 'intraday':
            query_obj.day_range = yml_data['day_range']
            query_obj.time_interval = yml_data['time_interval']

        yml_response = query_obj.make_query()
        print (yml_response)
        return yml_response




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003)



