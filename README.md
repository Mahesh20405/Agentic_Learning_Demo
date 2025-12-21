# 📘 Personalized Study Assistant Agent

A simple demonstration of an AI agent that learns from user interactions and personalizes responses based on accumulated knowledge about the user's preferences and learning level.

## 🎯 Purpose

This project demonstrates key concepts in agent-based systems:
- **Memory & State Management**: The agent maintains a profile of user preferences
- **Adaptive Learning**: Adjusts teaching style based on feedback
- **Personalization**: Tailors responses to individual learning needs

## 🚀 How to Run

### Prerequisites
- Python 3.6 or higher installed on your system

### Steps

1. **Save the code** to a file named `study_assistant.py`

2. **Open a terminal/command prompt** and navigate to the directory containing the file

3. **Run the program**:
   ```bash
   python study_assistant.py
   ```

4. **Interact with the agent**:
   - Enter topics you want to learn about
   - Provide feedback on the explanations
   - Watch as the agent adapts to your preferences
   - Type `exit` when done

## 💡 How It Works

### 1. User Profile (Agent Memory)
The agent maintains a profile with three key attributes:

```python
user_profile = {
    "level": "unknown",           # Tracks: beginner/intermediate
    "preferred_style": "unknown", # Tracks: simple/examples
    "topic_history": []           # Records all topics discussed
}
```

### 2. Response Generation
Based on the current user profile, the agent generates appropriate responses:

- **Beginner + Examples**: Uses real-life examples
- **Beginner**: Uses simple explanations
- **Intermediate**: Provides structured explanations with key points
- **Unknown**: Gives basic explanations

### 3. Learning from Feedback
The agent analyzes user feedback to update its understanding:

| Feedback Contains | Agent Updates |
|------------------|---------------|
| "too hard", "complex" | Sets level to "beginner", style to "examples" |
| "easy", "understand" | Sets level to "intermediate" |
| "example" | Sets style to "examples" |

### 4. Adaptation Loop
With each interaction, the agent:
1. Records the topic in history
2. Generates a response based on current profile
3. Receives feedback
4. Updates its understanding of the user
5. Uses this knowledge for future interactions

## 📝 Example Interaction

```
📘 Personalized Study Assistant
Type 'exit' to stop

Student: What topic do you want help with? machine learning

Agent: This is a basic explanation of machine learning.
Student feedback (e.g., too hard / easy / need example): too hard

[Agent Memory Updated]
{'level': 'beginner', 'preferred_style': 'examples', 'topic_history': ['machine learning']}
----------------------------------------

Student: What topic do you want help with? neural networks

Agent: Let's learn neural networks with a simple real-life example.
Student feedback (e.g., too hard / easy / need example): easy

[Agent Memory Updated]
{'level': 'intermediate', 'preferred_style': 'examples', 'topic_history': ['machine learning', 'neural networks']}
----------------------------------------

Student: What topic do you want help with? exit

Agent: Session ended. Goodbye!
```

## 🔍 Key Concepts Demonstrated

### Agent Learning
- The agent starts with no knowledge about the user
- It learns preferences through explicit feedback
- Each interaction refines its understanding

### Personalization
- Responses evolve based on accumulated knowledge
- The same topic would be explained differently to different users
- Learning style adapts to individual needs

### Memory & State
- The agent maintains persistent state during the session
- Topic history shows the learning journey
- Profile updates demonstrate continuous learning

## 🎓 Educational Value

This demo illustrates:
- **Stateful agents** that maintain context across interactions
- **Adaptive systems** that modify behavior based on feedback
- **User modeling** through implicit and explicit signals
- **Simple machine learning** concepts without complex algorithms

## 🔧 Extending the Code

You can enhance this agent by:
- Adding more learning levels (advanced, expert)
- Implementing more sophisticated feedback analysis
- Saving user profiles to a file for persistent memory
- Adding actual educational content for different topics
- Implementing confidence scores for personalization decisions
- Creating a GUI interface instead of command-line

## 📚 Use Cases

This pattern can be applied to:
- Educational tutoring systems
- Customer support chatbots
- Personalized content recommendation
- Adaptive user interfaces
- Healthcare coaching applications

## ⚠️ Limitations

- Feedback analysis is keyword-based (not using NLP)
- No persistent storage between sessions
- Limited personalization dimensions
- Simple rule-based logic (not ML-based)