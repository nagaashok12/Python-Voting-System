# 🗳️ Python Voting System

A simple command-line voting system built using pure Python. Users can cast votes, and admins can view results. Votes are stored persistently using JSON.

---

## ✅ Features

- Add default candidates (Alice, Bob, Charlie)
- One-person one-vote (by voter ID)
- Persistent vote storage in `votes.json`
- Admin-only result viewing
- Easy-to-understand CLI interface

---

## 🛠️ Technologies Used

- Python 3
- JSON for data storage
- Command-line interface (CLI)

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/nagaashok12/python-voting-system.git
   cd python-voting-system
   ```

2. Run the program:
   ```bash
   python voting_system.py
   ```

3. Admin Password (for results): `admin123`

---

## 📦 File Structure

```
python-voting-system/
├── voting_system.py
├── votes.json           # Created after first vote
└── README.md
```

---

## 💡 Future Improvements

- GUI version with Tkinter
- User authentication
- Real-time dashboard
