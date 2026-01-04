all_grades = [
    [60, 92, 70],  # Student 0 
    [50, 80, 77],  # Student 1 
    [45, 100, 95]  # Student 2
]

def check_failing(grades_grid):
    for i, student_scores in enumerate(grades_grid):
        for score in student_scores:
            if score < 50:
                print(f"Student {i} failed a subject!")
                break 

# Run the function
check_failing(all_grades)