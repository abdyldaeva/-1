import csv
points = 0
with open("quiz.csv", "r", newline="") as a:
    reader = csv.reader(a, delimiter = ',')
    for row in reader:
      print(row[0])
      print(row[1], row[2], row[3],)
      i = input("")
      if i == row[4]:
        points += 5
        print("Правильно!")
      
print("ваш балл = " + str(points))  
if points in range (0, 58):
    print("Ваша оценка F")
elif points in range (59, 66):
    print("Ваша оценка D-")
elif points in range (62, 66):
    print("Ваша оценка D")
elif points in range (66, 69):
    print("Ваша оценка D+")
elif points in range (69, 73 ):
    print("Ваша оценка C-")
elif points in range (73, 76):
    print("Ваша оценка C")
elif points in range (76, 79):
    print("Ваша оценка C+")
elif points in range (79, 82):
    print("Ваша оценка b-")
elif points in range (82, 86):
    print("Ваша оценка b")
elif points in range (86, 89):
    print("Ваша оценка B+")
elif points in range (89, 93):
    print("Ваша оценка A-")
elif points in range (93, 100):
    print("Ваша оценка A+") 