from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_static_response():
    response = {
        "message": "Hi, Task 4.2 completed succesfully!",
        "status": "success"
    }
    return jsonify(response)

@app.route('/forbidden', methods=['GET'])
def get_forbidden():
    # Trigger a 403 Forbidden error
    response = {
        "message": "simulated forbidden error.",
        "status": "error"
    }
    return jsonify(response), 403

@app.route('/error', methods=['GET'])
def get_error():
    # Intentionally raise an exception to simulate a 500 error
    raise Exception("simulated server error.")

@app.errorhandler(404)
def not_found_error(error):
    response = {
        "message": "Resource not found.",
        "status": "error"
    }
    return jsonify(response), 404

@app.errorhandler(405)
def method_not_allowed(e):
    response = {
        "message": "Method not allowed.",
        "status": "error"
    }
    return jsonify(response), 405    

@app.errorhandler(Exception)
def handle_exception(e):
    # Handle the exception and return a JSON response with status code 500
    response = {
        "message": str(e),
        "status": "error"
    }
    return jsonify(response), 500

if __name__ == '__main__':
    app.run(debug=True)