# Initialise separate leaderboards for each duration (10s, 20s, 30s)
leaderboard_10s = {}
leaderboard_20s = {}
leaderboard_30s = {}

# Show the leaderboard for all durations
def show_all_leaderboards():
    print("\n======= SPACE MISSION LEADERBOARDS =======")
    
    # Show leaderboard for each duration
    for duration, leaderboard in [(10, leaderboard_10s), (20, leaderboard_20s), (30, leaderboard_30s)]:
        print(f"\n------- Mission Duration: {duration} seconds -------")
        if not leaderboard:
            print("No crew members have completed this mission yet.")
        else:
            for name in leaderboard:
                print(f"{name}: {leaderboard[name]} points")
    print("==========================================\n")

# Get the correct leaderboard based on mission duration
def get_leaderboard(duration):
    if duration == 10:
        return leaderboard_10s
    elif duration == 20:
        return leaderboard_20s
    elif duration == 30:
        return leaderboard_30s
    return {}
