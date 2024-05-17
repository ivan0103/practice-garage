from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/worker', methods=['GET'])
def worker_handler():
    # Implement any necessary logic here
    result = "This is the result from the worker!"
    print(result)  # Print the result to the console
    return jsonify(message=result)

if __name__ == '__main__':
    app.run(debug=True)