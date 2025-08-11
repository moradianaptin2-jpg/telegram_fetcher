from flask import Flask, render_template, request
from fetcher import fetch_messages

app = Flask(__name__)

# صفحه اصلی
@app.route("/", methods=["GET", "POST"])
def index():
    messages = []
    if request.method == "POST":
        channel = request.form.get("channel")
        if channel:
            messages = fetch_messages(channel)
    return render_template("index.html", messages=messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
