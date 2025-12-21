# -----------------------------------------
# Personalized Study Assistant Agent
# Demonstrates Agent Learning & Personalization
# -----------------------------------------

# Memory: what the agent learns about the user
user_profile = {
    "level": "unknown",              # beginner / intermediate
    "preferred_style": "unknown",    # simple / examples
    "topic_history": []
}

# Function to generate response based on memory
def generate_response(topic):
    user_profile["topic_history"].append(topic)

    level = user_profile["level"]
    style = user_profile["preferred_style"]

    if level == "beginner" and style == "examples":
        return f"Let's learn {topic} with a simple real-life example."
    elif level == "beginner":
        return f"I'll explain {topic} in a very simple way."
    elif level == "intermediate":
        return f"Here is a structured explanation of {topic} with key points."
    else:
        return f"This is a basic explanation of {topic}."

# Function to learn from user feedback
def learn_from_feedback(feedback):
    feedback = feedback.lower()

    if "too hard" in feedback or "complex" in feedback:
        user_profile["level"] = "beginner"
        user_profile["preferred_style"] = "examples"

    elif "easy" in feedback or "understand" in feedback:
        user_profile["level"] = "intermediate"

    elif "example" in feedback:
        user_profile["preferred_style"] = "examples"

# Main interaction loop
def run_agent():
    print("📘 Personalized Study Assistant")
    print("Type 'exit' to stop\n")

    while True:
        topic = input("Student: What topic do you want help with? ")

        if topic.lower() == "exit":
            print("\nAgent: Session ended. Goodbye!")
            break

        response = generate_response(topic)
        print(f"\nAgent: {response}")

        feedback = input("Student feedback (e.g., too hard / easy / need example): ")
        learn_from_feedback(feedback)

        print("\n[Agent Memory Updated]")
        print(user_profile)
        print("-" * 40)

# Run the agent
if __name__ == "__main__":
    run_agent()
