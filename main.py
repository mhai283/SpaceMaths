from leaderboard import show_all_leaderboards, get_leaderboard
from game_logic import play_game

# Get player's name or provide options to view leaderboards or exit
def get_player_name():
    return input("Type 'leaderboard' to view the mission leaderboard, or 'exit' to quit.\nEnter your astronaut name: ")

# Choose difficulty level (mission difficulty)
def get_difficulty():
    while True:
        choice = input("\nChoose your mission difficulty: Easy | Medium | Hard: ").lower()
        if choice in ["easy", "medium", "hard"]:
            return choice
        print("\nPlease choose from: Easy, Medium, Hard")

# Get mission duration
def get_countdown():
    while True:
        try:
            seconds = int(input("\nHow many seconds for your mission? 10 | 20 | 30: "))
            if seconds in [10, 20, 30]:
                return seconds
            else:
                print("Please choose 10, 20, or 30 seconds.")
        except:
            print("Please enter a valid number.")

# Main loop — runs until the astronaut says 'exit'
def main():
    print("\n🪐 Welcome to the Space Maths Mission! 🚀\n")

    while True:
        name = get_player_name().strip()

        if name == "exit":
            print("Thanks for playing astronaut! Goodbye 👋\n")
            break
        elif name == "leaderboard":
            show_all_leaderboards()
            continue

        difficulty = get_difficulty()
        duration = get_countdown()

        leaderboard = get_leaderboard(duration)  # Get the appropriate leaderboard for the mission duration
        leaderboard = play_game(name, difficulty, duration, leaderboard)

if __name__ == "__main__":
    main()
