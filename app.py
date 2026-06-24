from flask import Flask, render_template, request, redirect, url_for
from models import db, Patient

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


# AI Prediction Function
def predict_health(glucose, haemoglobin, cholesterol):

    if glucose >= 140 and cholesterol >= 200:
        return "High Diabetes & Cholesterol Risk"

    elif glucose >= 140:
        return "High Diabetes Risk"

    elif cholesterol >= 200:
        return "High Cholesterol Risk"

    elif haemoglobin < 12:
        return "Possible Anemia"

    else:
        return "Normal Health"


# Home Page
@app.route("/")
def home():

    patients = Patient.query.all()

    return render_template("index.html", patients=patients)


# Add Patient
@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":

        fullname = request.form["fullname"]
        dob = request.form["dob"]
        email = request.form["email"]
        glucose = float(request.form["glucose"])
        haemoglobin = float(request.form["haemoglobin"])
        cholesterol = float(request.form["cholesterol"])

        remarks = predict_health(glucose, haemoglobin, cholesterol)

        patient = Patient(
            fullname=fullname,
            dob=dob,
            email=email,
            glucose=glucose,
            haemoglobin=haemoglobin,
            cholesterol=cholesterol,
            remarks=remarks
        )

        db.session.add(patient)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("add.html")


# Edit Patient
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    patient = Patient.query.get_or_404(id)

    if request.method == "POST":

        patient.fullname = request.form["fullname"]
        patient.dob = request.form["dob"]
        patient.email = request.form["email"]
        patient.glucose = float(request.form["glucose"])
        patient.haemoglobin = float(request.form["haemoglobin"])
        patient.cholesterol = float(request.form["cholesterol"])

        patient.remarks = predict_health(
            patient.glucose,
            patient.haemoglobin,
            patient.cholesterol
        )

        db.session.commit()

        return redirect(url_for("home"))

    return render_template("edit.html", patient=patient)


# Delete Patient
@app.route("/delete/<int:id>")
def delete(id):

    patient = Patient.query.get_or_404(id)

    db.session.delete(patient)
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)