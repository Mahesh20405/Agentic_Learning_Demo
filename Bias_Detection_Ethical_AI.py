import re
from collections import defaultdict

# Memory: Track patterns and learn from corrections
bias_memory = {
    "detected_patterns": defaultdict(int),
    "user_corrections": [],
    "bias_score": 0,
    "categories_found": set()
}

# Bias detection rules based on ethical AI principles
BIAS_PATTERNS = {
    "gender": [
        (r'\b(he|his|him)\b.*\b(doctor|engineer|CEO|manager|leader)\b', 'masculine profession assumption'),
        (r'\b(she|her)\b.*\b(nurse|secretary|assistant|teacher)\b', 'feminine profession stereotype'),
        (r'\b(female|woman|girl)\b.*\b(emotional|sensitive|nurturing)\b', 'gender trait stereotype'),
        (r'\b(male|man|boy)\b.*\b(aggressive|strong|logical)\b', 'gender trait stereotype')
    ],
    "race": [
        (r'\b(Asian)\b.*\b(good at math|smart|hardworking)\b', 'racial stereotype'),
        (r'\b(Black|African)\b.*\b(athletic|musical)\b', 'racial stereotype'),
        (r'\b(white|Caucasian)\b.*\b(privileged|default)\b', 'racial assumption')
    ],
    "age": [
        (r'\b(old|elderly|senior)\b.*\b(slow|confused|outdated|forgetful)\b', 'age-based discrimination'),
        (r'\b(young|millennial|Gen Z)\b.*\b(lazy|entitled|inexperienced)\b', 'age-based stereotype')
    ],
    "socioeconomic": [
        (r'\b(poor|low-income)\b.*\b(uneducated|criminal|lazy)\b', 'class-based bias'),
        (r'\b(rich|wealthy)\b.*\b(smart|successful|deserving)\b', 'class-based assumption')
    ]
}

def detect_bias(text):
    """Analyze text for potential biases"""
    findings = []
    text_lower = text.lower()
    
    for category, patterns in BIAS_PATTERNS.items():
        for pattern, description in patterns:
            if re.search(pattern, text_lower, re.IGNORECASE):
                findings.append({
                    'category': category,
                    'description': description,
                    'severity': 'medium'
                })
                bias_memory['detected_patterns'][category] += 1
                bias_memory['categories_found'].add(category)
    
    return findings

def calculate_bias_score():
    """Calculate overall bias score based on detections"""
    total_detections = sum(bias_memory['detected_patterns'].values())
    return min(total_detections * 10, 100)

def suggest_alternatives(text, findings):
    """Provide neutral alternatives"""
    suggestions = []
    
    for finding in findings:
        if finding['category'] == 'gender':
            suggestions.append("Use gender-neutral terms like 'they/them' or refer to role without gender assumptions")
        elif finding['category'] == 'race':
            suggestions.append("Focus on individual qualities rather than racial generalizations")
        elif finding['category'] == 'age':
            suggestions.append("Describe capabilities without age-based assumptions")
        elif finding['category'] == 'socioeconomic':
            suggestions.append("Avoid linking economic status with character or ability")
    
    return list(set(suggestions))

def learn_from_feedback(was_correct):
    """Learn from user feedback"""
    if was_correct:
        bias_memory['bias_score'] = calculate_bias_score()
        return "✓ Detection confirmed. Updating bias awareness patterns."
    else:
        return "✗ False positive noted. Improving detection accuracy."

def generate_report():
    """Generate ethical AI compliance report"""
    print("\n" + "="*60)
    print("ETHICAL AI ANALYSIS REPORT")
    print("="*60)
    print(f"Bias Score: {bias_memory['bias_score']}/100")
    print(f"Categories Detected: {', '.join(bias_memory['categories_found']) if bias_memory['categories_found'] else 'None'}")
    print(f"\nDetection Breakdown:")
    for category, count in bias_memory['detected_patterns'].items():
        print(f"  • {category.capitalize()}: {count} instance(s)")
    print("="*60)

def run_bias_detector():
    """Main interaction loop"""
    print("="*60)
    print("AI BIAS DETECTION ASSISTANT")
    print("="*60)
    print("This tool demonstrates ethical AI principles by detecting")
    print("potential biases in text based on fairness considerations.")
    print("\nType 'report' to see analysis summary")
    print("Type 'exit' to stop\n")
    
    while True:
        print("-"*60)
        text = input("\nEnter text to analyze (or command): ").strip()
        
        if text.lower() == 'exit':
            generate_report()
            print("\nSession ended. Remember: Ethical AI requires constant vigilance!")
            break
        
        if text.lower() == 'report':
            generate_report()
            continue
        
        if not text:
            print("Please enter some text to analyze.")
            continue
        
        # Detect bias
        findings = detect_bias(text)
        
        if not findings:
            print("\nNo obvious bias patterns detected.")
            print("   (Note: This is a simplified demo - real bias detection is more complex)")
        else:
            print(f"\nDetected {len(findings)} potential bias pattern(s):\n")
            
            for i, finding in enumerate(findings, 1):
                print(f"   {i}. Category: {finding['category'].upper()}")
                print(f"      Issue: {finding['description']}")
                print(f"      Severity: {finding['severity']}")
            
            # Provide suggestions
            suggestions = suggest_alternatives(text, findings)
            print("\nSuggestions for more ethical language:")
            for i, suggestion in enumerate(suggestions, 1):
                print(f"   {i}. {suggestion}")
            
            # Get feedback
            feedback = input("\nWas this detection helpful? (y/n): ").strip().lower()
            result = learn_from_feedback(feedback == 'y')
            print(f"   {result}")
        
        # Show current bias awareness
        print(f"\nCurrent Bias Awareness Score: {calculate_bias_score()}/100")

# Run the detector
if __name__ == "__main__":
    run_bias_detector()
