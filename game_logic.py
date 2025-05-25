import random
import time

# Countdown
def countdown_start():
    print("\nPrepare for liftoff. Starting in...\n")
    time.sleep(1.5)
    print("3\n")
    time.sleep(1)
    print("2\n")
    time.sleep(1)
    print("1\n")
    time.sleep(1)
    print("Liftoff! 🚀\n")

# Space-themed questions
def generate_question(difficulty):
    if difficulty == "easy":
        a = random.randint(1, 9)
        b = random.randint(1, 9)
    elif difficulty == "medium":
        a = random.randint(10, 99)
        b = random.randint(1, 10)
    else:
        a = random.randint(10, 99)
        b = random.randint(1, 99)

    operator = random.choice(["+", "-", "*"])

    # No negative results for subtraction
    if operator == "-" and b > a:
        a, b = b, a

    if operator == "+":
        answer = a + b
    elif operator == "-":
        answer = a - b
    else:
        answer = a * b

    question = f"{a} {operator} {b}"
    return question, answer

# Main game loop: space mission to solve math problems
def play_game(name, difficulty, duration, leaderboard):
    score = 0
    correct_count = 0
    wrong_count = 0
    streak = 0
    highest_streak = 0
    total_attempts = 0  # total number of attempts (correct + wrong)

    countdown_start()
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        question, correct_answer = generate_question(difficulty)
        print("\nMission Control: What is:", question)

        question_time = time.time()
        answer = input("Astronaut's answer: ")

        if time.time() >= end_time:
            break

        try:
            total_attempts += 1  # count each attempt
            if int(answer) == correct_answer:
                time_taken = time.time() - question_time
                correct_count += 1
                streak += 1
                highest_streak = max(highest_streak, streak)
                if time_taken <= 2:
                    score += 2
                    print("✅ Correct. (+2 points) Well done, astronaut!")
                else:
                    score += 1
                    print("✅ Correct. (+1 point)")
                if streak >= 2:
                    print(f"🔥 Streak! {streak} correct answers in a row!")
            else:
                wrong_count += 1
                streak = 0
                print(f"❌ Incorrect. The correct answer was: {correct_answer}. Mission failure!")

        except ValueError:
            wrong_count += 1
            streak = 0
            print(f"❌ Invalid input. The correct answer was: {correct_answer}. Mission failure!")

    print("\nTime's up!")
    print(f"\nYour score: {score}")
    print(f"✅ Correct answers: {correct_count}")
    print(f"❌ Incorrect answers: {wrong_count}")
    print(f"🔥 Highest streak: {highest_streak}")

    if total_attempts > 0:
        accuracy = (correct_count / total_attempts) * 100
        print(f"📊 Mission accuracy: {accuracy:.2f}%\n")
    else:
        print("📊 Mission accuracy: N/A (No valid attempts)\n")

    # Add score to leaderboard or update existing one
    if name in leaderboard:
        leaderboard[name] += score
    else:
        leaderboard[name] = score

    return leaderboard
