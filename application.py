from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/application-form')
def application_form():

    """Form for inputting name, desired salary and desired position"""

    return render_template("application-form.html")

@app.route('/application', methods=["POST"])
def application():

    """Returns string stating what user entered"""

    Firstname = request.form.get("firstname")
    Lastname = request.form.get("lastname")
    Salary = request.form.get("salary")
    Job = request.form.get("job")

    return render_template("application.html",
                            firstname=Firstname,
                            lastname=Lastname,
                            salary=Salary,
                            job=Job)


if __name__ == "__main__":
    app.run(debug=True)
