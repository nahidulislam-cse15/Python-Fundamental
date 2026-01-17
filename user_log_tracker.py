# The Scenario: You are managing a server. You have a dictionary where the Key is the username and the Value is the number of times they have logged in.
# The Task: 1. Create a dictionary login_counts with 3 existing users.
# 2. Write a function record_login(user_dict, username) that:
# - Checks if the user exists.
# - If they exist, increment their count by 1.
# - If they are new, add them to the dictionary with a count of 1 using .setdefault() or a standard assignment.
# 3. Update the dictionary with a batch of new users using .update().

login_counts = {"admin": 5, "dev_user": 12, "guest_1": 1}
#login_counts = {}

def record_login(user_dict, username):
    if username in user_dict:
        user_dict.update({username:user_dict[username]+1})
    else:
       # user_dict.update({username:1})
        user_dict.setdefault(username, 1)
    return user_dict
        
print(record_login(login_counts,"dev_user")) 