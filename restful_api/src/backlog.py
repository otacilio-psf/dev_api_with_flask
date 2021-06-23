from flask_restful import Resource
from flask import request
import json

global backlog
backlog = [
    {
        "backlog_id": 1,
        "task": "Develop PUT method"
    }
]

class ListOrAddBacklog(Resource):

    def get(self):
        return backlog

    def post(self):
        b_data = json.loads(request.data)
        pos = len(backlog) + 1
        b_data["backlog_id"] = pos
        backlog.append(b_data)
        return b_data

class Backlog(Resource):

    def get(self, id):
        id -= 1
        if id < 0:
            return {"status": "error", "menssage": "Invalid input"}
        try: 
            return backlog[id]
        except IndexError:
            msg = f"Backlog id: {id+1} dosen't exist"
            return {"status": "error", "menssage": msg}
        except Exception:
            return {"status": "error", "menssage": "Unknow error"}

    def put(self, id):
        id -= 1
        if id < 0:
            return {"status": "error", "menssage": "Invalid input"}
        try:
            b_data = json.loads(request.data)
            backlog[id]["task"] = b_data["task"]
            return backlog[id]
        except IndexError:
            msg = f"Backloh id: {id+1} dosen't exist"
            return {"status": "error", "menssage": msg}
        except Exception:
            return {"status": "error", "menssage": "Unknow error"}
    
    def delete(self, id):
        id -= 1
        if id < 0:
            return {"status": "error", "menssage": "Invalid input"}
        try:
            r = backlog[id]
            backlog[id] = {"id": id+1, "status": "deleted"}
            return r
        except IndexError:
            msg = f"Backlog id: {id+1} dosen't exist"
            return {"status": "error", "menssage": msg}
        except Exception:
            return {"status": "error", "menssage": "Unknow error"}
