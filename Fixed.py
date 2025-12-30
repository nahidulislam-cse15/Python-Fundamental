# Fixed Credit System Code
print("--- University Grading System (Fixed Credit) ---")
dept = input("Enter Department (CSE, EEE, BBA, ENG, LAW): ").upper()

# Variables to store Grade Points for each subject
gp = 0.0

def get_gp(score):
    if score >= 80: return 4.00
    elif score >= 75: return 3.75
    elif score >= 70: return 3.50
    elif score >= 65: return 3.25
    elif score >= 60: return 3.00
    elif score >= 55: return 2.75
    elif score >= 50: return 2.50
    elif score >= 45: return 2.25
    elif score >= 40: return 2.00
    else: return 0.0

def input_scores(subject):
    print(f"\nEnter marks for {subject}:")
    ct = float(input("Class Test (out of 20): "))
    mid = float(input("Mid Term (out of 30): "))
    final = float(input("Final Term (out of 50): "))
    total = ct + mid + final
    return get_gp(total)

if dept == "CSE": 
    for i in range(50):
        gp+=input_scores(f"Subject {i+1}")
elif dept == "EEE":
    for i in range(50):
        gp+=input_scores(f"Subject {i+1}")
elif dept == "BBA":
    for i in range(50):
        gp+=input_scores(f"Subject {i+1}")
elif dept == "ENG":
     for i in range(50):
        gp+=input_scores(f"Subject {i+1}")
elif dept == "LAW":
    for i in range(50):
        gp+=input_scores(f"Subject {i+1}")
else:
    print("Invalid Department")

# Calculate CGPA (Fixed: Total GP / Number of Subjects)
cgpa = (gp) / 50
print(f"\nYour Estimated CGPA: {cgpa:.2f}")