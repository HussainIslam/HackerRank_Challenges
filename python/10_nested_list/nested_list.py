#!/bin/python3

if __name__ == '__main__':
    students = []
    # students = [['Harry', 37.21], ['Berry', 37.21], [
    #     'Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    secondLowest = sorted(set([student[1] for student in students]))[1]
    print("\n".join(sorted([(student[0])
                            for student in students if student[1] == secondLowest])))
