from flask         import Flask
from flask_restful import Api
from src.board     import ListOrAddTask, Tasks
from src.backlog   import ListOrAddBacklog, Backlog

app = Flask(__name__)
api = Api(app)

api.add_resource(ListOrAddTask, "/board")
api.add_resource(Tasks ,"/board/<int:id>")
api.add_resource(ListOrAddBacklog ,"/backlog")
api.add_resource(Backlog ,"/backlog/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)