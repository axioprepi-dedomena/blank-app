import streamlit as st

st.title("🎈OneQTest")
st.write(
    "Circling on Sunday. Set up first set of questions only, having wrangled through various setup stages."
)

import streamlit as st
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
            st.subheader(f"Question {question['id']}: {question['question']}")
            st.write(f"Related to: {question['article']}")
            answer = st.radio("Is the provider compliant?", ('Compliant', 'Non-compliant', 'Partially compliant', 'Unknown'), key=question['id'])
            question['compliance_level'] = answer
    
    def generate_report(self):
        compliant = sum(1 for q in self.assessment_questions if q['compliance_level'] == "Compliant")
        non_compliant = sum(1 for q in self.assessment_questions if q['compliance_level'] == "Non-compliant")
        partial = sum(1 for q in self.assessment_questions if q['compliance_level'] == "Partially compliant")
        unknown = sum(1 for q in self.assessment_questions if q['compliance_level'] == "Unknown")
        
        st.write("\n--- DSA Compliance Assessment Report ---")
        st.write(f"Total questions: {len(self.assessment_questions)}")
        st.write(f"Compliant: {compliant}")
        st.write(f"Non-compliant: {non_compliant}")
        st.write(f"Partially compliant: {partial}")
        st.write(f"Unknown: {unknown}")
        
        st.write("\nDetailed Results:")
        for question in self.assessment_questions:
            st.write(f"\n{question['article']}:")
            st.write(f"Question: {question['question']}")
            st.write(f"Compliance: {question['compliance_level']}")

    def save_results(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.assessment_questions, f, indent=2)
        st.write(f"\nResults saved to {filename}")

tool = DSAComplianceTool()
tool.run_assessment()
if st.button("Generate Report"):
    tool.generate_report()
    tool.save_results("dsa_compliance_results.json")
