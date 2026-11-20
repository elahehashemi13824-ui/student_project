from student import average_grade, max_grade, min_grade, get_status

student_name = input("Enter student name: ")

grades_input = input("Enter student grades (separated by commas): ")

try:
    grades = [float(grade.strip()) for grade in grades_input.split(",")]

    if not grades:
        print("No grades entered.")

    elif any(grade < 0 or grade > 20 for grade in grades):
        print("Grades must be between 0 and 20.")

    else:
        avg = average_grade(grades)
        maximum = max_grade(grades)
        minimum = min_grade(grades)
        status = get_status(avg)

        print("\n========== Student Information ==========")
        print(f"Student: {student_name}")
        print(f"Avg = {avg}")
        print(f"Max = {maximum}")
        print(f"Min = {minimum}")
        print(f"Status = {status}")
        print("=========================================")

except ValueError:
    print("Please enter valid numbers for grades.")
