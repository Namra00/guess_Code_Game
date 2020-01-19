import random


def get_input():
    x = list(input("Guess your 3 digit number: "))
    return x


def gen_random():
    # digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    digit = [str(num) for num in range(10)]
    digits = digit.copy()
    random.shuffle(digits)
    return digits[:3]


def gen_clues(code, user_guess):
    if user_guess == code:
        return 'CODE CRACKED!'

    clues = []

    for index, num in enumerate(user_guess):
        if code[index] == num:
            clues.append("match")
        elif num in guess:
            clues.append("close")

    if not clues:
        return ["Nope"]
    else:
        return clues


print("Welcome Code Breaker!")
secret_code = gen_random()
clue_report = []

while clue_report != "CODE CRACKED!":
    guess = get_input()
    clue_report = gen_clues(guess, secret_code)
    print('Here is the result of your guess: ')
    for clue in clue_report:
        print(clue)

