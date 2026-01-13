emails=["  Nahidullss@gmail.com  "," NahiD@abulkhairgroup.com","  naHid@InnnovativeSkillsbd.com"]
def process_email(email):
    username,domain=email.split("@")
    return username,domain
locked_pair_tuple=[process_email(email.strip().lower()) for email in emails]
print(locked_pair_tuple)