if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # Get the marks of the queried student and calculate the average
    query_scores = student_marks[query_name]
    average = sum(query_scores) / len(query_scores)

    # Print the average rounded to 2 decimal places
    print(f"{average:.2f}")
