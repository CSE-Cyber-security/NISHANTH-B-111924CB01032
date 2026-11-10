"""Run the Password Strength Checker from the terminal."""

from getpass import getpass
from password_checker import check_password


def main():
    print("=" * 48)
    print("           PASSWORD STRENGTH CHECKER")
    print("=" * 48)
    password = getpass("Enter a password (input is hidden): ")

    result = check_password(password)

    print(f"\nStrength: {result['strength']} ({result['score']}/100)")
    print("\nAnalysis:")
    for item in result["feedback"]:
        print(f"- {item}")

    print("\nTip: Use a long, unique passphrase. Never reuse passwords.")
    print("Your password is checked locally and is not saved.")


if __name__ == "__main__":
    main()
