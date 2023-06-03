from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
import json

with open('db.json') as f:
    data = json.load(f)

app = Flask(__name__)

student_info = {
    "Name": "",
    "Matric_Number": "",
    "Year": "",
    "Course": "",
}

curr_question = list(data.keys())[0]
curr_response = data[curr_question]
final_answer = ""


@ app.route('/')
def home():
    curr_time = datetime.now()
    hour = int(curr_time.strftime("%H"))

    if hour >= 0 and hour < 12:
        message = "Morning"
    elif hour >= 12 and hour < 17:
        message = "Afternoon"
    else:
        message = "Evening"

    return render_template("home.html", message=message)


@ app.route("/get-to-know", methods=["GET", "POST"])
def get_info():
    if request.method == "POST":
        student_info["Name"] = request.form["name"]
        student_info["Matric_Number"] = request.form["matric-number"]
        student_info["Year"] = request.form.get("year-of-study")
        student_info["Course"] = request.form.get("course")
        return redirect("/introduction")

    return render_template("information.html")


@ app.route("/introduction", methods=["GET", "POST"])
def intro():
    if request.method == "POST":
        response = request.form["response-button"]

        if response == "I want to develop a Database":
            return redirect("/develop-db")

        global curr_response
        global curr_question

        next_decision = curr_response[response]
        question = list(next_decision.keys())[0]
        next_responses = next_decision[question]
        curr_response = next_responses
        curr_question = question

        return redirect("/question")

    else:
        responses = list(curr_response.keys())
        return render_template("introduction.html", name=student_info["Name"], main_question=curr_question, responses=responses)


@ app.route("/question", methods=["GET", "POST"])
def questions():
    if request.method == "POST":
        response = request.form["response-button"]

        global curr_response
        global curr_question
        global final_answer

        next_decision = curr_response[response]

        if isinstance(next_decision, dict):
            question = list(next_decision.keys())[0]
            curr_question = question
            next_responses = next_decision[question]
            curr_response = next_responses

            return render_template("questions.html", main_question=question, responses=next_responses)
        else:
            curr_question = response
            final_answer = next_decision
            return redirect("/answer")

    return render_template("questions.html", main_question=curr_question, responses=curr_response)


@ app.route("/answer", methods=["GET", "POST"])
def answer():
    if request.method == "POST":

        global curr_question
        global curr_response

        curr_question = list(data.keys())[0]
        curr_response = data[curr_question]

        return redirect("/introduction")
    if "img_name" in request.args:
        return render_template("answer.html", img_name=request.args["img_name"])
    if "question" in request.args:
        return render_template("answer.html", question=request.args["question"], answer=request.args["answer"])
    return render_template("answer.html", question=curr_question, answer=final_answer)


@ app.route("/develop-db", methods=["GET", "POST"])
def develop_db():
    db_data = data['What would you like to learn today?']['I want to develop a Database']


    if request.method == "POST":
        primacyEffect = int(request.form.get('primacyEffect'))
        recencyEffect = int(request.form.get('recencyEffect'))
        # primacyEffect is a number between 1 to 3
        # recencyEffect is a number between 1 to 3
        # write a code that take care of the possible combinations of primacyEffect and recencyEffect
        # and return the appropriate image name
        # use switch case
        if primacyEffect == 1:
            if recencyEffect == 1:
                image_name = "recalled_low_pe_low_re.jpeg"
            elif recencyEffect == 2:
                image_name = "recalled_low_pe_mid_re.jpeg"
            elif recencyEffect == 3:
                image_name = "recalled_low_pe_high_re.jpeg"
        elif primacyEffect == 2:
            if recencyEffect == 1:
                image_name = "recalled_mid_pe_low_re.jpeg"
            elif recencyEffect == 2:
                image_name = "recalled_mid_pe_mid_re.jpeg"
            elif recencyEffect == 3:
                image_name = "recalled_mid_pe_high_re.jpeg"
        elif primacyEffect == 3:
            if recencyEffect == 1:
                image_name = "recalled_high_pe_low_re.jpeg"
            elif recencyEffect == 2:
                image_name = "recalled_high_pe_mid_re.jpeg"
            elif recencyEffect == 3:
                image_name = "recalled_high_pe_high_re.jpeg"



        
        return redirect(url_for('.answer', img_name=image_name))
    return render_template("develop_db.html")


app.run(debug=True)
