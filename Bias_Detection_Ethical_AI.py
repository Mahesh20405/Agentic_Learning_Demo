import re
from collections import defaultdict

# -------------------- MEMORY --------------------
bias_memory = {
    "detected_patterns": defaultdict(int),
    "bias_score": 0,
    "categories_found": set()
}

# -------------------- RULES --------------------
BIAS_PATTERNS = {
    "gender": [
        (r'\b(he|his|him)\b.*\b(engineer|doctor|leader|manager)\b',
         "Assuming profession based on gender"),
        (r'\b(she|her)\b.*\b(nurse|assistant|teacher)\b',
         "Gender-based role stereotype")
    ],
    "race": [
        (r'\b(asians?)\b.*\b(good at math|smart)\b',
         "Racial generalization"),
        (r'\b(blacks?|africans?)\b.*\b(athletic|musical)\b',
         "Racial stereotype")
    ],
    "age": [
        (r'\b(old|elderly)\b.*\b(slow|forgetful)\b',
         "Age-based assumption"),
        (r'\b(young|gen z)\b.*\b(lazy|inexperienced)\b',
         "Age stereotype")
    ],
    "socioeconomic": [
        (r'\b(poor)\b.*\b(lazy|uneducated)\b',
         "Economic bias"),
        (r'\b(rich|wealthy)\b.*\b(successful|deserving)\b',
         "Privilege assumption")
    ]
}

# -------------------- CORE FUNCTIONS --------------------
def detect_bias(text):
    findings = []
    text = text.lower()

    for category, patterns in BIAS_PATTERNS.items():
        for pattern, description in patterns:
            if re.search(pattern, text):
                findings.append((category, description))
                bias_memory["detected_patterns"][category] += 1
                bias_memory["categories_found"].add(category)

    return findings


def calculate_bias_score():
    return min(sum(bias_memory["detected_patterns"].values()) * 10, 100)


def suggest_fix(category):
    fixes = {
        "gender": "Use gender-neutral language and avoid role assumptions.",
        "race": "Avoid linking abilities to race.",
        "age": "Describe individuals without age assumptions.",
        "socioeconomic": "Avoid judging character by economic status."
    }
    return fixes.get(category, "Use neutral, inclusive language.")


def show_report():
    print("\n========== FINAL REPORT ==========")
    print(f"Bias Score: {bias_memory['bias_score']}/100")
    print("Detected Categories:")
    for c in bias_memory["categories_found"]:
        print(f" - {c.capitalize()}")
    print("=================================")

# -------------------- MAIN LOOP --------------------
def run_demo():
    print("\nAI BIAS DETECTION – SIMPLE DEMO")
    print("Type a sentence, 'report', or 'exit'\n")

    while True:
        text = input("Input: ").strip()

        if text.lower() == "exit":
            show_report()
            print("\nDemo ended.")
            break

        if text.lower() == "report":
            show_report()
            continue

        findings = detect_bias(text)

        if not findings:
            print("✔ No bias detected.\n")
            continue

        print("\n⚠ Potential Bias Found:")
        for i, (cat, desc) in enumerate(findings, 1):
            print(f"{i}. [{cat.upper()}] {desc}")
            print(f"   Suggestion: {suggest_fix(cat)}")

        bias_memory["bias_score"] = calculate_bias_score()
        print(f"\nCurrent Bias Score: {bias_memory['bias_score']}/100\n")


if __name__ == "__main__":
    run_demo()
