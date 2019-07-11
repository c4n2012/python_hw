from flask import Flask, jsonify, json, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/result", methods=['POST', 'GET'])
def result():
   if request.method == 'POST':
       query = request.form['query']
       response = MyService.retrieve_response(query)
       if request.headers['Content-Type'] == 'application/json':
           return jsonify(...)
       return render_template("index.html", value=response)

if __name__ == "__main__":
    app.run()