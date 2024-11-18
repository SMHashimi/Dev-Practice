import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(value[0])

toDataFrame = pandas.DataFrame(student_dict)
# print(toDataFrame)

# for (key, value) in toDataFrame.items():
#     print(value)

#loop through rows of a data frame
for (index, row) in toDataFrame.iterrows():
    print(row.score)























