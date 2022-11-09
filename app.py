import os
from flask import Flask
from flask_httpauth import HTTPTokenAuth
from flask_cors import cross_origin

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
auth = HTTPTokenAuth(scheme="Token")


@auth.verify_token
def verify_token(token):
    return app.config['SECRET_KEY'] == token


@app.route("/")
@cross_origin()
@auth.login_required
def root():
    return {"status_code": 200, "message": "Success fetch the API!"}


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080))
    )
