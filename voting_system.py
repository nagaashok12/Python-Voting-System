import json
import os

VOTE_FILE = "votes.json"

def load_data():
    if os.path.exists(VOTE_FILE):
        with open(VOTE_FILE, "r") as file:
            data = json.load(file)
        return data.get("votes", {}), set(data.get("voters", []))
    else:
        return {}, set()

def save_data(votes, voters):
    with open(VOTE_FILE, "w") as file:
        json.dump({"votes": votes, "voters": list(voters)}, file)

def add_candidate(votes, name):
    if name not in votes:
        votes[name] = 0

def vote(voter_id, candidate, votes, voters):
    if voter_id in voters:
        print("❌ You have already voted.")
        return
    if candidate in votes:
        votes[candidate] += 1
        voters.add(voter_id)
        print("✅ Vote cast successfully!")
    else:
        print("❌ Invalid candidate.")

def show_results(votes):
    print("\n📊 Voting Results:")
    for candidate, count in votes.items():
        print(f"{candidate}: {count} votes")
    if votes:
        winner = max(votes, key=votes.get)
        print(f"\n🏆 Winner: {winner}")

def main():
    print("🎉 Welcome to Python Voting System 🎉")

    votes, voters = load_data()

    if not votes:
        add_candidate(votes, "Alice")
        add_candidate(votes, "Bob")
        add_candidate(votes, "Charlie")

    while True:
        print("\n1. Vote\n2. Show Results (admin)\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            voter_id = input("Enter your Voter ID: ").strip()
            print("Candidates:", list(votes.keys()))
            selected = input("Enter candidate name: ").strip()
            vote(voter_id, selected, votes, voters)
            save_data(votes, voters)

        elif choice == "2":
            password = input("Enter admin password: ")
            if password == "admin123":
                show_results(votes)
            else:
                print("❌ Invalid password.")

        elif choice == "3":
            save_data(votes, voters)
            print("👋 Exiting. Thank you!")
            break

        else:
            print("❌ Invalid input!")

if __name__ == "__main__":
    main()
