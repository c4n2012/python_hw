from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)
var_list = [{
    "fruit": "Apple",
    "size": "Large",
    "color": "Red"
}]


@app.route('/')
def main_app():
    some_title = "First Flask site" 
    return render_template("index.html", values=var_list, site_title=some_title)

@app.route('/api/add', methods=['POST'])
def add():

    try:
        if request.method == 'POST':
            data = request.get_json()
            print(request)
        var_list.append(data)
    except:
        print("This didn't work.")
    return ""


@app.route('/api/list', methods=['GET'])
def returnAll():
    return jsonify(var_list)

if __name__ == '__main__':
    app.run()
