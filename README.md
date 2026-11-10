# Password Strength Checker

A beginner-friendly Python project that checks password strength locally in the terminal.

## Features

- Hides password input while typing (`getpass`).
- Checks password length.
- Checks for lowercase letters, uppercase letters, numbers, and symbols.
- Warns about common passwords, repeated characters, and predictable sequences.
- Displays a score from 0 to 100, a strength label, and improvement tips.
- Does not save, print, or send the password anywhere.

## Requirements

- Python 3.8 or later
- No third-party packages are required.

## Folder structure

```text
password_strength_checker/
├── main.py
├── password_checker.py
├── README.md
├── .gitignore
└── tests/
    └── test_password_checker.py
```

## How to run

1. Download or clone this project.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python main.py
   ```

4. Type a password when prompted. The characters will not appear on screen.
5. Read the strength result and suggestions.

On some systems, use `python3 main.py` instead of `python main.py`.

## Run the tests

From the project folder, run:

```bash
python -m unittest discover -s tests -v
```

## Example output

```text
================================================
           PASSWORD STRENGTH CHECKER
================================================
Enter a password (input is hidden):

Strength: Strong (100/100)

Analysis:
- Good length: 16 or more characters.

Tip: Use a long, unique passphrase. Never reuse passwords.
Your password is checked locally and is not saved.
```

The exact score and feedback depend on the password entered.

## How it works

1. The program receives the password using Python's `getpass` module.
2. The checker evaluates length and character variety.
3. It applies penalties for common passwords and predictable patterns.
4. It calculates a score between 0 and 100.
5. It converts the score into a strength category and prints suggestions.

## Score categories

| Score | Result |
|---:|---|
| 0–29 | Very Weak |
| 30–54 | Weak |
| 55–79 | Moderate |
| 80–100 | Strong |

## Push the project to GitHub

Create a new GitHub repository, then run these commands inside this folder:

```bash
git init
git add .
git commit -m "Add password strength checker"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the remote URL with your own repository URL.

## Important note

This is a learning project using simple rules. A password score is only an estimate and cannot guarantee that a password is secure. For real applications, use a well-reviewed password-strength library and secure password storage such as a suitable password hashing algorithm. Never store passwords in plain text.
