
FOODIE UPENDRA
Here you’ll find a collection of delicious recipes that your family will love, all tested and approved by me, creator of this food blog. Cooking is my passion so please follow along and share what I create!

MONDAY, 19 DECEMBER 2022
Python Answers
 Practical no 1

AIM: demonstration of print program

PROGRAM DISCRIPTION: 

1) Print(): 

Syntax print (".....")

This function is use to print/output contents on the screen.

& \t:

Syntax:\t

This function is used to insert a tab/leave 4 spaces between sentence

&\n:

Syntax :\n

This function start the succeeding content/sentence on the new line

 

 

1) PROGRAM TO PRINT “HELLO WORLD”
 

SOURCE CODE:

 

# welcome

 

print("hello world")

 



2) PROGRAM TO PRINT NAME AND ADDRESS
 

SOURCE CODE:

 

# NAME AND ADDRESS

 

print("my name is abhijeet mallah Add:- Flat no. 69,FLAT NO. 69,HELL VILLA,HEAVEN SOCIETY,ETERNITY(WEST)")

 

OUTPUT: 

 
 

3) PROGRAM TO PTINT NAME AND ADDRESS IN 
MULTILINES

 

SOURCE CODE:

#NAME AND ADDRESS

 

 

 

OUTPUT:

 



 

 

4) PROGRAM TO PRINT PATTERN
 
 

SOURCE CODE :

 

#PRINT THE PYRAMID PATTERN 

 

print("\t\t\t\t\t\t1\n")

print("\t\t\t\t1\t\t2\t\t1\n")

print("\t\t\t1\t\t3\t\t3\t\t1\n")

print("\t\t1\t\t4\t\t6\t\t4\t\t1")

 

OUTPUT:



 

5) PROGRAM TO PRINT YEAR AND AMOUNT PATTERN
 

      SOURCE CODE :

       #PRINT THE PATTERN

 

 

print("YEAR\t\t\tAMOUNT")

print("1\t\t\t5550\n2\t\t\t6550\n3\t\t\t8550\n4\t\t\t10050\n5\t\t\t15550\n6\t\t\t20000\n7\t\t\t25000\n8\t\t\t35550\n9\t\t\t45550\n10\t\t\t65550")



 

 

6) PROGRAMM TO PRINT PATTERN
 

 
     

    SOURCE CODE:

 

   #PRINT THE PATTERN 

 

print("This\n\tis\n\t\tMy\n\t\t\tFirst\n\t\t\t\tPython\n\t\t\t\t\tprogram")

 



7) WRITE A PYTHON PROGRAM TO PRINT THE PATTERN.
 

 
 

Source code:- print(“NAME\t:ABC\t\tADDRESS\t:DADAR,MUMBAI-400031”)

 

Print(“std\t:FyBSC\t\tHOBBIES\t:playing cricket and singing”)

 

Output:-

 

 
 

8) PROGRAM TO PRINT PATTERN.
 
 

SOURCE CODE: 

 

#PRINT THE PATTERN 

 

print("12345")

print("\t6789")

print("\t\t12345")

print("\t9876")

print("12345")

 

OUTPUT:

 



9)PROGRAM TO PRINT PATTERN.

 
 

   SOURCE CODE: 

 

 

#PRINT THE FOLLOWING PATTERN

 

print("**********#\n*********#\n********#\n*******#\n******#\n*****#\n****#\n***#\n**#\n*#")

 

 

OUTPUT:-

 



 

 

 

 

AIM: DEMONSTRATION OF INPUT

PROGRAM DISCREPTION: 

• input()
o This function is used to take input from the user
o Syntax: input(“…….”)
• printf()
o This function is used to print/display output on the screen
o Syntax: print (“……..”)
1)

INPUT

#Write a python program to find the average of three number

 

a=int(input("enter the first no"))

b=int(input("enter the second no"))

c=int(input("enter the third no"))

average=a+b+c/3

print("enter the average",average)

OUTPUT



2)

INPUT

#Write a python program to convert KM To M

 

a=float(input("enter the distance in km"))

 

distance=a*1000

print("enter the distance in meter",distance)

OUTPUT

3)

INPUT

#Write a python program to convert time from hours to seconds

 

h=int(input("time in hours"))

s=h*3600

print("enter the time in seconds",s)

OUTPUT

4)

INPUT

#Write a python program to accept length,bredth,hight of abox and print its area and volume

 

l=float(input("entert the length of box"))

b=float(input("enter the bredth of the box"))

h=float(input("enter the height of the box"))

volume=l*b*h

area=2*(l*b+b*h+h*l)

print("enter the volume and area of box",volume,area)

OUTPUT



5)

INPUT

#To calculate the total distance travelled by a vehical in t seconds

 

u=float(input("enter the inital velocity"))

a=float(input("enter the accleration"))

t=float(input("enter the time"))

distance=(u*t)+1/2*(a*t)**2

print("total distance travelled by vehical",distance)

OUTPUT



6)

INPUT

#Write the number and its square

 

a=int(input("enter the number"))

square=a*a

print("square of the no",square)

OUTPUT



7)

INPUT

#Write a python progeam to find sum,subtraction,division and product of the two number

 

a=float(input("enter the first no"))

b=float(input("enter the second no"))

sum=a+b

subtraction=a-b

division=a/b

product=a*b

print("enter the answer",sum,subtraction,division,product)

OUTPUT



8)

  INPUT

#write a python program to find simple interest

 

p=int(input("enter the principal value"))

r=int(input("enter the rate of interest "))

n=int(input("enter the time"))

A=(p*r*n)/100

print("enter the simple interest",A)     

OUTPUT



9)

INPUT

#Write a python program to find discount

 

a=float(input("enter the cost price"))

b=float(input("enter the selling price"))

p=a-b

dis =p*100/a

print("enter the profit percentage",dis)

 

        OUTPUT



10)

INPUT

#Write a python program on discount percent and actual price

 

a=float(input("enter the actual price"))

b=float(input("enter the discount percentage"))

c=a*(b/100)

d=a-c

print("enter the discount",d)

OUTPUT



PRACTICAL 2

IF/ELSE PROGRAM

1.WRITE A PYTHON PROGRAM TO CHECK WHETHER NUMBER

ENTERED IS ODD OR EVEN.

 

Source code:

#program to check whether the no. is odd or even

#declare a as no.

a=int(input("enter no."))

if a%2 == 0:

   print("the given no. is even")

else:

   print("the given no. is odd")

Output:



 

 

 

2.WAP TO CHECK WHETHER NUMBER ENTERED IS DIVISIBLE BY

three OR NOT.

 

Source code:

#PROGRAM TO CHECK WHETHER NUMBER ENTERED IS DIVISIBLE BY three OR NOT.

#declare a the entered no.

a=int(input("enter no."))

#if the given no. divisible by 3,so the remainder must be 0.

if a%3 == 0:

   print("the given no. is divisible by 3")

else:

   print("the given no. is not divisible by 3")

 

Output:

For divisible:



For non divisible:



 

 

 

 

 

 

3.WAP TO CHECK WHETHER THE NUMBER IS DIVISIBLE BY 3 OR

7 OR BOTH.

Source code:

#PROGRAM TO CHECK WHETHER THE NUMBER IS DIVISIBLE BY 3 OR 7 OR BOTH.

#declare a the given integer.

a=int(input("enter the no."))

#after dividing the remainder of the given no. must be o.

if a%3==0 and a%7==0:

   print("the given no. is divisible by both 3 and 7.")

elif a%3==0:

   print("the given no. is only divisible by 3.")

elif a%7==0:

   print("the given no. is only divisible by 7.")

else:

   print("the given no. isn't divisible by both 3 and 7.")

Output:

The all cases are as follows:



4.WAP TO ENTER A 4-DIGIT NUMBER AND CHECK WHETHER IT

IS A LEAP YEAR OR NOT.

 

Source code:

#write a program to check a year for leap year

#declare variable var_year for year.

#Checking if the given year is leap year  

var_year=int(input("enter year(please enter 4 digit no.) "))

if (var_year%4 == 0 and var_year%100!=0) or var_year%400==0 :

   print(var_year,"is a leap year")

else:

   print(var_year,"isn't a leap year")

Output:

The all cases are as follows:



 

 

 

 

 

 

5.WAP TO CHECK WHETHER THE NUMBER ENTERED IS

POSITIVE,NEGATIVE OR ZERO.

Source code:

#program to check the given no. is zero,positive,negative.

#declare a as integer

a=int(input("enter the no. "))

if a==0:

   print("the given no. is zero")

elif a>0:

   print("the given no. is positive")

elif a<0:

   print("the given no. is negative")

else:

   print("you entered a invalid no.")

Output:

The all cases are as follows:



 

 

 

6.WAP TO GRADE THE STUDENTS IN AN ACADEMIC

INSTITUTION ACCORDING TO THE FOLLOWING GROUPS:

 

MARKS GRADE

 

Above or equal Honors

60 to 79    First

50 to 59    Second

40 to 49    Third

Below 40   Fail

Source code:

#write a program to TO GRADE THE STUDENTS IN AN ACADEMIC INSTITUTION.

#declare a as marks. 

a=int(input("enter the percentage"))

if a>=79 or a>=60:

   print("first")

elif a<=59 and a>=50:

   print("second")

elif a<=49 and a>=40:

   print("third")

else:

   print("fail")

 

 

 

 

 

Output:

The all cases are as follows:

 



7.ADMISSON TO A PROFESSIONAL COURSE IS SUBJECT TO THE

FOLLOWING CONDITIONS:

 

a.Marks in Mathematics&gt;=60

b.Marks in Physics&gt;=50

c.Marks in Chemistry&gt;=40

d.Total in all three subjects&gt;=200 or Total in Mathematics and

Physics&gt;=150

Given the marks in all three subjects ,write a programto process

the applications to list the eligible candidates.

Source code:

 

#write a program ADMISSON TO A PROFESSIONAL COURSE IS SUBJECT TO THE FOLLOWING CONDITIONS

#declare a= marks in maths,b=marks in physics,c=marks in chemistry.

a=int(input("enter the marks of mathematics"))

b=int(input("enter the marks of physics"))

c=int(input("enter the marks of chemistry"))

#declare d total of all three subject.

d=a+b+c

#declare e total of maths and physics.

e=a+b

if a>=60:

   print("student is eligible")

elif b>=50:

   print("student is eligible")

elif c>=40:

  print("student is eligible")

elif d>=200 or e>=150:

   print("student is eligible")

else:

   print("student isn't eligible")

 

 

 

 

 

Output:



 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

8.WAP TO COMPUTE THE REAL ROOTS OF A QUADRATIC

EQUATION

Source code:

# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module

import cmath

# declare a,b,c the coefficients of ax**2 + bx + c = 0

a =int(input("enter the coefficient of x^2"))

b =int(input("enter the  coefficient of x "))

c =int(input("enter the  coefficient of x^0"))

 

# calculate the discriminant

d = (b**2) - (4*a*c)

 

# find two solutions

sol1 = (-b-cmath.sqrt(d))/(2*a)

sol2 = (-b+cmath.sqrt(d))/(2*a)

 

print('The solution are {0} and {1}'.format(sol1,sol2))

Output:



 

 

 

9.WAP THAT WILL READ THE VALUE OF X AND EVALUATE THE

FOLLOWING FUNCTION 

y=1 forx>0

0 forx=0

-1 forx<0

Source code:

#PROGRAM THAT WILL READ THE VALUE OF X AND EVALUATE THE FOLLOWING FUNCTION.

#accept the value of x.

x=int(input("enter the value of x"))

if x>0:

   print("y=1")

elif x==0:

    print("y=0")

elif x<0:

    print("y= -1")

else:

    print("invalid")

Output: 



 

10.WAP THAT WILL READ THE VALUE OF X AND EVALUATE THE

FOLLOWING FUNCTION.

y=4x+100 forx>40

300 for x=40

4.5+150 forx<40

Source code:

#PROGRAM THAT WILL READ THE VALUE OF X AND EVALUATE THE FOLLOWING FUNCTION.

#accept the value of x.

x=int(input("enter the value of x"))

if x<40:

   y=4*x+100

   print(y)

elif x==0:

    print("y=300")

elif x>0:

   y=150+4.5

   print(y)

else:

    print("invalid")

Output:



Practical no. 3

 

While loop

 

1.To check whether number is even or odd upto ‘n’ series. Accept ‘n’ value from user.

 

SOURCE CODE

 

num = int(input("Enter a number: "))

int = 0

while int <= num:

   if int % 2  != 0:

       print("{0} is odd".format(int))

   else:

       print("{0} is even".format(int))

   int = int + 1

 

OUTPUT

 



 

2.To print odd number sums in a given range. Accept lower and upper limit from the user

 

SOURCE CODE

lower_limit = int(input("Enter the lower limit of range: "))

upper_limit = int(input("Enter the upper limit of range: "))

 

sum = 0

 

while lower_limit <= upper_limit:

   if lower_limit % 2 != 0:

       sum = lower_limit + sum

   else:

       sum = sum 

   lower_limit = lower_limit + 1

print("The sum of the odd numbers in the entered range is {0}".format(sum))

 

OUTPUT

 



 

3. To print factors of entered number

 

SOURCE CODE

 

num = int(input("Enter a number: "))

 

int = 1

 

while int <= num:

   if num % int == 0:

       print("{0} is a factor of {1}".format(int,num))

   else:

       int = int

   int = int + 1

 

OUTPUT

 

 



 

4.​To display factorial of a number.

 

SOURCE CODE

 

num = int(input("Enter the number: "))

int = 1

fact = 1

 

while int <= num:

   fact = fact * int

   int = int + 1

print(f"The factorial of {num} is {fact}")

 

OUTPUT



 

5. To calculate nPr and nCr values. (Permutations and Combinations)

 

SOURCE CODE

 

n = int(input("Enter the value of n: "))

r = int(input("Enter the value of r: "))

 

n_fact = 0

r_fact = 0

n_min_r_fact = 0

int = 1

fac_n = 1

fac_r = 1

fac_n_min_r = 1

 

while int <= n:

   fac_n = fac_n * int

   int = int + 1

n_fact = n_fact + fac_n

 

int = 1

 

while int <= r:

   fac_r = fac_r * int

   int = int + 1

r_fact = r_fact + fac_r

 

int = 1

 

while int <= (n - r):

   fac_n_min_r = fac_n_min_r * int

   int = int + 1

n_min_r_fact = n_min_r_fact + fac_n_min_r

 

npr = (n_fact) / (n_min_r_fact)

ncr = (n_fact) / ((n_min_r_fact) * (r_fact))

 

print("P({0},{1}) is {2} and C({0},{1}) is {3}".format(n,r,npr,ncr))   

 

OUTPUT

 



 

6. To accept numbers from user and separate out its digits.

 

SOURCE CODE

 

num = int(input("Enter the number: "))

 

while num / 10 != 0:

   digit = num % 10

   print(digit)

   num = int(num/10)

 

OUTPUT

 



 

7.To perform addition of digits of a number.

 

SOURCE CODE

 

num = int(input("Enter the number: "))

sum = 0

num_1 = num

while num / 10 != 0:

   digit = num % 10

   sum = digit + sum

   num = int(num/10)

print(f"The sum of the digits in {num_1} is {sum}")

 

OUTPUT

 



8.To reverse a number.

9. To check whether given number is palindrome or not. (same in reverse order) (eg:- 121 is reversed as 121)

10.To check whether given number is Armstrong or not. (Sum of cube of digits in a number should be the number.)

 

SOURCE CODE

 

num = int(input("Enter the number: "))

num_1 = num

sum = 0

 

while num / 10 != 0:

   digit = num % 10

   x = digit ** 3

   sum = sum + x

   num = int(num/10)

if sum == num_1:

   print(f"The entered number {num_1} is an armstrong number")

else:

   print(f"The entered number {num_1} is not an armstrong number")

 

OUTPUT

 



 

11.​To check whether number is perfect or not.

SOURCE CODE

 

num = int(input("Enter a number: "))

 

int = 1

sum = 0

 

while int < num:

   if num % int == 0:

       sum = sum + int   

   else:

       int = int

   int = int + 1

 

if sum == num:

   print(f"The number entered {num} is a perfect number")

else:

   print(f"The number entered {num} is not a perfect number")

 

OUTPUT

 



 

 

 

12.​To accept to numbers from user, perform its addition till user wish. (Expected output):- 

​◦​Enter first number: 

​◦​Enter second number: 

​◦​Addition of Two number are:  

​◦​Do you want to continue (Y/N)?

 

SOURCE CODE

 

num_1 = int(input("Enter First number: "))

num_2 = int(input("Enter Second number: "))

print(f"The Addition of two numbers is: {num_1+num_2}")

wish = input("Do you want to continue(y for yes/n for no): ")

 

while wish == 'y':

   num_1 = int(input("Enter First number: "))

   num_2 = int(input("Enter Second number: "))

   print(f"The Addition of two numbers is: {num_1+num_2}")

   wish = input("Do you want to continue(y for yes/n for no): ")

print("Thank you for your precious time")

print("Visit Again :D ")

 

OUTPUT

 



PRACTICAL NO. 4.2

TITLE: PROGRAMS BASED ON FOR LOOP

1. WRITE A PYTHON PROGRAM using for loop that asks the user for a number, and prints the digits of the number on screen
Enter a number:456

Digits in number are: 4 5 6

Source Code : 

num = int(input("Enter a number: "))

string = ""

 

for digit in str(num):

    string += digit + " "

 

print(string)

Output:





2. WRITE A PYTHON PROGRAM using for loop to perform addition of 2 numbers till the user wishes.
Source Code:

cont = "yes"

 

for _ in iter(int, 1):

  

    if cont.casefold() == "yes":

        num1 = int(input("Enter first number: "))

        num2 = int(input("Enter second number: "))

 

        ans = num1 + num2

        print("The sum of two numbers is", ans)

        cont = input("Do you want to continue? (yes/no): ")

        

    else:

        print("This program is now closed")

        break

Output:





3. WRITE A PYTHON PROGRAM to calculate factorial of number.
Source Code:

num = int(input("Enter a number: "))

factorial = num

 

for factor in range(1, num):

    factorial *= factor

 

print("{0}! is {1}".format(num, factorial))

Output:





4. WRITE A PYTHON PROGRAM to check number is prime or not.
Source Code:

import math

 

num = int(input("Enter a number: "))

 

isPrime = True

 

for divisor in range(2, (int(math.sqrt(num)) + 1)):

    if num % divisor == 0:

        isPrime = False

        break

 

if isPrime:

    print("Number is prime")

else:

    print("Number is not prime")

Output:

                

     

5. WRITE A PYTHON PROGRAM to check whether number is Armstrong or not.
Source Code:

num = int(input("Enter a number: "))

 

sumofcubes = 0

 

for digit in str(num):

    

    sumofcubes += int(digit) ** 3

 

if sumofcubes == num:

    print("This is an Armstrong number")

else:

    print("This is not an Armstrong number")              

Output: 





6. WRITE A PYTHON PROGRAM to display prime numbers between 1 to 100
Source Code: 

import math

for num in range(1, 101):

    divisor = 2

    factor = 0

    for divisor in range(2, int(math.sqrt(num))):

        if num % divisor == 0:

            factor += 1

            break

 

        divisor += 1

 

    if factor == 0 and num != 1:

        print(num)

    num += 1

Output: 





7. WRITE A PYTHON PROGRAM to check whether number is palindrome or not.
Source Code:

num = int(input("Enter a number: "))

rev = ""

 

for digit in str(num):

    rev = digit + rev

 

if num == int(rev):

    print("{0} is a palindrome".format(num))

else:

    print("{0} is not a palindrome".format(num))

Output:

                   



8. WRITE A PYTHON PROGRAM to check whether number is perfect or not.
Source Code:

num = int(input("Enter a number: "))

 

addition = 0

 

for divisor in range(1, num):

    if(num % divisor == 0):

        addition += divisor

 

if(addition == num):

    print("{0} is a perfect number".format(num))

else:

    print("{0} is not a perfect number".format(num))

Output:

                 



9. Write a program to print Factors of a number.
Source Code:

num = int(input("Enter a number: "))

 

print("Factors of {0} are:".format(num), end = " ")

 

for divisor in range(1, num):

    if(num % divisor == 0):

        print(divisor, end = "  ")

Output:





10. Write a program to reverse a number.
Source Code:

num = int(input("Enter a number: "))

rev = ""

 

for digit in str(num):

    rev = digit + rev

 

print("Reverse of {0} is {1}".format(num, rev))

 

Output:

num = int(input("Enter a number: "))

rev = ""

 

for digit in str(num):

    rev = digit + rev

 

print("Reverse of {0} is {1}".format(num, rev))

 

 

 

 

Programming with Python- I PRACTICAL 5         Demonstration of String 

Program Description: 

replace(): Returns a copy of the string where all occurrences of a substring is replaced with another substring. 

String.Isalnum: Returns true if all the characters in a given string are 

alphanumeric. string.lower: Return a copy of s, but with upper case, letters converted to lower case. string.join: Concatenate a list or tuple of words 

with intervening occurrences of sep. string.swapcase: Converts lower case 

letters to upper case and vice versa. 

string.find: Return the lowest indexing a sub string. 

String.len: Returns the length of the string. 

string.Istitle: Returns True if the string is a title cased string. 

string.count: Return the number of (non-overlapping) occurrences of substring sub in string. string.upper: lower case letters converted to upper case. 

sorted(): Returns a sorted list from the iterable object. 

1.Consider the string “Global variable” &gt;Write statements in python to implement the following: a. To display the last four characters. 

CODE: 

x='Global variable' 

print(x[11:15]) 

OUTPUT:



b. To display the substring starting from index 4 and ending at 8. CODE: 
x='Global variable' 

print(x[4:9]) 

OUTPUT: 



c. To check whether string has alphanumeric character or not.our character from the string. CODE: 
x='Global variable' 

print(x.isalnum()) 

OUTPUT:



d. To trim the first four letter of the string. CODE: 
x='Global variable' 

print(x[4:15]) 

OUTPUT: 



e. To display starting index from the substring “va”. CODE: 
x='Global variable' print(x[7:15]) OUTPUT: 



f. To change the case of the given string. CODE: 
x='Global variable' 

print(x.swapcase()) 

OUTPUT: 



g. To check whether the string is in title case. CODE: 
x='Global variable' 

print(x.istitle()) 

OUTPUT: 



h. To change all the occurrences of letter ‘a’ with ‘o’. CODE: 
x = "Global variable" 

length = len(x) var = '' 

for i in x: 

y = i.replace('a','o') 

var = var + y 

print(" The String after changing the 'a' with 'o' is",var)OUTPUT: 



2. WAP IN PYTHON TP CHECK WHETHER THE ENTERED NUMBER IS PALINDROME OR NOT. CODE: 
x = input("Enter the string:") 

x =x.lower() 

w = "" 

for i in x: 

w = i + w 

if (x == w): 

print("The given string is Pallindrome") else: 

print("The given string is not Pallindrome") 

OUTPUT:



3.WAP IN PYTHON TO SORT THE STRING ENTERED. CODE: 

x = input("Enter the string:") 

x=sorted(x) 

x=''.join(x) 

print(x) 

OUTPUT: 



4. WAP IN PYTHON TO COUNT THE NUMBER OF VOWELS IN A STRING. CODE: 

strg = input("Give the string: ") 

strg = str.lower(strg) str_len = len(strg) 

a = 0 

for i in range(str_len): for j in ['a','e','i','o','u']: if strg[i] == j: 

a +=1 

break 

print("The Number of Vowels in the Given string is: ",a) OUTPUT: 



5.PROGRAM TO ACCEPT A STRING FROM THE USER AND CHEKS IT STARTS WITH A OR NOT. CODE: 

strg = input("Give the string: ") 

strg = str.lower(strg) 

if strg[0] == 'a': 

print("The Given String is staring with 'A'") 

else: 

print("The Given String is not staring with 'A'") 

OUTPUT:



6. WRITE A PYTHON PROGRAM TO CALCULATE THE LENGTH OF A STRING. CODE: 

strg=input("Enter the string : ") 

count=0 

for i in str_len: 

count += 1 

print("The length of the string is : ",count) OUTPUT: 



7.WAP TO COUNT THE NUMBER OF CHARACTERS(CHARACTER FREQUENCY) IN A STRING. CODE: 

strg = input("Give the string: ") 

strg = str.lower(strg) 

strg2 = [] 

for i in strg: 

if i not in strg2: strg2.append(i) 

for i in range(len(strg2)): 

print("The Frequency of %s in the given string is:%i"%(strg2[i], strg.count(strg2[i]))) OUTPUT:



8.WRITE A PYTHON PROGRAM TO REVERSE A STRING AND STRING IS “BANANA”. CODE: 

strg=input("Enter the string : ") 

print("The reverse of the string is : ",strg[::-1]) OUTPUT: 



9. WRITE A PYTHON PROGRAM TO GET A STRING MADE OF FIRST 2 AND LAST 2CHARS FROM A GIVEN STRING.IF STR LENGTH IS LESS THAN 2 ,RETURN INSTEAD OF THE EMPTY STRING. CODE: 

strg = input("Enter the string : ") l = len(strg) 

newstrg = "" 

for i in range(0, len(strg)): 

if l < 3: 

break 

else: 

if i in (0, 1, l-2, l-1): 

newstrg = newstrg + strg[i] else: 

continue 

print("Input string : " + strg ) 

print("New String : " + newstrg) 

OUTPUT:



10.WAP THAT TAKES INPUT FROM THE USER AND DISPLAYS THAT INPUT BACK IN UPPER 

AND LOWER CASE. 

CODE: 

strg = input("Enter the string : ") 

print("The string in upper case ", strg.upper()) print("The string in lower case ", strg.lower()) 

OUTPUT:



11. WAP IN PYTHON TO REVERSE THE ENTERED STRING. CODE: 
strg=input("Enter the string : ") 

print("The reverse of the string is : ",strg[::-1]) 

OUTPUT: 



12. WRITE A PYTHON PROGRAM TO ADD “ING” AT THE END OF THE GIVEN STRING.IF THE GIVEN STRING ALREADY ENDS WITH “ING” ADD “LY” INSTEAD. IF THE STRING LENGTH OF THE GIVEN STRING IS LESS THAN 3 LEAVE IT UNCHANGED. 
CODE: 

strg = input("Enter the string: ") if len(strg) < 3: 

print(strg) 

elif strg[-3:] == 'ing': 

print("The changed string is: ",strg + 'ly') else: 

print("The changed string is: ",strg + 'ing') 

OUTPUT:

  

Q13. WAP TO CHANGE A GIVEN STRING TO NEW STRING BY EXCHANGING FIRST AND THE LAST LETTER. CODE: 

Str = input("Give a String: ") 

Str = str.lower(Str) 

Str1 = Str 

Str = Str.strip(Str[0]) 

Str = Str.strip(Str[-1]) 

Str = Str1[-1] + Str + Str1[0] 

print("The String After Editing is",Str.title())

OUTPUT: 



Q14. WAP TO COUNT OCCURRENCE OF SUBSTRING. SOURCE CODE: 

Str = input("Give a String: ") 

Str = str.lower(Str) 

sub_str = input("Give a Sub-String: ") 

if Str.count(sub_str) != 0: 

print("Number of occurrence of %s: %i"% (sub_str, Str.count(sub_str))) else: 

print("There is no occrrence of the sub-string.") 

OUTPUT:

 



Q15. WAP TO CALCULATE THE ASCII VALUE OF THE GIVEN STRING. SOURCE CODE: 

Str = input("Give a String: ") 

print("ASCII Sentence: ") for i in Str: 

if i == ' ': 

print(" ", end = '') 

else: 

print(ord(i), end = '') print() 

 

 

 

 

 

 

 

PRACTICAL 5

Aim:Demonstration of List

Program Description:Python Lists are just like dynamically sized arrays, declared in other languages (vector in C++ and ArrayList in Java). In simple language, a list is a collection of things, enclosed in [ ] and separated by commas.

Practical work

Q1. WAP TO CREATE A LIST OF SEM1 SUBJECTS AND DISPLAY IT ON SCREEN.

SOURCE CODE:

Subject = [

'1. Fundamentals of Computer Organization & Introduction to Embedded Systems',

'2. Programming with Python- I',

'3. Linux Fundamentals',

'4. Algorithms and Programming with C',

'5. Discrete Mathematics',

'6. Descriptive Statistics and Introduction to probability',

'7. Soft Skills Development'

                 ]

for i in Subject:      print(i)

OUTPUT:



Q2. WAP TO ASK STUDENTS TO ENTER SUBJECT CODE AND THE SUBJECT NAME.

SOURCE CODE:

Subjects = [

'Fundamentals of Computer Organization & Introduction to Embedded Systems.',

'Programming with Python- I.',

'Linux Fundamentals.',

'Algorithms and Programming with C.',

'Discrete Mathematics.',

'Descriptive Statistics and Introduction to probability',

'Soft Skills Development']

Codes = ['101','102','103','104','105','106','107']

INPUT = input("Give the Classroom Code: ") var_code = INPUT[-3:]

for i in range(7):

         if var_code == Codes[i]:

              print(f"The Subject for code {INPUT} is {Subjects[i]}")

              break

         elif i == 6:

              print("The given code is invaide.")

              break

         else:

              continue

OUTPUT:


Q3. WAP TO CREATE AN EMPTY AND ADD ANY 5 TARGETS DEPENDS ON PRIORITY.

SOURCE CODE:

empty_list = []

for i in range(5):

    var_1 = int(input("Give the Position of priority: "))

    empty_list.insert(var_1-1,input(f"Give Your {var_1} Target accoding to your Priority: "))

print("The Given Targets are ")

for i in range(5):

    print(f"{i+1}. {empty_list[i]}")

OUTPUT:



Q4. WAP TO CREATE A LIST OF YOUR 12TH MARKS AND SUBJECTS.

GENERATE A NEW LIST FOR YOUR MARKS IN DESCENDING ORDER.

DISPLAY MINIMUM MARKS THAT YOU HAVE SCORED. DISPLAY MAXIMUM MARKS THAT YOU HAVE SCORED. DISPLAY TOTAL MARKS THAT YOU HAVE SCORED. DISPLAY AVERAGE MARKS THAT YOU HAVE SCORED. DISPLAY YOUR PERCENTAGE.

SOURCE CODE:

Subjects = ['English',

          'IT',

          'Mathematics & Statistics',

          'Physics',

          'Chemistry',

          'Biology',

          ]

Marks = []

for i in Subjects:

    Marks.append(int(input("Give your marks in %s :"%i))) print()

#1. GENERATE A NEW LIST FOR YOUR MARKS IN DESCENDING ORDER. Var_marks = Marks

#Sorting the list in descending order. Var_marks.sort(reverse=True)              

#Printing the list

print("A. My Marks in Descending order are Given as follows: ") for i in Var_marks:

    print(i,end = ' ')

print()

#2. DISPLAY MINIMUM MARKS THAT YOU HAVE SCORED.

print(f"B. The Minimum marks i have scored is {min(Var_marks)}.")

#3. DISPLAY MAXIMUM MARKS THAT YOU HAVE SCORED.

print(f"C. The Maximum marks i have scored is {max(Var_marks)}.")

#4. DISPLAY TOTAL MARKS THAT YOU HAVE SCORED.

print(f"D. The Total marks i have scored is {sum(Var_marks)}.")

#5. DISPLAY AVERAGE MARKS THAT YOU HAVE SCORED.

print("E.  The  Average  marks  i  have  scored  is %.2f."%float(sum(Var_marks)/6))

#6. DISPLAY YOUR PERCENTAGE.

print(f"F.  The  Percentage  i  have  scored  is %.2f%%."%float(sum(Var_marks)/6))

OUTPUT:



Q5. WAP TO ASK USER TELEPHONE NO. ALONG WITH STD CODE BASED ON STD CODE, FIND LOCATION.

SOURCE CODE:

Area = ['New Delhi', 'Uttar Pradesh', 'Haryana', 'Rajasthan','Punjab',

       'Himachal Pradesh', 'Jammu and Kashmir', 'Maharashtra',

       'Gujarat', 'West Bengal', 'Andaman and Nicobar Islands',

       'Jharkhand', 'Sikkim', 'Arunachal Pradesh', 'Assam',

       'Nagaland', 'Mizoram', 'Tripura', 'Manipur', 'Tamil Nadu',

       'Kerala', 'Uttarakhand', 'Bihar', 'Orissa', 'Madhya Pradesh',

       'Chhattisgarh', 'Karnataka', 'Goa', 'Andhra Pradesh',

       'Telangana']

Code = ['011', '120', '124', '141', '160',

       '174', '191', '020',

       '079', '033', '319',

       '326', '359', '360', '361',

       '363', '369', '372', '381', '3845',

       '044', '468', '594', '611', '664', '714',

       '770', '080', '832', '840',

       '040']

INPUT = input("Give a your phone number with the STD Code: \n") Input = INPUT[:3]

for i in range(len(Code)):

    if Code[i] == Input:

         print(f'Your Place is {Area[i]}')           break

OUTPUT:


Q6. WAP TO ACCEPT A NAME FROM FEMALE CUSTOMER ALONG WITH PREFEX AND CHECK WHETHER 'SHE' IS MARRIED OR UNMARRIED

SOURCE CODE:

Name = input("Give your name with the your prefix: \n")

prefix = Name.split()

if prefix[0] == 'Mrs' or prefix[0] == 'Mrs.':      print(f'{Name} is Married')

else:

    print(f'{Name} is Unmarried')

OUTPUT:



Q7.WAP TO COUNT THE NUMBER OF ALPHABET IN THE GIVEN WORD.

SOURCE CODE:

Str_Word = input("Give the word: ") Str_Word1 = Str_Word.lower() list_Word = []

for i in Str_Word1:

    list_Word.append(i)

for i in range(len(Str_Word)):

    var_x = list_Word.count(list_Word[i])

    print(f"The  number  of  {list_Word[i]}  in  the  {Str_Word}  is {var_x}.")

OUTPUT:


Q8.WAP TO TAKE STUDENT NAME AND ROLL.NO FROM THE USER AND PRINT IT ACCORDING THE USER WANT.

SOURCE CODE:

No_Stu = int(input("Give the number of student: "))

Name_Stu = []

Roll_Stu = []

for i in range(No_Stu):

    Name_Stu.insert(i,input("Give the name of Student: "))

    Roll_Stu.insert(i,input("Give the roll no of Student: "))

print('\n\n\n')

Input = input("Name: ")

for i in range(len(Name_Stu)):

    if Input == Name_Stu[i]:

         print("Roll no.:",Roll_Stu[i])

         break

    elif i == (len(Name_Stu)-1):

         print("The given name is not in Data.")           break

OUTPUT:


Q9. Python Program to assign each list element value equal to its magnitude order

SOURCE CODE:

test_list = [0,3,7,1,9,3,7,4,5,11,45,3,2,1,7] print("The original list is : " + str(test_list)) ord_dict = list(set(test_list))

res = [ord_dict.index(ele) for ele in test_list] print("Relative size ordered list : " + str(res))

OUTPUT:


Q10.Python program to implement matrix multiplication SOURCE CODE:

X = [[5,5,9], [1 ,5,3],

[2 ,6,8]] print(X)

Y = [[8,5,3], [8,5,1],

[3,1,4]]

print(Y)

print("Multiplying matrix X by matrix Y") result = [[0,0,0,0],

[0,0,0,0],

[0,0,0,0]]

for i in range(len(X)):   

   for j in range(len(Y[0])):

       for k in range(len(Y)):

           result[i][j] += X[i][k] * Y[k][j] for x in result:

   print("Result",(x))

OUTPUT:


 

PRACTICAL 6

TUPLE

1. Create tuple to store 5 countries names and display it SOURCE CODE:
country = ("USA","RUSSIA","CHINA","AUSTRALIA","INDIA") print(country)

OUTPUT:



2. Demonstrate packing and unpacking concept in tuple
    SOURCE CODE:

     #Packing of tuple

tup_1 = (1,"DOG",3.14)

#unpacking of tuple

a,b,c = tup_1

#Printing unpacked elements of tuple

print(a) print(c) print(b)

OUTPUT:



3.Tuples can be mutable in some case.Write suitable example. SOURCE CODE:

#Mutable objects in tuple are mutable

tup_2 = ("ELON",2.56,["JAVISH",93,(234,344,2132),"MUSK"],{"My":23})

#Trying to reassign immutable objects tup_2[0] = 34

OUTPUT:



#Trying to reassign mutable objects tup_2 [2][0] = "LAVISH" print(tup_2)

OUTPUT: 



4.Create tuple to store 10 students marks and display it by for loop

SOURCE CODE:

students = ("JEFF","ELON","BERNARD","GAUTAM","MUKESH","AKSHAY","ANIRUD H","MARK","SHIV","MJ")

marks = (78,68,57,45,87,98,98,50,77,85)

for i in range(0,10):

   print(f"{students[i]} : {marks[i]}")

OUTPUT:



6.demonstrate any methods of tuples

SOURCE CODE:

#Methods of tuple in python

t1 = ("NEW ZEALAND",56,["H",34,5.66,"dhhd"],{"hh":76},"yuuu") #Prints the length of the tuple t1

length = len(t1)

print(f"THE LENGTH OF THE TUPLE t1 is {length}")

t2 = (12,34,23,34,56,34,11,89,67,87,34,22,12,12) #Prints the maximum element of tuple t2

maximum = max(t2)

print(f"THE MAXIMUM ELEMENT IN t2 is {maximum}")

#Prints the minimum element of tuple t2

minimum = min(t2)

print(f"THE MINIMUM ELEMENT IN t2 is {minimum}")

#Prints the index of first occurrence of the element 34 in t2

index = t2.index(34)

print(f"34 COMES FIRST IN THE INDEX POSITION OF {index} IN t2")

#Prints the number of occurence of the number 12 in t2

counts = t2.count(12)

print(f"THE NUMBER 12 OCCURS {counts} TIMES IN t2")

OUTPUT:



PRACTICAL 7

DEMONSTRATION OF DICTIONARY

1.Create dictionary of integer keys which can store 5 elements. SOURCE CODE:



OUTPUT:



2.Write a program to access key value. Accept key from user

SOURCE CODE:



OUTPUT:



3.Create dictionary which can store squares of a number.

SOURCE CODDE:



OUTPUT:



4. Apply pop, pop item, clear and del.
SOURCE CODE:



OUTPUT:



5. Use any 5 methods of dictionary.
SOURCE CODE:



OUTPUT:



6. Apply sorted method on dictionary.
SOURCE CODE:



OUTPUT:



 

 

Practical No. 8

Functions

Q1] Write modular program to perform four basic operation on two numbers Code:

#1.write modular program to perform four basic operation on two numbers def performAdd(a, b):

print("Addition of a and b is",a+b)

def performSub(a, b): 

print("Subtraction of a and b is",a-b)

def performMulti(a, b): 

print("Multiplication of a and b is",a*b)

def performDiv(a, b):

if b==0:

print("Division by 0 is not possible") else:

print("Division of a by b is",a/b)

a1=int(input("Enter a: ")) b1=int(input("Enter b: ")) performAdd(a1, b1) performSub(a1, b1) performMulti(a1, b1) performDiv(a1, b1)

Output:



Q2] Write a program to create function to calculate factorial of number Code:

#2.Write a program to create function to calculate factorial of number def factorial(a):

if a==2:

return 2 

else:

return a*factorial(a-1)

num=int(input("Enter the number to calculate factorial for: ")) print("Factorial of given number",num,"is",factorial(num))

Output:



Q3] Write a program to check entered number is prime or 

not Code:

#3.Write a program to check entered number is prime or not import math

def primeOrNot(a):

isPrime = True

for i in range(2, int(math.sqrt(a))): 

if (a%i==0):

print("Number is not prime") 

isPrime = False

break

if isPrime==True: 

print("Number is prime")

a=int(input("Enter a number: ")) primeOrNot(a)

Output:



Q4] Write a program to check number is even or odd Code:

#write a function to check number is even or odd def evenodd(a):

if a%2==0:

print(a,"is 

even") else:

print(a,"is odd")

num=int(input("Enter a number: ")) evenodd(num)

Output:



Q5] Program to check number is positive or negative 

Code:

#write a program to check if number is positive or negative def posneg(a):

if a==0:

print("Number is 

zero") elif a<0:

print("Number is negative") 

else:

print("Number is positive")

num=int(input("Enter a number: ")) posneg(num)

Output:



ANONYMOUS FUNCTIONS

1. Write an anonymous function which evaluate expression entered from user




2. Write an anonymous function to square a number by passing the value at the definition time




3. Write a function to double the number




4. Write a function to implement map reduce and filter
FILTER





MAP





REDUCE





5. Write a function which can handle if else




6. Write a function which uses loop




 

PROGRAMS ON MODULES 

1] Explore any 5 from the following modules : 
1. Math 
2. Calendar 
3. Time 
4. Random 
5. Numpy 
Code:

import math import calendar import time import random import numpy 

#Returns the arc cosine of a number print("Are cosin of 0.55 is",math.acos(0.55)) 

#Rounds a number up to the nearest integer print("Round up 1.545 to",math.ceil(1.545)) 

#Display the calendar print(calendar.month(2022, 11)) 

#Prints current time 

print("Current time:",time.ctime(time.time())) 

#Returns a random number the given range 

print("Random number in range(1,9) is",random.randrange(1, 10)) 

#Create a array 

arr = numpy.array([1,2,4,5]) print("Array using numpy is",arr) 

Output:


2] Create a user defined module calculation and design form functions 
Addition 

Subtraction 

Multiplication 

Division. And use that module functions is demo.py 

Code:

import add import sub import multi import div 

a,b = 10,5 add.Addition(a,b) sub.Substract(a,b) multi.Multiply(a,b) div.Division(a,b) 

Output: 



3] Create a module to calculate factorial and another module to calculate nPr and nCr in the second program. 
Code:

import factorial import nprncr 

a=int(input("Enter a number to calculate factorial: ")) factorial.Facto(a) 

n,r=5,2 

print(n,r) nprncr.Permuations(n,r) nprncr.Combinations(n,r) 

Output:



Practical 9

Q1] Opening a file and printing the lines using for loop Code:

filename = input("Enter name of input file: ") inputFile = open(filename, "r")

for line in inputFile:

print(line)

inputFile.close()

print("Completed reading of file", filename)

Output:



Q2] Opening the file and printing the lines using while loop Code:

import sys

inputFileName = input ("Enter name of input file: ") inputFile = open(inputFileName, "r") print("Opening file", inputFileName, " for reading.") line = inputFile.readline()

while (line != ""):

sys.stdout.write(line)

line = inputFile.readline()

inputFile.close()

print("\nCompleted reading of file", inputFileName)

Output:



Q3] Data processing

Code:

inputFile = open ("employees.txt", "r")

print ("Reading from file input.txt")

BONUS = int(5000)

for line in inputFile:

name,job,income = line.split(',')

last,first = name.split()

income = int(income)

income = income + (0.1 * BONUS)

print("Name: %s, %s\t\t\tJob: %s\t\tIncome $%.2f" %(first,last,job,income))

print ("Completed reading of file input.txt") inputFile.close()

Output:



Q4] Writing to a new file

Code:

inputFileName = input("Enter the name of input file to read the grades from: ") outputFileName = input("Enter the name of the output file to record the GPA's to: ") inputFile = open(inputFileName, "r")

outputFile = open(outputFileName, "w")

print("Opening file", inputFileName, " for reading.")

print("Opening file", outputFileName, " for writing.") gpa = 0

for line in inputFile:

if (line[0] == "A"):

gpa = 4

elif (line[0] == "B"):

gpa = 3

elif (line[0] == "C"):

gpa = 2

elif (line[0] == "D"):

gpa = 1

elif (line[0] == "F"):

gpa = 0

else:

gpa = -1

temp = str (gpa)

temp = temp + '\n'

print (line[0], '\t', gpa)

outputFile.write (temp)

inputFile.close ()

outputFile.close ()

print ("Completed reading of file", inputFileName) print ("Completed writing to file", outputFileName)

Output:



Q5] Appending data to a existing file Code:

outputFileName = input("Enter the name of the output file to append new data: ") outputFile = open(outputFileName, "a+")

print("Opening file", outputFileName, " for appending.")

newData = "\nAlice Li,CAG,77000\nElisa Gem,Heroine,89000" outputFile.write(newData)

outputFile.close()

Output:





 

posted by Upendra @ December 19, 2022  0 comments

About Me
My Photo
Name:
Upendra
Location:
India
View my complete profile

Links
Google News
Edit-Me
Edit-Me
Previous Posts
Python Answers
 Grilled Chicken Breasts – its an easy and all-pur...
Choclate cake
Pav bhagi
Jerra Rice
Tandoori chicken
Chicken biryani
Veg pulav
Archives
August 2017
July 2022
December 2022
Powered by Blogger

Subscribe to
Posts [Atom]

 
