from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    marks = [int(data[key]) for key in data]
    total = sum(marks)
    percentage = (total / (len(marks) * 100)) * 100
    
    return jsonify({"total": total, "percentage": round(percentage, 2)})

if __name__ == "__main__":
    app.run(debug=True)
