# Quiz Game

questions = {
    "Which function is used to get the length of a list in Python?": "len()",
    "What is 5 + 7?": "12",
    "What is the color of the sky?": "Blue"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question + " ")
    if user_answer.strip().lower() == answer.lower():
        score += 1
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {answer}.")

print(f"Your final score is {score}/{len(questions)}.")
