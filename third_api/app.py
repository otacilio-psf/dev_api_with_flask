from flask import Flask, jsonify, request
import json

app = Flask(__name__)

to_do_list = [
    {
        "id": 1,
        "owner": "Otacilio",
        "task": "Develop GET method",
        "status": "done"
    },
    {
        "id": 2,
        "owner": "Pedro",
        "task": "Develop POST method",
        "status": "doing"
    }
]

# list all or add a task 
@app.route("/todo", methods=['GET', 'POST'])
def list_or_add_task():
    if request.method == 'GET':
        r = to_do_list
    if request.method == 'POST':
        b_data = json.loads(request.data)
        pos = len(to_do_list) + 1
        b_data["id"] = pos
        to_do_list.append(b_data)
        r = b_data
    return jsonify(r)

# return, edit or delete a task
@app.route("/todo/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def tasks(id):
    id -= 1
    if id < 0:
        return jsonify({"status": "error", "menssage": "Invalid input"})

    if request.method == 'GET':
        try: 
            r = to_do_list[id]
        except IndexError:
            msg = f"Task id: {id+1} dosen't exist"
            r = {"status": "error", "menssage": msg}
        except Exception:
            r = {"status": "error", "menssage": "Unknow error"}

    elif request.method == 'PUT':
        try:
            b_data = json.loads(request.data)
            to_do_list[id]["status"] = b_data["status"]
            r = to_do_list[id]
        except IndexError:
            msg = f"Task id: {id+1} dosen't exist"
            r = {"status": "error", "menssage": msg}
        except Exception:
            r = {"status": "error", "menssage": "Unknow error"}
    
    elif request.method == 'DELETE':
        try:
            r = to_do_list[id]
            to_do_list[id] = {"id": id+1, "status": "deleted"}
        except IndexError:
            msg = f"Task id: {id+1} dosen't exist"
            r = {"status": "error", "menssage": msg}
        except Exception:
            r = {"status": "error", "menssage": "Unknow error"}
    
    return jsonify(r)


if __name__ == '__main__':
    app.run(debug=True)
