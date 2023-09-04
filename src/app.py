from flask import Flask, jsonify,render_template
import socket

app = Flask(__name__)

# Function to fetch hostname and ip
def fetch_details():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    print("Hostname",hostname)
    print("IP",host_ip)
    return str(hostname), str(host_ip)

@app.route("/")
def hello_world():
    return "<h1>Hello World</h1>"

@app.route("/details")
def details():
    hostname,host_ip = fetch_details()
    return render_template("index.html",hostname=hostname,IP=host_ip)


@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)