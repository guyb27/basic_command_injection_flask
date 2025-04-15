from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

def ping_host(ip):
    cmd = f"ping -c 1 {ip}"
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return e.output

@app.route("/", methods=["GET", "POST"])
def index():
    output = None
    ip = ""
    if request.method == "POST":
        ip = request.form["ip"]
        output = ping_host(ip)
    return render_template("index.html", output=output, ip=ip)

if __name__ == "__main__":
    app.run(debug=True)
