#i=1
#j=int(input("Enter Number - "))
#while i<=j:
#    print("*"*j)
#    i=i+1


#i=0
#j=int(input("Enter Number - "))
#while i<=5:
 #   print(j*" " + "*"*i)
  #  i=i+1
   # j=j-1



#for i in range():


 #   print("*" * i)

  #  i = i - 1

#x="1"
#y="2"
#print(int(x)+int(y))
#i=int(input("enter any number:"))
#while(i<=38):
 #   i=int(input("enter any number:"))
  #  print(i)

#print("done with loop")


#x=str(input("what's your city name?\n"))
#y=str(input("what's your pet name?\n"))
#print("The band name is "+ x+ " "+y)



#calculator
#name1=input("enter any name:")
#name2=input("enter any name:")
#combine=(name1+name2)
#x=combine.lower()
#t=combine.count('t')
#r=combine.count('r')
#u=combine.count('u')
#e=combine.count('e')
#true=t+r+u+e

#l=combine.count('l')
#o=combine.count('o')
#v=combine.count('v')
#e=combine.count('e')
#love=l+o+v+e
#score=str(true)+str(love)
#print(score)


#treasure island
#print('''
#*******************************************************************************
#          |                   |                  |                     |
# _________|________________.=""_;=.______________|_____________________|_______
#|                   |  ,-"_,=""     `"=.|                  |
#|___________________|__"=._o`"-._        `"=.______________|___________________
#          |                `"=._o`"=._      _`"=._                     |
# _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
#|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
#|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
# _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
#|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
#|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
#____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
#/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
#____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
#/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
#____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
#/______/______/______/______/______/______/______/______/______/______/_____ /
#*******************************************************************************
#''')
#print("Welcome to Treasure Island.\n")
#print("Your mission is to find treasure.")
#x=str(input("enter left or right:"))
#if x=="left" :
# y=(input("enter swim or wait"))
 #if y == "wait":
  #z=input("wait,which door ,red or blue or yellow")

  #if z=="red":
   #  print("game over")
  #elif z=="blue":
   #  print("game over")
  #else:
   #     print("YOU WIN")
 #else:
  #  print("game over")


#else:
 #print("game over")

#avg of heights
#height=input("enter any heights:").split()
#for n in range(0,len(height)):
#    height[n]=int(height[n])
#print(height)
#sum=0
#for n in height:
#    sum+=n
#    print(sum)

#    length=len(height)
#total=sum/length
#print(total)


#highest scores

#scores=input("enter any scores:").split()
#for x in range(0,len(scores)):
#    scores[x]=int(scores[x])
#    print(scores)
#scores=[1,2,91,100]
#height_score=0
#for x in scores:
#    if scores > height_score:
#        height_score=scores
#    print(f"{height_score}")


#FIZZBUZZ
# x=int(input("enter any numbers:")).split()
#for i in range(1, 100):
#    if i % 3 == 0:
#        print("fizz")
#    elif i % 5 == 0:
#        print("buzz")
#    elif i % 3 == 0 and i % 5 == 0:
#        print("FIZZBUZZ")
#    else:
#        print(i)


#password generator
#import random
#letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#numbers=["0","1","2","3","4","5","6","7","8","9"]
#spl_letters=["!","@","#","$","%","^","&","*"]
#nr_letters=int(input("enter no of letters you want in password:"))
#nr_numbers=int(input("enter no of numbers you want in password:"))
#nr_spl_letters=int(input("enter no of spl yo want in password:"))
#password=""
#password_list=[]
#for i in range(1,nr_letters+1):
    #random_i=random.choice(letters)
    #password+=random_i
    #print(password)
 #   password_list.append(random.choice(letters))
#for i in range(1,nr_numbers+1):
 #   password_list.append(random.choice(numbers))
#for i  in range(1,nr_spl_letters+1):
 #   password_list.append(random.choice(spl_letters))
  #  print(password_list)
   # random.shuffle(password_list)
#password=""
#for i in password_list:
 #   password+=i
  #  print(f"this is new password{password}")


#functions
#def greet(name):
 #   print(f"hello {name}")
  #  print(f"how are u {name}")

#greet("Lavanya")


#Paint wall
#import math
#def area_paint(height,width,cover):
 #   area=height*width
  #  total=math.ceil(area/cover)
   # print(f"the no.of cans{total}")

#area_paint(3,5,10)


#prime
#def prime(num):
    # is_Prime=True

  #for i in range(2, num):
    #    if num % i == 0:
     #      print("not ")
      #  else:
       #     print("true")
    #       is_Prime=False
    # if is_Prime:
    #   print("true")
    # else:
    #   print("not prime")


#prime(10)


#encryption
#alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#enter=input("enter any plain text:")
#print(enter)
#shift_key=int(input("enter key:"))
#print(shift_key)
#def encrypt(plain_text,shift):
 #   cipher_text=[]
  #  for i in enter:
   #     position=alphabet.index(i)
    #    new_position=position+shift_key
     #   new_i=alphabet[new_position]
      #  cipher_text  +=new_i
       # print(f"new letter is {cipher_text}")

#encrypt(plain_text=enter,shift=shift_key)


#reorgansing code
#direction=input("enter e encrypt or d decrypt:")
#text=input("type ur msg:\n").lower()
#shift_amount=int(input("type key:"))
#def caesar(start_text,shift_amount,cipher_direction):
 #    end_text=""
  #   for letter in start_text:
   #      position=alphabet.index(letter)
    #     if cipher_direction=="decode":
     #        shift_amount*=-1
      #   new_position=position+shift_amount
       #  end_text +=alphabet[new_position]
     #print(f"here is {direction}d result:{end_text}")

#caesar('mmbb',1,'decode')


#DICTIONARIES
#list={"Bank":"THIS IS BANK",
 #     "COM":"THIS IS A COM",
  #    "CLS":"THIS IS CLS"}
#list={}
#list["Blank"]="This is B"
#print(list)

#using functions
#travel_log=[
  #    {"country":"France",
   #    "cities_visited":["SISCO","ABCD","EFGH"],
 #  #    "Cities" :12
#},
#{
   #   "country":"Germany",
  #    "cities_visited":["a","b","c"],
 #     "Cities":12
#},

#]

#def travel(Cont,cit,num):
     # new_list=[]
    #  new_list["country"]=Cont
   #   new_list["cities_visited"]=cit
  #    new_list["Cities"]=num
 #     travel_log.append(new_list)

#add_new_list=["Ru",["jkldi","jkldo"],1]
#print(travel_log)
#Hangman
#list=["apple","ball","cat"]
#import random
#x=random.choice(list)
#print(x)
#y=len(x)
#display=[]
#for _ in x:
 #   display+="_"
#print(display)
#user_input=input("enter guess letter: ")
#m=user_input.lower()


#for position in range(y):
 #   if x==m:
  #      print("right")
   #     display[position]=m
    #else:
     #   print("wrong")
#print(display)


#Secret Auction program
#from art import logo
#print(logo)
#bids={}

#Functions with outputs
#def my_function():
#    return 3*2
#my_function()

#def format_name(f_name,l_name):
 #   if f_name=="" or l_name=="":
  #      return "you did not provide valid names"
    #print(f_name.title())
    #print(l_name.title())
   # formated_f_name=f_name.title()
    #formated_l_name=l_name.title()
    #print(f"{formated_f_name} {formated_l_name}")
    #return f"{formated_f_name} {formated_l_name}"
#formated_string=format_name("ANgEla","YU")
#print(formated_string)
#print(format_name(input("enter any name:"),input("enter aby task")))

#Calendar events
#def leap_year(num):
 #   if num%4==0:
  #      if num%100==0:
   #         if num%400==0:
    #            return True
     #       else:
      #          return False
       # else:
        #    return True
    #else:
     #   return False
#string=leap_year(2000)
#print(string)


#Black jack
#import random
#def deal_card():
 #   cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  #  x=random.choice(cards)
   # print(x)
    #y=random.choice(cards)



#user_cards = []
#computer_cards=[]
#is_game_over=False
#while not is_game_over:

 #   """take list of cards and appends score of cards"""
#for i in range(2):
    #new_card=deal_card()
    #user_cards.append(deal_card)
    #computer_cards.append(deal_card)
#def sum(cards):
#    return sum(cards)
#user_score=calculate_score(user_cards)
#computer_score=calculate_score()
#print(f"Your cards:{user_cards},current score:{user_score}")
#print(f"Computer's first card:{computer_cards[0]}")
#if user_score==0 or computer_score==0 or user_score>21:
 # is_game_over=True
#else:
 #   user_should_deal=input("Type 'y' to get another card,type 'n'to pass: ")
  #  if user_should_deal=='y':
   #     user_cards.append(deal_card())
    #else:
     #   is_game_over=True
#while computer_score!=0 and computer_score<17:
 #   computer_cards.append(deal_card())
  #  computer_score=calculate_score(computer_cards)
#def calculate_score(cards):
 #

  #  :type cards: object

#    if sum(cards)==21 and len(cards)==2:
 #       return 0
  #  if 11 in cards and sum(cards)>21:
   #     cards.remove(11)
    #    cards.append(1)
    #return sum(cards)

#def compare(user_score, computer_score):
#        if user_score == computer_score:
 #           return "Draw"
  #      elif computer_score == 0:
   #         return "lose,opponent has Blackjack"
    #    elif user_score == 0:
     #       return "win with blackjack"
      #  elif user_score > 21:
       #     return "you went over.you loose"
        #elif computer_score > 21:
         #   return "opponent went over.You win"
        #elif user_score > computer_score:
         #   return "You win"
        #else:
         #   return "You loose"

#print(compare(user_score,computer_score))

#Local,Global scope
#python=10
#def fun():
 #   def py():
  #      python1=20
   #     print(python1)
    #py()
#fun()
#print(python)

#python=10
#def py():
 #   def func():
  #   cr=["en","la","gg"]
   #  if python==10:
    #    print(cr[0])
    #func()
#print(python)
#py()



#game
#data = [
 #   {
  #      'name': 'Instagram',
   #     'follower_count': 346,
    #    'description': 'Social media platform',
     #   'country': 'United States'
   # },
    #{
     #   'name': 'Cristiano Ronaldo',
      #  'follower_count': 215,
       # 'description': 'Footballer',
        #'country': 'Portugal'
    #},
    #{
     #   'name': 'Ariana Grande',
      #  'follower_count': 183,
       # 'description': 'Musician and actress',
        #'country': 'United States'
    #},
    #{
     #   'name': 'Chetan',
      #  'follower_count': 300,
       # 'description': 'Student',
        #'country': 'India'
    #},
    #{
     #   'name': 'Lavanya',
      #  'follower_count': 350,
       # 'description': 'Actress',
        #'country': 'United States'
    #},
    #{
     #   'name': 'Aashish',
      #  'follower_count': 270,
       # 'description': 'Social media platform',
        #'country':'Brazil'
#}

#}

#Guessing number
#from random import randint

#Easy=10
#Hard=5
#def func(answer,guess):
#
 #   if guess>answer:
  #      print( "too high")
   # elif guess<answer:
    #    print ( "too low")
    #else:
     #print( "near to answer")
#def set_difficulty():
 #   input("enter hard or easy")
#
 #   if Easy:
  #      return Easy-1
   # elif Hard:
    #    return Hard-1
    #else:
     #   print("type proper input")
#set_difficulty()
#answer= randint(1, 100)
#print(f"correct answer is {answer}")
#guess = int(input("guess numbers between 1 and 100"))


#class Solution:
 #   @staticmethod
  #  def isPalindrome(num):
   #     temp = num
    #    reverse = 0
     #   while temp > 0:
      #      remainder = temp % 10
       #     reverse = (reverse * 10) + remainder
        #    temp = temp // 10
        #if num == reverse:
        #    return True
        #else:
         #   return False

#def _driver():
 #   num = int(input("Enter any number: "))
  #  print(Solution.isPalindrome(num))

#_driver()

#   HCF of two numbers
def func(num1, num2):
    min_no = min(num1, num2)
    print (min_no)

    while min_no:

       if num1 % min_no == 0 and num2 % min_no == 0:
        break

        min_no += -1

    print(min_no)


func(4, 6)








