from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home(): 
    return "hello this is my Fist deployed program"
# @app.route('/Smart_Trip_Planner/<string:source>/<string:destination>/<int:days>/<int:budget>', methods=['GET'])
# def smart_trip_planner(source , destination, days, budget):
#     detail=at.generate_trip_plan(source, destination, days, budget).replace("\n", "<br>")
#     return jsonify(detail)
app.run(debug=True)
