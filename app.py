from flask import Flask
# from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return ("This is Project-1.")


# @app.route('/addition/<int:a>/<int:b>')
# def addition(a, b):
#     number = a*b
#     result = {
#         "number": number,
#         "input1": a,
#         "input2": b
#     }
#     return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
