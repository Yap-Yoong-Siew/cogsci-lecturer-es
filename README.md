# Cognitive Science Lecturer Expert System


This is a prototype of an expert system developed for WID2001 - Knowledge Representation and Reasoning. Our group decided to develop the expert system based on the Cognitive Science course


We applied expert system components into the system as described below:

1. Knowledge Base

- Our chosen knowledge representation technique was a rule-based representation.
- Hence, extracted knowledge from our domain expert was converted into rules and stored in the knowledge base.

2. Inference Engine

- We applied a forward chaining approach with deductive reasoning to generate conclusions based on the student's input.
- This is a data driven approach where the system collects input from the student to narrow down the possible conclusions until a final conclusion can be presented back to the student.

3. User Interface

## To Run

1. Run command `pip install -r requirements.txt`
2. Run `python lecturer_es.py` and open the app locally.
