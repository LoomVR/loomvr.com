from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "this is a test for gcloud. lets see if we can get this up and running"

if __name__ == "__main__":
    app.run()
