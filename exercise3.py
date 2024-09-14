# start

# 1

height: float = float(input("what's the height number?"))

while True:
 if  0.4 <= height <= 2.5:
   print()
 else:
    print("wrong input")
 break

# end

# 2

# start

num1:int = int(input("what's the number1?"))
num2:int = int(input("what's the number2?"))

for i in range (num1,num2+1, +1):
   print(i, end=" ")
else:
   for i in range (num1, num2-1,-1):
      print(i, end=" ")

# end

# 3

# START

counter: int = 1
x:float = float (input("How much is a pie?"))

while x ==3.14 and counter < 3:
    counter += 1
x = float(input("How much is a pie?"))

if counter == 3:
    print(f"you are correct")
else:
    print(f"pie is 3.14")

# end

# 4

# start

while True:
    grade1: int = int(input("grade1:"))
    grade2: int = int(input("grade2:"))
    grade3: int = int(input("grade3:"))
    avg_grades = (grade1 + grade2 + grade3) // 3

    if 0 <= grade1 <= 10 and 11-1<= grade2 <= 60 and 61-1 <= grade3 <= 100\
     and not grade1 == grade2 == grade3:
     break

# end


#challenge

counter: int = 1
x: int = int (input("what is your age? "))

while x >= 18 and counter <= 10:
    counter += 1
    x = int(input("what is your age? "))
    counter += 2
    x2 = int(input("what is your age?"))
    counter += 3
    x3 = int(input("what is your age?"))
    counter += 4
    x4 = int(input("what is your age?"))
    counter += 5
    x5 = int(input("what is your age?"))
    counter += 6
    x6 = int(input("what is your age?"))
    counter += 7
    x7 = int(input("what is your age?"))
    counter += 8
    x8 = int(input("what is your age?"))
    counter += 9
    x9 = int(input("what is your age?"))
    break
if x >= 18 and counter == 10:
  print(f"You can drink, you are 18")

if not x >= 18:
  print("You can't drink")
else:
    print(f"You can drink, you are 18")

#end