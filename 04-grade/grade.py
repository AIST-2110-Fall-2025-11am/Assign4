# Prompt the user to enter the total number of questinos
number_of_questions = int(input("Total number of questions: "))


# Prompt the user to enter the number of correct answers
number_of_correct_answers = int(input("How many did you get right? "))


# Calculate the score
score = (number_of_correct_answers / number_of_questions) * 100


# Use the score to determine the letter grade



# Print the grade in the format:
#   "CORRECT out of TOTAL is SCORE% (LETTER)""
if score >= 90:
    print(f"{number_of_correct_answers} out of {number_of_questions} is {score}% (A)")
elif score >= 80:
    print(f"{number_of_correct_answers} out of {number_of_questions} is {score}% (B)")
elif score >= 70:
    print(f"{number_of_correct_answers} out of {number_of_questions} is {score}% (C)")
elif score >= 60:
    print(f"{number_of_correct_answers} out of {number_of_questions} is {score}% (D)")
else:
    print(f"{number_of_correct_answers} out of {number_of_questions} is {score}% (F)")
