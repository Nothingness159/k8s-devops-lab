from flask import Flask
import socket

app = Flask(__name__)

@app.get("/health")
def health_check():
    return {"status": "ok"}
@app.route("/")
def home():
    return f"Hello, Kubernetes! Running on {socket.gethostname()}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

