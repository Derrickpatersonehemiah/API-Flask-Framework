from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/Task4.1', methods=['GET'])
def get_static_response():
    response = {
        "message": "Hello, this is a static response!",
        "status": "success"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

    