def display_question(question, number):
    print(f"\nQuestion {number}: {question['question']}")

    for option, text in question["options"].items():
        print(f"{option}. {text}")


def validate_answer(answer, options):
    return answer.upper() in options


def check_answer(answer, correct_answer):
    return answer.upper() == correct_answer.upper()


def update_score(score, is_correct):
    if is_correct:
        return score + 1

    return score


def get_result_category(percentage):
    if percentage >= 80:
        return "Excellent"
    elif percentage >= 60:
        return "Good"
    elif percentage >= 40:
        return "Fair"
    else:
        return "Needs improvement"


def display_results(score, total_questions):
    incorrect = total_questions - score
    percentage = (score / total_questions) * 100

    print("\n--- QUIZ RESULTS ---")
    print(f"Correct answers: {score}")
    print(f"Incorrect answers: {incorrect}")
    print(f"Final score: {score}/{total_questions}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Category: {get_result_category(percentage)}")


def play_quiz(questions):
    score = 0

    for number, question in enumerate(questions, start=1):
        display_question(question, number)

        while True:
            answer = input("Your answer (A/B/C/D): ").strip()

            if validate_answer(answer, question["options"]):
                break

            print("Invalid option. Please choose A, B, C, or D.")

        if check_answer(answer, question["correct"]):
            print("Correct!")
            score = update_score(score, True)
        else:
            print(f"Incorrect. Correct answer: {question['correct']}")

    display_results(score, len(questions))


def main():
    questions = [
        {
            "question": "Which language is used in this assignment?",
            "options": {
                "A": "Python",
                "B": "HTML",
                "C": "CSS",
                "D": "SQL"
            },
            "correct": "A"
        },
        {
            "question": "Which keyword defines a function in Python?",
            "options": {
                "A": "function",
                "B": "def",
                "C": "fun",
                "D": "define"
            },
            "correct": "B"
        },
        {
            "question": "Which data structure stores key-value pairs?",
            "options": {
                "A": "Tuple",
                "B": "Set",
                "C": "Dictionary",
                "D": "String"
            },
            "correct": "C"
        },
        {
            "question": "Which loop iterates over a sequence?",
            "options": {
                "A": "for",
                "B": "switch",
                "C": "case",
                "D": "define"
            },
            "correct": "A"
        },
        {
            "question": "Which value represents a Boolean true?",
            "options": {
                "A": "Yes",
                "B": "1",
                "C": "True",
                "D": "On"
            },
            "correct": "C"
        }
    ]

    while True:
        play_quiz(questions)

        again = input("\nPlay again? (yes/no): ").strip().lower()

        if again not in ("yes", "y"):
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()