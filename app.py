from flask import Flask, render_template
import os  # ✅ Needed to read environment variable

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  
    app.run(host="0.0.0.0", port=port)         
