# Prompt the user for input and store it as an integer named 'score'
score = int(input("Score: "))

# Check if the score is between 90 and 100 (inclusive)
if score >= 90 and score <= 100:
    # If the score is in the 'A' range, print this message
    print("Grade: A")
# If the score is not in the 'A' range, check if it's between 80 and 89
elif score >= 80 and score < 90:
    # If the score is in the 'B' range, print this message
    print("Grade: B")
# If the score is not in the 'B' range, check if it's between 70 and 79
elif score >= 70 and score < 80:
    # If the score is in the 'C' range, print this message
    print("Grade: C")
# If the score is not in the 'C' range, check if it's between 60 and 69
elif score >= 60 and score < 70:
    # If the score is in the 'D' range, print this message
    print("Grade: D")
# If the score is not in any of the previous ranges, it's less than 60
else:
    # In this case, the score is in the 'F' range, so print this message
    print("Grade: F")


# alternate way of solving above program
# Prompt the user for input and store it as an integer named 'score'
score = int(input("Score: "))

# Check if the score is between 90 and 100 (inclusive)
if 90 <= score <= 100:
    # If the score is in the 'A' range, print this message
    print("Grade: A")
# If the score is not in the 'A' range, check if it's between 80 and 89
elif 80 <= score < 90:
    # If the score is in the 'B' range, print this message
    print("Grade: B")
# If the score is not in the 'B' range, check if it's between 70 and 79
elif 70 <= score < 80:
    # If the score is in the 'C' range, print this message
    print("Grade: C")
# If the score is not in the 'C' range, check if it's between 60 and 69
elif 60 <= score < 70:
    # If the score is in the 'D' range, print this message
    print("Grade: D")
# If the score is not in any of the previous ranges, it's less than 60
else:
    # In this case, the score is in the 'F' range, so print this message
    print("Grade: F")


# another way of solving above program
# Prompt the user for input and store it as an integer named 'score'
score = int(input("Score: "))

# Check if the score is greater than or equal to 90
if score >= 90:
    # If the score is 90 or above, print this message
    print("Grade: A")
# If the score is not in the 'A' range, check if it's greater than or equal to 80
elif score >= 80:
    # If the score is in the 'B' range (80 or above), print this message
    print("Grade: B")
# If the score is not in the 'B' range, check if it's greater than or equal to 70
elif score >= 70:
    # If the score is in the 'C' range (70 or above), print this message
    print("Grade: C")
# If the score is not in the 'C' range, check if it's greater than or equal to 60
elif score >= 60:
    # If the score is in the 'D' range (60 or above), print this message
    print("Grade: D")
# If the score is not in any of the previous ranges, it's less than 60
else:
    # In this case, the score is in the 'F' range, so print this message
    print("Grade: F")
