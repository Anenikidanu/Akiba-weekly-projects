def val_score(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")
    return score


def calculate_grade(students):
    for student in students:
        score = val_score(student['score'])

        if score >= 90:
            student['grade'] = "A"
        elif score >= 80:
            student['grade'] = "B"
        elif score >= 70:
            student['grade'] = "C"
        elif score >= 60:
            student['grade'] = "D"
        else:
            student['grade'] = "F"

    return students


def calculate_average(students):
    if not students:
        raise ValueError("Student list cannot be empty.")

    total_score = 0

    for student in students:
        total_score += student['score']

    average_score = total_score / len(students)
    return average_score


def high_and_low_scores(students):
    if not students:
        raise ValueError("Student list cannot be empty.")

    highest_score = students[0]['score']
    lowest_score = students[0]['score']

    for student in students:
        score = student['score']

        if score > highest_score:
            highest_score = score

        if score < lowest_score:
            lowest_score = score

    return highest_score, lowest_score


def count_passed_failed(students):
    passed = 0
    failed = 0

    for student in students:
        if student['score'] >= 50:
            passed += 1
        else:
            failed += 1

    return passed, failed


def students_above_average(students, average):
    above_average = []

    for student in students:
        if student['score'] > average:
            above_average.append(student)

    return above_average


def generate_report(students):
    if not students:
        raise ValueError("Student list cannot be empty.")

    # Validate every score before generating the report
    for student in students:
        val_score(student['score'])

    calculate_grade(students)

    average = calculate_average(students)
    highest, lowest = high_and_low_scores(students)
    passed, failed = count_passed_failed(students)
    above_average = students_above_average(students, average)

    print("===== STUDENT PERFORMANCE REPORT =====")

    for student in students:
        status = "Passed" if student['score'] >= 50 else "Failed"

        print(
            f"Name: {student['name']} | "
            f"Score: {student['score']} | "
            f"Grade: {student['grade']} | "
            f"Status: {status}"
        )

    print("--------------------------------------")
    print(f"Class Average: {average:.2f}")
    print(f"Highest Score: {highest}")
    print(f"Lowest Score: {lowest}")
    print(f"Students Passed: {passed}")
    print(f"Students Failed: {failed}")

    print("\nStudents Above Class Average:")

    if above_average:
        for student in above_average:
            print(f"{student['name']} - {student['score']}")
    else:
        print("None")

    return {
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "passed": passed,
        "failed": failed,
        "above_average": above_average
    }


# Example data
students = [
    {"name": "Sara", "score": 85},
    {"name": "Ahmed", "score": 42},
    {"name": "Musa", "score": 93},
    {"name": "Hana", "score": 67}
]

generate_report(students)
