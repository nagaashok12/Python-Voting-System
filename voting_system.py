# Import necessary modules
import json  # For reading/writing vote data
import os    # For checking if the vote file exists

# File to store voting data
VOTE_FILE = "votes.json"

# Load votes and voter history from JSON file
def load_data():
    # Check if the data file exists
    if os.path.exists(VOTE_FILE):
        with open(VOTE_FILE, "r") as file:
            data = json.load(file)
        # Return votes dictionary and a set of voters
        return data.get("votes", {}), set(data.get("voters", []))
    else:
        # If file doesn't exist, return empty structures
        return {}, set()

# Save current voting data and voter history to the JSON file
def save_data(votes, voters):
    with open(VOTE_FILE, "w") as file:
        json.dump({"votes": votes, "voters": list(voters)}, file)

# Add a new candidate to the election
def add_candidate(votes, name):
    if name not in votes:
        votes[name] = 0  # Initialize vote count to 0

# Cast a vote for a candidate
def vote(voter_id, candidate, votes, voters):
    # Prevent duplicate voting by checking voter ID
    if voter_id in voters:
        print("❌ You have already voted.")
        return
    # Check if the candidate exists
    if candidate in votes:
        votes[candidate] += 1
        voters.add(voter_id)  # Record that this voter has voted
        print("✅ Vote cast successfully!")
    else:
        print("❌ Invalid candidate.")

# Display the vote count and declare the winner
def show_results(votes):
    print("\n📊 Voting Results:")
    for candidate, count in votes.items():
        print(f"{candidate}: {count} votes")
    if votes:
        winner = max(votes, key=votes.get)
        print(f"\n🏆 Winner: {winner}")

# Main program logic
def main():
    print("🎉 Welcome to Python Voting System 🎉")

    # Load previous voting data (if any)
    votes, voters = load_data()

    # Add default candidates if this is the first run
    if not votes:
        add_candidate(votes, "Alice")
        add_candidate(votes, "Bob")
        add_candidate(votes, "Charlie")

    # Show main menu in a loop
    while True:
        print("\n1. Vote\n2. Show Results (admin)\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Voter ID is used to prevent multiple votes
            voter_id = input("Enter your Voter ID: ").strip()
            print("Candidates:", list(votes.keys()))
            selected = input("Enter candidate name: ").strip()
            vote(voter_id, selected, votes, voters)
            save_data(votes, voters)  # Save after voting

        elif choice == "2":
            # Only admin can see results
            password = input("Enter admin password: ")
            if password == "admin123":
                show_results(votes)
            else:
                print("❌ Invalid password.")

        elif choice == "3":
            # Exit the application
            save_data(votes, voters)
            print("👋 Exiting. Thank you!")
            break

        else:
            print("❌ Invalid input!")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
