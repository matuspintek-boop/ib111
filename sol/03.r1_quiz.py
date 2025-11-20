def mark_points(answers, solution):
    scored_points = 0
    for i in range(len(solution)):
        correct_answer, points = answers[i]
        if solution[i] == correct_answer:
            scored_points += points
    return scored_points
