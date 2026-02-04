import random

def guess_the_number():
    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Введите число: "))
        attempts += 1

        if guess < number:
            print("Слишком низко!")
        elif guess > number:
            print("Слишком высоко!")
        else:
            print("Поздравляю! Вы угадали число с", attempts, "попыток.")
            break

guess_the_number()
