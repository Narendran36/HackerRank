if __name__ == '__main__':
    student = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name,score])
    
mark_2 = sorted(list(set([score for name,score in student])))[1]
names = sorted(list(set([name for name,score in student if score == mark_2])))
for name in names:
    print(name)
