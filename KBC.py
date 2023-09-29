# Write a Program to perform as a KBC Question Bank

# que1 = ("Who is the Current Railway Minister of India is")
# optionsA = ("\n1. Mamta Banarjee ")
# optionsB = ("\n2. Ram Vilash ")
# optionsC = ("\n3. Ashwini Vaishnaw ")
# optionsD = ("\n4. Piyush Goyal ")

# print(que1 + optionsA + optionsB + optionsC + optionsD)

# a = input("Choose your answer : ")

# Score = 0

# if a == "3":
#     print("Correct Answer")
#     Score = Score + 100
#     print("Congrats, Your Total Score is ",Score)

# else :
#     print("Wrong Answer")
#     print("Your Current Score is ",Score )

que1 = [
    ["Who is the Current Railway Minister of India is", "1. Mamta Banarjee ",
        "2. Ram Vilash ", "3. Ashwini Vaishnaw ", "4. Piyush Goyal ", 1],
    ["Who is the Current Railway Minister of India is", "1. Mamta Banarjee ",
        "2. Ram Vilash ", "3. Ashwini Vaishnaw ", "4. Piyush Goyal ", 1],
    ["Who is the Current Railway Minister of India is", "1. Mamta Banarjee ",
        "2. Ram Vilash ", "3. Ashwini Vaishnaw ", "4. Piyush Goyal ", 1],
    ["Who is the Current Railway Minister of India is", "1. Mamta Banarjee ",
        "2. Ram Vilash ", "3. Ashwini Vaishnaw ", "4. Piyush Goyal ", 1]
]


levels = [20, 30, 50, 100, 200, 400, 800, 1000]
# print(que1)
money = 0  # Default Money Variable
# i = 0
for i in range(0, len(que1)):
    Question = que1[i]
    # Heading Before Question
    print(f"Comming Up Question for RS. {levels[i]}")

    print(f"{que1[0]}")  # Question

    print(f"a. {que1[i][1]}        b. {que1[i][2]}")  # Options for Questions
    print(f"c. {que1[i][3]}        d. {que1[i][4]}")

    reply = int(input("Enter Your Answer (1-4):"))  # Users Reply

    # if (reply == 0):
    #     money = levels[i-1]
    #     break

    if (reply == que1[i][-1]):
        print(f"Correct Answer, You have earned {levels[i]}")
        # if (i == 4):
        #     money = 20

        # elif (i == 6):
        #     money = 30
    else:
        print("Wrong Answer, Give me my Money Back")
        break

