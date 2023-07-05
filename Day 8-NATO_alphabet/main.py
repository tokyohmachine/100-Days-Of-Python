import pandas

student_dict = {
    "student": ["Daniela", "Max", "Alex"],
    "score": [56, 78, 87]
}

data_frame = pandas.DataFrame(student_dict)
print(data_frame)

for (index, row) in data_frame.iterrows():
    if row.student == "Daniela":
        print(row.score)