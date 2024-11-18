import random

# new_dict = {new_key:new_value for (key, value) in dict.items()}

dict = {
    "alex": 98,
    "max": 100,
    "ali": 89,
    "jamo": 78,
}

# for person in dict:
#     print(person)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)

passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)

# for student, score in students_scores.items():
#     if score >= 60:
#         print(f"The Student is: {student} and the score is {score}")

sentence = "What is the Airspeed Velocity of an Unladen Swallow?".split()
# for word in range(0, len(sentence)):
#     length = len(sentence[word])
#     print(f"'{sentence[word]}' has {length} letters.")

result = {word: f"{len(word)} letters" for word in sentence}
print(result)





