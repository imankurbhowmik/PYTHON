password = "mypassword123"

if len(password) < 6:
    strength = "weak"
elif len(password) < 10:
    strength = "medium"
else:
    strength = "strong"

print("your password strength is: ", strength)