import streamlit as st

st.title("🎈OneQTest")
st.write(
    "Circling on Sunday."
)

import json

class DSAComplianceTool:
    def __init__(self):
        self.assessment_questions = [
            {
                "id": 1,
                "question": "Does the provider have a clear and accessible Terms of Service?",
                "article": "Article 12",
                "compliance_level": None
            },
            {
                "id": 2,
                "question": "Does the provider publish transparency reports at least once a year?",
                "article": "Article 13",
                "compliance_level": None
            },
            {
                "id": 3,
                "question": "Does the provider have mechanisms to allow users to flag illegal content?",
                "article": "Article 14",
                "compliance_level": None
            },
            # Add more questions based on DSA articles
        ]
        
    def run_assessment(self):
        for question in self.assessment_questions:
            print(f"\nQuestion {question['id']}: {question['question']}")
            print(f"Related to: {question['article']}")
            answer = input("Is the provider compliant? (y/n/partial): ").lower()
            
            if answer == 'y':
                question['compliance_level'] = "Compliant"
            elif answer == 'n':
                question['compliance_level'] = "Non-compliant"
            elif answer == 'partial':
                question['compliance_level'] = "Partially compliant"
            else:
                question['compliance_level'] = "Unknown"
    
    def generate_report(self):
        compliant = sum(1 for q in self.assessment_questions if q['compliance_level'] == "Compliant")
        non_compliant = sum(1 for q in self.assessment_questions if q['compliance_level'] == "Non-compliant")
        partial = sum(1 for q in self.assessment_questions if q['compliance_level'] == "Partially compliant")
        unknown = sum(1 for q in self.assessment_questions if q['compliance_level'] == "Unknown")
        
        print("\n--- DSA Compliance Assessment Report ---")
        print(f"Total questions: {len(self.assessment_questions)}")
        print(f"Compliant: {compliant}")
        print(f"Non-compliant: {non_compliant}")
        print(f"Partially compliant: {partial}")
        print(f"Unknown: {unknown}")
        
        print("\nDetailed Results:")
        for question in self.assessment_questions:
            print(f"\n{question['article']}:")
            print(f"Question: {question['question']}")
            print(f"Compliance: {question['compliance_level']}")

    def save_results(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.assessment_questions, f, indent=2)
        print(f"\nResults saved to {filename}")

# Usage
if __name__ == "__main__":
    tool = DSAComplianceTool()
    tool.run_assessment()
    tool.generate_report()
    tool.save_results("dsa_compliance_results.json")
