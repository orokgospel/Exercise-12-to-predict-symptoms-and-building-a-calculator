x=input()
if x=="hello":
  print("hi")
if x=="hi":
  print("hello")
#Exercise 1
def Diagnose(body):
    print("Welcome to Corona Virus Quarantine device")
    print(body)
    body = input('Enter the expected result:\n',)
    if body=="positive" :
        print("virus confirmed")
    elif body!= "positive":
        print("result not found")
    if body =="negative":
        print("not infected")
        return

Diagnose('body')
#Exercise 2
number1=int(input("Enter first value: \n"))
number2=int(input("Enter 2nd value: \n"))
plus= number1 + number2
minus= number1 - number2
division=number1 / number2
print("Plus Answer is: \n", plus)
print("Minus Answer is: \n",minus)
print("Division Answer is: \n",division)
