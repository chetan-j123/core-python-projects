def calculate_average(marks_list):
    print(marks_list)
    marks = list(marks_list)
    total_marks = 0
    for i in range(0, len(marks), 1):
        total_marks = total_marks + marks[i]
    average_marks = float(total_marks / len(marks))
    return average_marks


def determine_grade(subject_names, mark):
    for i in range(0, len(subject_names), 1):
        if mark > 90:
            grade = "A+"
        elif 80 < mark <= 90:
            grade = "A"
        elif 70 < mark <= 80:
            grade = "B+"
        elif 60 < mark <= 70:
            grade = "B"
        elif 50 < mark <= 60:
            grade = "C+"
        elif 45 < mark <= 50:
            grade = "C"
        elif 36 < mark <= 45:
            grade = "D"
        else:
            grade = "F"
        return grade


def determine_final_grade(average):
    if average > 90:
        final_grade = "A+"
    elif 80 < average <= 90:
        final_grade = "A"
    elif 70 < average <= 80:
        final_grade = "B+"
    elif 60 < average <= 70:
        final_grade = "B"
    elif 50 < average <= 60:
        final_grade = "C+"
    elif 45 < average <= 50:
        final_grade = "C"
    elif 36 < average <= 45:
        final_grade = "D"
    else:
        final_grade = "F"
    return final_grade


student_subjects = {}

print("\t🧑‍🎓 Student Report Card System 📑")
print("👋 Welcome! Enter student details and marks to generate a report card.")

student_name = str(input("📝 Enter the name of the student = "))
student_class = str(input("🏫 Enter the class of the student = "))
exam_name = str(input("📚 Enter the exam name = "))
student_section = str(input("🏷️ Enter the section of the student = "))
roll_number = str(input("🎫 Enter the roll number of the student = "))

print("✅ You have entered all necessary student details.")

subject_count = int(input(f"📊 Now enter the total number of subjects for {student_name} (Roll No: {roll_number}) = "))

for i in range(0, subject_count, 1):
    subject_name = str(input("📘 Enter the subject name = "))
    subject_marks = float(input(f"✍️ Enter the marks for {subject_name} = "))
    student_subjects.update({subject_name: subject_marks})

print("📌 You have entered marks for", subject_count, "subjects.")

show_marks = str(input("📖 Do you want to see the list of marks? (yes/no) = "))

if show_marks == "yes":
    print("📋 Marks Entered:", student_subjects)
    calc_avg = str(input("⚖️ Do you want to calculate the average of the marks? (yes/no) = "))
    if calc_avg == "yes":
        values = student_subjects.values()
        print("📊 The average marks are", calculate_average(values))
    else:
        show_subject_grades = str(input("🏅 Do you want to get the grade of each subject? (yes/no) = "))
        if show_subject_grades == "yes":
            keys = list(student_subjects.keys())
            values = list(student_subjects.values())
            avg_marks = calculate_average(values)
            for i in range(0, len(values)):
                print("✅ Your grade in", keys[i], "is", determine_grade(keys[i], values[i]))
            print("🌟 The final overall grade is =", determine_final_grade(avg_marks))

else:
    calc_avg = str(input("⚖️ Do you want to calculate the average of the marks? (yes/no) = "))
    if calc_avg == "yes":
        values = student_subjects.values()
        avg = calculate_average(values)
        print("📊 The average marks are", avg)
        get_final_grade = str(input("🏆 Do you want to get the overall grade? (yes/no) = "))
        if get_final_grade == "yes":
            keys = list(student_subjects.keys())
            values = list(student_subjects.values())
            determine_grade(keys, values, avg)
    else:
        show_subject_grades = str(input("🏅 Do you want to get the grade of each subject? (yes/no) = "))
        if show_subject_grades == "yes":
            keys = list(student_subjects.keys())
            values = list(student_subjects.values())
            determine_grade(keys, values)

save_report = str(input("💾 Do you want to save this student report card in a file? (yes/no) = "))
if save_report == "yes":
    file = open("reportcard.txt", "a")
    file.write("\n" + "                   Report Card of " + str(student_name))
    file.write("\n" + "-" * 128)
    file.write("\n Name = " + student_name)
    file.write("\n Class = " + student_class)
    file.write("\n Exam Name = " + exam_name)
    file.write("\n Roll No = " + str(roll_number))
    file.write("\n Section = " + student_section)
    file.write("\n Subjects = " + str(student_subjects))
    values = student_subjects.values()
    vals = calculate_average(values)
    file.write("\n Average = " + str(vals))
    keys = list(student_subjects.keys())
    values = list(student_subjects.values())
    val = calculate_average(values)
    file.write("\n Grades in subjects are as follows:")
    for i in range(0, len(values)):
        file.write("\n Grade in " + str(keys[i]) + " is = " + str(determine_grade(keys[i], values[i])))
    file.write("\n Final Overall Grade = " + str(determine_final_grade(val)))
    file.write("\n" + "-" * 128)
    file.close()

view_file = str(input("📂 Do you want to see the saved file? (yes/no) = "))
if view_file == "yes":
    file = open("reportcard.txt", "r")
    print("📄 Saved Report:\n")
    print(file.read())
    file.close()
else:
    print("⚠️ Please enter a valid response.")

