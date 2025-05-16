from flask import Flask, request, render_template, jsonify, send_file
import pandas as pd
import os
import uuid
from datetime import datetime
import matplotlib.pyplot as plt

app = Flask(__name__)
os.makedirs("results", exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start", methods=["POST"])
def start():
    session_id = str(uuid.uuid4())
    form = request.form
    return render_template(
        f"test_{form['test_type']}.html",
        session_id=session_id,
        name=form["name"],
        participant_id=form["participant_id"],
        age=form["age"],
        gender=form["gender"],
        education=form["education"],
        job=form["job"],
        marital_status=form["marital_status"],
        attempt=form["attempt"],
        test_type=form["test_type"]
    )

@app.route("/submit/<session_id>", methods=["POST"])
def submit(session_id):
    data = request.json
    name = data["name"]
    test_type = data["test_type"]
    results = data["answers"]
    df = pd.DataFrame(results)
    df["name"] = name
    df["test_type"] = test_type
    df["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    filename = f"{name}_{test_type}_{session_id}.xlsx"
    filepath = f"results/{filename}"
    df.to_excel(filepath, index=False)

    # رسم نمودار زمان واکنش
    plt.figure()
    plt.plot(df['rt'], marker='o')
    plt.title(f"تغییرات زمان پاسخ ({test_type})")
    plt.xlabel("تست")
    plt.ylabel("زمان واکنش (ثانیه)")
    chart_path = f"results/{name}_{test_type}_chart.png"
    plt.savefig(chart_path)

    return jsonify({"file": filename, "chart": chart_path})

@app.route("/download/<filename>")
def download(filename):
    return send_file(f"results/{filename}", as_attachment=True)

@app.route("/chart/<filename>")
def chart(filename):
    return send_file(f"results/{filename}", mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
