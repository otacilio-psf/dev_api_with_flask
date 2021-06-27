from flask          import Flask
from flask_restful  import Api
from src.Developers import Developer, Developers
from src.Tasks      import Task, Tasks

app = Flask(__name__)
api = Api(app)

api.add_resource(Developers, "/developers")
api.add_resource(Developer, "/developer/<int:id>")
api.add_resource(Tasks, "/tasks")
api.add_resource(Task, "/task/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)