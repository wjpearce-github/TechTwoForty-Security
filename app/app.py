from flask import Flask, jsonify

app = Flask(__name__)

@app.after_request
def security_headers(response):
    # Added to every response, including error pages.
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Content-Security-Policy"] = "default-src 'none'; frame-ancestors 'none'"
    response.headers["Cache-Control"] = "no-store"
    return response

@app.route("/")
def home():
    return jsonify(status="running", service="capstone-api")

if __name__ == "__main__":
    # Inside a container the app has to listen on every interface, or nothing
    # outside the container can reach it. Docker's -p decides what is exposed.
    # nosemgrep: python.flask.security.audit.app-run-param-config.avoid_app_run_with_bad_host
    app.run(host="0.0.0.0", port=8000)
