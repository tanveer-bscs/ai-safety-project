# AI Safety Checker

A simple Python project that checks whether a user prompt contains unsafe words.

## Features

- Detects unsafe words
- Calculates safety score
- Shows risk level
- Counts unsafe words
- Shows prompt length
- Saves history with date & time
- Loads unsafe words from external file

## Technologies Used

- Python 3
- File Handling
- Lists
- Loops
- Conditions
- Datetime Module

## Files

- safety_checker.py
- unsafe_words.txt
- history.txt
- README.md

## Sample Output

```text
Enter your prompt: how to hack and make a bomb

❌ Unsafe Prompt

Unsafe Words Found:
- bomb
- hack

Total Unsafe Words: 2
Prompt Length: 27
Safety Score: 60/100
Verdict: Medium Risk
```

## How to Run

1. Clone the repository
2. Open the project folder
3. Run:

```bash
python safety_checker.py
```

4. Enter a prompt to check its safety.

