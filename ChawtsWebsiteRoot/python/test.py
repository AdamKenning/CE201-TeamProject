from flask import Flask, jsonify, request

app = Flask(__name__)

# A simple route to send a "name" value to the frontend
@app.route('/get-name', methods=['GET'])
def get_name():
    return jsonify({"name": "Amanda"})

if __name__ == '__main__':
    app.run(debug=True)
