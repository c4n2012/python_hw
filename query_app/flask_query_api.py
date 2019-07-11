from flask import Flask, request, jsonify, render_template
import yaml

app = Flask(__name__)

@app.route('/')
def main_app():
    some_title = "First Flask site" 
    return render_template("index.html", values=var_list, site_title=some_title)

@app.route('/query/yml_data', methods=['POST'])
def receive_yml_data():
    if request.method == 'POST':
        yml_req_src = request.get_data(cache=True, as_text=True)
        yml_data = yaml.load(yml_req_src,Loader=yaml.FullLoader)
        yaml.dump(yml_data)
        # print(yml_req_src)
        # print(yml_data)
        # print(yaml.dump(yml_data))
        # yaml_converter_to_json(yml_data)
        return "200"

def yaml_converter_to_json(yml_src):
    a = jsonify(yml_src)
    print(a)    


@app.route('/api/list', methods=['GET'])
def returnAll():
    return jsonify(var_list)




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003)



