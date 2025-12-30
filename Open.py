# Open Credit System Code
print("--- University Grading System (Open Credit) ---")
dept = input("Enter Department (CSE, EEE, BBA, ENG, LAW): ").upper()

gp = 0.0
total_credits = 0.0

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

def input_scores(name,credit):
    print(f"\nEnter marks for {name}")
    ct = float(input("Class Test (20): "))
    mid = float(input("Mid Term (30): "))
    final = float(input("Final Term (50): "))
    score = ct + mid + final
    # print(score)
    return get_gp(score) * credit

if dept == "CSE":
   
    for i in range(50):
        credit = float(input(f"Enter Subject {i+1} Credit: "))
        gp+=input_scores(f"Subject {i+1}",credit)
        total_credits+=credit
        # print(total_credits)
elif dept == "EEE":
    for i in range(50):
        credit = float(input(f"Enter Subject {i+1} Credit: "))
        gp+=input_scores(f"Subject {i+1}",credit)
        total_credits+=credit
elif dept == "BBA":
    for i in range(41):
        credit = float(input(f"Enter Subject {i+1} Credit: "))
        gp+=input_scores(f"Subject {i+1}",credit)
        total_credits+=credit
elif dept == "ENG":
     for i in range(40):
        credit = float(input(f"Enter Subject {i+1} Credit: "))
        gp+=input_scores(f"Subject {i+1}",credit)
        total_credits+=credit
elif dept == "LAW":
    for i in range(45):
        credit = float(input(f"Enter Subject {i+1} Credit: "))
        gp+=input_scores(f"Subject {i+1}",credit)
        total_credits+=credit
else:
    print("Invalid Department")


# cse

# CGPA = Σ(Grade Point * Credit) / Σ(Total Credits)
if total_credits > 0:
    cgpa = gp / total_credits
    print(f"\nFinal weighted CGPA: {cgpa:.2f}")