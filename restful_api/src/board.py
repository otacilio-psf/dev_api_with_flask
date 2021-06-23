from flask_restful import Resource
from flask import request
import json
from src.backlog   import backlog

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
class ListOrAddTask(Resource):
    
    def get(self):
        return to_do_list

    def post(self):
        b_data = json.loads(request.data)
        pos = len(to_do_list) + 1
        b_data["id"] = pos
        task_dic = [i for i in backlog if i["backlog_id"]==b_data["backlog_id"]][0]
        b_data["task"] = task_dic["task"]
        b_data["status"] = "to do"
        b_data.pop("backlog_id")
        backlog.remove(task_dic)
        to_do_list.append(b_data)
        return b_data

# return, edit or delete a task
class Tasks(Resource):

    def get(self, id):
        id -= 1
        if id < 0:
            return {"status": "error", "menssage": "Invalid input"}
        try: 
            return to_do_list[id]
        except IndexError:
            msg = f"Task id: {id+1} dosen't exist"
            return {"status": "error", "menssage": msg}
        except Exception:
            return {"status": "error", "menssage": "Unknow error"}

    def put(self, id):
        id -= 1
        if id < 0:
            return {"status": "error", "menssage": "Invalid input"}
        try:
            b_data = json.loads(request.data)
            to_do_list[id]["status"] = b_data["status"]
            return to_do_list[id]
        except IndexError:
            msg = f"Task id: {id+1} dosen't exist"
            return {"status": "error", "menssage": msg}
        except Exception:
            return {"status": "error", "menssage": "Unknow error"}
    
    def delete(self, id):
        id -= 1
        if id < 0:
            return {"status": "error", "menssage": "Invalid input"}
        try:
            r = to_do_list[id]
            to_do_list[id] = {"id": id+1, "status": "deleted"}
            return r
        except IndexError:
            msg = f"Task id: {id+1} dosen't exist"
            return {"status": "error", "menssage": msg}
        except Exception:
            return {"status": "error", "menssage": "Unknow error"}
