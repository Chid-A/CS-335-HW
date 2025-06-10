#Question 1

name = "Chid Anaele"
age = 21
ai_course = True
print("Name:", name)
print("Age in 5 years:", age + 5)
print("Is enrolled in CS 335 course?", ai_course)

#Question 2 

topics = ["Logic", "Search", "NLP", "ML", "Bayesian Inference","Tokenization" ,"Deep Learning"]

for topic in topics:
 print("We will study:", topic)

 #Question 3 

student = {"name": "Omeed", "score": 92}

if student["score"] >= 95:
 grade = "A+"

elif student["score"] >= 90:
 grade = "A"

elif student["score"] >= 80:
 grade = "B"

else:
 grade = "C or below"
print(f"{student['name']} received a grade of {grade}.")

#Question 4

def greet_student(name):
 return f"Welcome to Omeed, {name}!"

Var1 = 0
Var2 = 0 
Var2 = Var1 * Var1

# Test
print(greet_student("Omeed"))
print(Var2("Squared Num"))
