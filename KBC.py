questions = [

["Who is the first computer programmer?","Lady Agusta","Charls Williams","Harry Potter","None",1],
["Which Programming language used to make fb?","Java script","python","c++","None",2],
["Who is the first computer programmer?","Lady Agusta","Charls Williams","Harry Potter","None",1],
["Which Programming language used to make fb?","Java script","python","c++","None",2],
["Who is the first computer programmer?","Lady Agusta","Charls Williams","Harry Potter","None",1],
["Which Programming language used to make fb?","Java script","python","c++","None",2],
["Who is the first computer programmer?","Lady Agusta","Charls Williams","Harry Potter","None",1],
["Which Programming language used to make fb?","Java script","python","c++","None",2]

]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,320000]
money = 0

i = 0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f"{question[0]}")
    print(f" a.{question[1]}   b.{question[2]}   c.{question[3]}     d.{question[4]}")
    reply = int(input("Enter your answer (1-4): "))
    if(reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if(i == 4):
            money = 10000
        elif(i == 8):
            money = 320000
    else:
        print("Wrong answer!!")
        break

print(f"Your take home money is {money}")