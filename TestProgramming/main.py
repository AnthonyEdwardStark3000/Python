with open('student_marks.txt') as file:
    student_list = []
    name_list = []
    for value in file:
        value = value.strip()
        student_list.append(value)
    # print(student_list)
    for i in range(1, len(student_list), 2):
        if int(student_list[i]) >= 80:
            # print(student_list[i])
            name_list.append(student_list[i - 1])
    for names in name_list:
        print(names)
