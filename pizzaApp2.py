#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 09:18:02 2020
Jarrett Nobles: CSC204 due 9/13/2020
a pizza ordering app.
@author: jarrett
"""
#welcome statement
cafe="Mercer Pizzareria"
print("Welcome to ",cafe)
#price statement
cost=9.95

print("All pizzas are ",cost)

#empty list
pizzaStyle=[]

#get input on number of pizza
pizzaNum=input("How many pizzas do you want: ")
pizzaNum=int(pizzaNum)

for n in range (pizzaNum):
    style=input("Choose your style of pizza: ")
    pizzaStyle.append(style)

#if statement for flavors not offered
for style in pizzaStyle:
    if style in pizzaStyle:
        pass
    else:
        print("That is not offered")

#solve for subcost
subcost= pizzaNum * cost 
print("Your subcost is $", round(subcost,2))

#solve for total cost
tax=.06
afterTax=subcost * tax
totalCost=round(subcost + afterTax,2)
print('Your total cost is $ ',round(totalCost,2)) 

#present receipt
print("           Your Receipt          ")
print("**********************************")
print("Style\t cost\t Qty\t     Subtotal\t")
for n in range(len(pizzaStyle)):
    print(pizzaStyle[n],"\t",cost,"\t",pizzaNum,"\t","\t",subcost,"\t")
print("Tax 6%:                   ",round(afterTax,2))     
print("Total Cost:              ",totalCost)

#prompt for payment
cash=input("Enter cash payment:$ ")
cash=float(cash)
if cash==totalCost:
    print("Thank you! Your order is placed!")
elif cash < totalCost:
    print("Insufficient funds")
else: 
    print("Your change is : $",round(cash-totalCost,2))    
    
print("**********************************")
          
             
              
    
        



    

  






