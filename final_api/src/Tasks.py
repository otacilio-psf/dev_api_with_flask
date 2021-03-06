from flask_restful     import Resource
from flask             import request
from flask_httpauth    import HTTPBasicAuth
from werkzeug.security import check_password_hash
from src.models        import Tasks_model, Developers_model, Users

auth = HTTPBasicAuth()

@auth.verify_password
def verify(user, password):
    if not (user, password):
        return False
    user_pass = Users.query.filter_by(user=user, active=1).first()
    if not user_pass:
        return False
    return check_password_hash(user_pass.password, password)

class Tasks(Resource):
    @auth.login_required
    def post(self):
        b_data = request.json
        try:
            dev = Developers_model.query.filter_by(id=b_data["developer_id"]).first()
            task = Tasks_model(task=b_data["task"],
                               status="To do",
                               developer_id=b_data["developer_id"],
                               developer=dev)
            response = {
                    "id": task.id,
                    "task": task.task,
                    "status": task.status,
                    "owner": task.developer.name
                }
            task.save()
        except Exception as e:
            response = {
                "status": "Error",
                "menssage": f"Error: {e}"
            }
        return response

    def get(self):
        tasks = Tasks_model.query.all()
        response = []
        try:
            for task in tasks:  
                r = {
                    "id": task.id,
                    "task": task.task,
                    "status": task.status,
                    "owner": task.developer.name,
                    "email": task.developer.email
                }
                response.append(r)
        except Exception as e:
            response = {
                "status": "Error",
                "menssage": f"Error: {e}"
            }
        return response

class Task(Resource):

    def get(self, id):
        task = Tasks_model.query.filter_by(id=id).first()
        try:
            response = {
                    "id": task.id,
                    "task": task.task,
                    "status": task.status,
                    "owner": task.developer.name,
                    "email": task.developer.email
                }
        except AttributeError:
            response = {
                "status": "Error",
                "menssage": f"Id: {id} doesn't exist"
            }
        except Exception as e:
            response = {
                "status": "Error",
                "menssage": f"Error: {e}"
            }
        return response

    @auth.login_required
    def put(self, id):
        task = Tasks_model.query.filter_by(id=id).first()
        b_data = request.json
        try:
            task.status = b_data["status"]
            task.save()
            response = {
                    "id": task.id,
                    "task": task.task,
                    "status": task.status,
                    "owner": task.developer.name,
                    "email": task.developer.email
                }
        except Exception as e:
            response = {
                "status": "Error",
                "menssage": f"Error: {e}"
            }
        return response
    
    @auth.login_required
    def delete(self, id):
        task = Tasks_model.query.filter_by(id=id).first()
        try:
            task.delete()
            response = {
                "status": "sucess",
                "menssage": f"Delete ID {id} Sucessful"
            }
        except Exception as e:
            response = {
                "status": "Error",
                "menssage": f"Error: {e}"
            }
        return response
        