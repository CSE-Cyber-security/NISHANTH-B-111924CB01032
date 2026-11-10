"""Password strength analysis logic.

This is an educational checker, not a replacement for a password
policy or a modern password-auditing service.
"""

import re

COMMON_PASSWORDS = {
    "password", "password123", "123456", "123456789",
    "qwerty", "qwerty123", "admin", "letmein", "welcome",
    "iloveyou", "abc123",
}


def check_password(password: str) -> dict:
    """Return a score, strength label, and improvement feedback."""
    if not isinstance(password, str):
        raise TypeError("password must be a string")

    score = 0
    feedback = []

    length = len(password)
    if length >= 16:
        score += 35
        feedback.append("Good length: 16 or more characters.")
    elif length >= 12:
        score += 28
        feedback.append("Good length: 12 or more characters.")
    elif length >= 8:
        score += 18
        feedback.append("Increase the length to at least 12 characters.")
    else:
        feedback.append("Too short: use at least 12 characters.")

    checks = [
        (r"[a-z]", 10, "Add lowercase letters."),
        (r"[A-Z]", 10, "Add uppercase letters."),
        (r"\d", 10, "Add numbers."),
        (r"[^A-Za-z0-9]", 15, "Add symbols (such as !, @, or #)."),
    ]

    for pattern, points, suggestion in checks:
        if re.search(pattern, password):
            score += points
        else:
            feedback.append(suggestion)

    lowered = password.lower()
    if lowered in COMMON_PASSWORDS:
        score = min(score, 10)
        feedback.append("This is a commonly used password. Choose a unique one.")

    if re.search(r"(.)\1{2,}", password):
        score -= 10
        feedback.append("Avoid repeating the same character three or more times.")

    if re.search(r"0123|1234|2345|3456|4567|5678|6789|abcd|qwerty", lowered):
        score -= 10
        feedback.append("Avoid predictable keyboard or sequential patterns.")

    score = max(0, min(score, 100))

    if score >= 80:
        strength = "Strong"
    elif score >= 55:
        strength = "Moderate"
    elif score >= 30:
        strength = "Weak"
    else:
        strength = "Very Weak"

    if not feedback:
        feedback.append("Good combination of length and character variety.")

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback,
    }
