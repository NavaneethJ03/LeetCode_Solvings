if __name__ == '__main__':
    # Step 1: Input Parsing
    students = []
    n = int(input(""))

    for _ in range(n):
        name = input()
        grade = float(input())
        students.append([name, grade])

    # Step 2: Find the second lowest grade
    grades = sorted(set([student[1] for student in students]))  # Get unique grades and sort them
    second_lowest_grade = grades[1]  # The second lowest grade

    # Step 3: Get students with the second lowest grade
    students_with_second_lowest = [student[0] for student in students if student[1] == second_lowest_grade]

    # Step 4: Sort the names alphabetically
    students_with_second_lowest.sort()

    # Step 5: Print each student's name
    for student in students_with_second_lowest:
        print(student)
