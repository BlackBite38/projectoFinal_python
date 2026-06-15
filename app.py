from flask import Flask, render_template, request
import sqlite3
import random

app = Flask(__name__)

def get_db_connection():
    # Abrir base de datos
    conn = sqlite3.connect("database.db")
    # Permite acceder a columnas por nombre
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    conn = get_db_connection()
    quizzes = conn.execute("SELECT * FROM quizzes").fetchall()
    conn.close()

    return render_template("index.html", quizzes=quizzes)

@app.route("/quiz/<int:id>", methods=["GET", "POST"])
def quiz(id):

    conn = get_db_connection()

    quiz = conn.execute(
        "SELECT * FROM quizzes WHERE id = ?",
        (id,)
    ).fetchone()

    questions = conn.execute(
        "SELECT * FROM questions WHERE quiz_id = ?",
        (id,)
    ).fetchall()

    score = 0

    review_data = []

    if request.method == "POST":

        for question in questions:

            selected_option = request.form.get(
                f"question-{question['id']}"
            )

            if int(selected_option) == question["correct_option"]:
                score += 1

            review_data.append({
                "question": question["question"],
                "selected": selected_option,
                "correct": question["correct_option"],
                "option1": question["option1"],
                "option2": question["option2"],
                "option3": question["option3"],
                "option4": question["option4"],
                "explanation": question["explanation"]
            })

        conn.close()


        total_questions = len(questions)

        percentage = (score / total_questions) * 100

        if percentage < 60:
            result_image = "S_sad.png"
            result_sound = "S_Sad.mp3"

        elif percentage <= 80:
            result_image = "S_neutral.png"
            result_sound = "S_Neutral.mp3"

        else:
            result_image = "S_happy.png"
            result_sound = "S_Happy.mp3"

        return render_template(
            "result.html",
            score=score,
            total=total_questions,
            percentage=percentage,
            result_image=result_image,
            result_sound=result_sound,
            review_data=review_data
        )

    conn.close()

    return render_template(
        "quiz.html",
        quiz=quiz,
        questions=questions
    )

# #=======================
# def build_questions_with_choices(questions):
#     formatted = []

#     for q in questions:

#         options = [
#             q["option_a"],
#             q["option_b"],
#             q["option_c"],
#             q["option_d"]
#         ]

#         random.shuffle(options)  # 🔥 orden aleatorio

#         formatted.append({
#             "id": q["id"],
#             "question": q["question"],
#             "options": options,
#             "correct_answer": q["correct_answer"]
#         })

#     return formatted


# @app.route("/quiz/<int:id>", methods=["GET", "POST"])
# def quiz(id):

#     conn = get_db_connection()

#     quiz = conn.execute(
#         "SELECT * FROM quizzes WHERE id = ?",
#         (id,)
#     ).fetchone()

#     questions_raw = conn.execute(
#         "SELECT * FROM questions WHERE quiz_id = ?",
#         (id,)
#     ).fetchall()

#     questions = build_questions_with_choices(questions_raw)

#     if request.method == "POST":

#         results = []
#         score = 0

#         for q in questions:

#             user_answer = request.form.get(f"question-{q['id']}")

#             is_correct = (user_answer == q["correct_answer"])

#             if is_correct:
#                 score += 1

#             results.append({
#                 "question": q["question"],
#                 "user_answer": user_answer,
#                 "correct_answer": q["correct_answer"],
#                 "is_correct": is_correct
#             })

#         conn.close()

#         return render_template(
#             "result.html",
#             score=score,
#             total=len(questions),
#             results=results
#         )

#     conn.close()

#     return render_template("quiz.html", quiz=quiz, questions=questions)



if __name__ == "__main__":
    app.run(debug=True)