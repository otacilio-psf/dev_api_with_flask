from flask import Flask, jsonify, request
import json

app = Flask(__name__)

developers = [
    {
        "id": 1,
        "name": "Otacilio",
        "stack": ["Spark", "Python"]
    },
    {
        "id": 2,
        "name": "Pedro",
        "stack": ["SQL", "Hive"]
    }
]

# return, edit or delete a developer by ID
@app.route("/dev/<int:id>", methods=['GET','PUT', 'DELETE'])
def developer(id):
    id -= 1
    if id < 0:
        msg = "Unknow error"
        return jsonify({"status": "error", "menssage": msg})
    if request.method == 'GET':
        try:
            response = developers[id]
        except IndexError:
            msg = f"Developer id:{id+1} doesn't exist"
            response = {"status": "error", "menssage": msg}
        except Exception:
            msg = "Unknow error"
            response = {"status": "error", "menssage": msg}
        return jsonify(response)
    elif request.method == 'PUT':
        b_data = json.loads(request.data)
        developers[id] = b_data
        return jsonify(b_data)
    elif request.method == 'DELETE':
        try:
            developers.pop(id)
            msg = f"Delete of id {id+1} was successful"
            response = {"status": "success", "menssage": msg}
        except IndexError:
            msg = f"Developer id:{id+1} doesn't exist"
            response = {"status": "error", "menssage": msg}
        except Exception:
            msg = "Unknow error"
            response = {"status": "error", "menssage": msg}
        return jsonify(response)

# list all developers or add a new one
@app.route("/dev", methods=['GET', 'POST'])
def list_or_add_developers():
    if request.method == 'GET':
        response = developers
    if request.method == 'POST':
        b_data = json.loads(request.data)
        pos = len(developers)+1
        b_data['id'] = pos
        developers.append(b_data)
        response = b_data
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
