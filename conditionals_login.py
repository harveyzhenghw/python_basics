# 📝 Step-by-Step Instructions

# Define the correct email and password
# (think of them like a lock code that only the program knows).

# Ask the user to type their email
# → save their answer in a variable.

# Ask the user to type their password
# → save their answer in another variable.

# Check if both the email and password are correct

# Compare the user’s answers with the saved lock code.

# If both are correct
# → show a success message like "Logged in".

# If either one is wrong
# → show an error message like "Incorrect login or password".

# End the program.


# START

# SET correct_email TO "some_email" 
# SET correct_password TO "qwerty"

# ASK user for email → store in input_email 
# ASK user for password → store in input_password

# IF input_email = correct_email AND input_password = correct_password THEN 
#     DISPLAY "Logged in"
#     // Here we would show secret content
# ELSE
#     DISPLAY "Incorrect login or password"
# END IF

# STOP

correct_email = "harvey@gmail.com"
correct_password = "qwerty"
input_email = input("input your email: ")
input_password = input("input your password: ")
if input_email == correct_email and input_password == correct_password:
    print("logged in")
else:
    print("incorrect username or passcode")