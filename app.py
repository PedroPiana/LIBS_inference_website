from flask import Flask,render_template,request
from inference import make_prediction

app=Flask(__name__)

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])

def predict():
    file=request.files.get("file")
    if file is None or file.filename=="":
        return render_template("index.html",error="Please select a file.")
    filename=file.filename.lower()
    if not (filename.endswith(".dat") or filename.endswith(".csv")):
        return render_template("index.html",error="The file must have a .dat or .csv extension.")
    try:
        results=make_prediction(file)
        return render_template("index.html",results=results,filename=file.filename)
    except Exception as e:
        return render_template("index.html",error=str(e))

if __name__=="__main__":
    app.run(debug=True)