# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 17:24:18 2021

@author: Annamalai
"""

import pandas as pd

def food_arena(name):
          print(f"\nWelcome {name}! We are ready to serve you")
          print("1. Food order")
          print("2. Cold drinks")
          print("3. Log out")
          
          ty=int(input(">> "))
          
          if ty==4:
              print('You logged out successfully\n')
              intropage()
              
          elif ty==1:
              print("\nWe are enclosing the food list for you")
              print("""
1. Veg
2. Non-Veg
                              
                              """)
              options=int(input(">> "))
              tot_bill,to_bill=0,0
              veg_food_list={'1':('veg-Briyani',60),'2':('Curd rice',30),'3':('Sambar rice',40),'4':('lemon rice',40),'5':('All items',170)}
              non_veg_food_list={'1':('Chicken rice',100),'2':('Shawarma',90),'3':('BBQ Chicken',160),'4':('BBQ wings',120),'5':('All items',470)}
                     
              if(options==1):
                          print("""
1. Veg-Briyani
2. Curd rice
3. Sambar rice
4. lemon rice
5. All
                                    """)
                          opt=[c for c in input(">> ").split(",")]
                          foo_name,bill_list=list(),list()
                          summ=0
                          for i,j in veg_food_list.items():
                            for k in opt:
                                if i==k:
                                  summ+=j[1]
                                  foo_name.append(j[0])
                                  bill_list.append(j[1])
                                  tot_bill=1
                          foo_name.append("Total")
                          bill_list.append(summ)
                          tabley=pd.DataFrame({'Items':foo_name,'cost':bill_list})
                          if(tot_bill==1):
                                  print(tabley)
                                  
                                  tot_bill=0
            
              elif (options==2):
                   print("""
1. Chicken rice
2. Shawarma
3. BBQ Chicken
4. BBQ wings
                                """)
                   opt2=[c for c in input(">> ").split(",")]
                   non_foo,bill2_list=list(),list()
                   sum1=0
                   for i,j in non_veg_food_list.items():
                          for k in opt2:
                                if i==k:
                                  sum1+=j[1]
                                  non_foo.append(j[0])
                                  bill2_list.append(j[1])
                                  to_bill=1
                   non_foo.append("Total")
                   bill2_list.append(sum1)
                   tabley1=pd.DataFrame({'Items':non_foo,'cost':bill2_list})
                   if(to_bill==1):
                                  print(tabley1)
                                  
                                  to_bill=0
              
          elif ty==2:
               print("So far don't have any drinks")
          
          elif ty==3:
                 print("Currently we are not providing any coupons here!")
         
     
def student_login():
                 data_mode='login'
                 print("Please Enter Your User Name")
                 name=input(">>")
                 print("Enter Your Password")
                 pas=(input(">>"))
                 excel_sheet_read(data_mode,name,pas)
                 

def excel_sheet_read(data_mode,name,pas):
                 
                if data_mode=='login':
                                  flag=0
                                  with open('customer_data.txt','r') as file:
                                                  if (name+','+pas+'\n') in file.readlines():
                                                         food_arena(name)
                                                         flag=1
                                  if(flag!=1):
                                        print("Sorry! Invalid Name/password")
                                  
     
def student_signup():
                               data_mode='signup'
                               print("Welcome to the Signup Session")
                               print("Are you new to the system?? if yes press 1 else 0")
                   
                               t=int(input(">> "))
                               f1=0
                               if t==1:
                                        data='signup'
                                        print("Enter your Good Name")
                                        new_name=input(">> ")
                                        print("Enter the Password")
                                        pas1=(input(">> "))
                                        print("Re-Enter the Password")
                                        pas2=(input(">> "))
                                        if pas1==pas2:
                                                 
                                                   with open('customer_data.txt','r+') as file:
                                                         
                                                             if (new_name+','+pas1+'\n') in file.readlines():
                                                                                    print("Data already exists")
                                                             else:
                                                                          f1=1
                                                                          file.write(new_name)
                                                                          file.write(',')
                                                                          file.write(pas1)
                                                                          file.write('\n')
                                                                          
                                                   if(f1==1):
                                                                 print("Thank You for Signing up!")
                                                   
                                                   
                                        
                                        else:
                                              print("The Passwords don't match..Retry")
                                              student_signup()
                                              
                                       
                               elif t==0:
                                       student_login()
                                       
                               else:
                                    print("Type Either 0 or 1")
                                    student_signup()
                   
                      
                          
                   
                   

def intropage():
          print("*** Welcome you all to the Food Ordering System ***")
          print("1. Customer Login")
          print("2. Customer Signup")
          
          
          s=int(input(">> "))
          
          if s==1:
                  print("\nYou have entered the Customer Login Session")
                  student_login()
                  
          elif s==2:
                  print("\nYou have entered the Customer Signup session")
                  student_signup()
                  
          else:
                  print("\nInvalid Key!!!. Choose from the above one.")
                  intropage()
                  


                  
          
def main():
          intropage()
          
          
          
          
main()