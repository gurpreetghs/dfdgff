from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h2>HTML Images</h2>"
            "<p>HTML images are defined with the img tag:</p>"
    return html

# @app.route("/", methods=["GET"])
# def homepage():
#     if request.method == "GET":
#         return jsonify({"message": "Hello World!"})

PORT = int(os.environ.get("PORT", 8080))
if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=PORT)
