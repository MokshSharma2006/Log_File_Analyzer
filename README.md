# Log_File_Analyzer

# 📊 Log Analyzer (Python)

A simple yet powerful Python-based Log Analyzer that scans log files to extract useful insights such as error rates, warnings, timestamps, and log-level statistics.
Ideal for system administrators, developers, and students learning log analysis and Python scripting.

## 🚀 Features

✅ Counts total log entries

## 🚨 Detects and counts:

Errors

Warnings

Info

Debugs

Critical / Fatal logs

📌 Extracts timestamps from log lines

🧾 Displays detailed error and warning previews

📈 Calculates error rate automatically

⚡ Fast and lightweight (no external dependencies)

🖥️ Command-line friendly

## 🛠️ Tech Stack

Language: Python 3

Libraries Used:

re (regular expressions)

argparse

datetime

collections

(All libraries are part of Python’s standard library)

## 📂 Project Structure
log-analyzer/
│
├── log_analyzer.py      # Main analyzer script
├── sample.log           # Sample log file (optional)
└── README.md            # Project documentation

▶️ Usage
1️⃣ Clone the Repository
git clone https://github.com/your-username/log-analyzer.git
cd log-analyzer

2️⃣ Run the Analyzer
python3 log_analyzer.py your_log_file.log


If no file is provided, it defaults to:

sample.log

## 🧪 Example Output

============================================================
LOG FILE ANALYSIS REPORT
============================================================
File analyzed: system.log
Analysis time: 2025-01-10 18:20:45

BASIC STATISTICS:
Total Lines     : 1500
Errors          : 12
Warnings        : 25
Info            : 980
Debug           : 450
Critical        : 2

ERRORS FOUND (12):
Line 45: Database connection failed...
Line 132: File not found...

SUMMARY: Error rate: 0.80%
🚨 High number of errors detected!

## 🧠 How It Works

Reads the log file line-by-line

Identifies log levels using keyword matching

Extracts timestamps using regex

Stores errors and warnings with line numbers

Generates a clean, readable analysis report

## 📌 Supported Timestamp Format
YYYY-MM-DD HH:MM:SS


Example:

2025-01-10 14:32:11

## 🧩 Future Improvements (Planned)

📄 Export report to a file (--output)

📊 Graphical visualization (charts)

🔍 Advanced regex-based log parsing

🌐 Web-based dashboard

🧪 Unit tests

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repo, improve features, or submit bug fixes via pull requests.

## 📜 License

This project is licensed under the MIT License

## 👤 Author

Moksh Sharma
Python Developer | Linux & System Tools Enthusiast.
