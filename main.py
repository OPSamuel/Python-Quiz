import csv
import time

score = 0
count = 0
tries = 3

name = input("Please enter your name: ")

while tries != 0:
        print("Enjoy the quiz! ")
        with open('Secondary School Quiz.csv') as csvfile:
            filereader = csv.reader(csvfile, delimiter=',')
            for row in filereader:
                count = count + 1
                print(row[0])
                print(row[1])
                print(row[2])
                print(row[3])
                answer = input("Please enter an answer: ").upper()
                if answer == row[4]:
                    print("Correct")
                    score = score + 1
                else:
                        print("Wrong")
            result = score/count * 100
            print("You got a score of", score, "out of", count)
            print("As a percentage that is %",result)
            print("******Program will automatically terminate in 10 seconds******")
            time.sleep(10)
            exit(0)