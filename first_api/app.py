from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/<int:id>")
def pessoas(id):
    return jsonify({'id': id, 'name': 'Otacilio'})

@app.route("/sum/<int:v1>/<int:v2>")
def sum_(v1,v2):
    return jsonify({'resultado': v1+v2})

@app.route("/sum_body", methods=['POST', 'GET'])
def sum_body():
    if request.method=="POST":
        body_data = json.loads(request.data)
        total = sum(body_data['valores'])
    elif request.method=='GET':
        total = 0
    return jsonify({'total': total})


if __name__ == '__main__':
    app.run(debug=True)