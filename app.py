from flask import Flask
from flask_cors import CORS
api=Flask(__name__)
CORS(api)
#Members API Route

@api.route("/members")
def members():
    return {"members":["Member1","Member2","Member3"]}

if __name__=="__main__":
    api.run(debug=True,host="0.0.0.0",port=5000)









# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.route('/api')
# def hello():
#     return jsonify(message='Hello from Flask akjfd!')

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)



