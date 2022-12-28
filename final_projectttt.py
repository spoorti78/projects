import json
import sys
import random
class Restaurant:
    Restaurant_name=  "********Jadhav's Kitchen********"
    
    def __init__(self):
        self.fooditems={}
        self.user_info={}
        self.order_food=[]
#Admin portal

#Add food items 
        
    def add_fooditems(self):
        
        food_name = input('Enter the food name: ')
        food_quantity = input('Enter the food quantity: ')
        food_price = input('Enter food price: ')
        food_discount = input('Enter discount on food: ')
        food_stock = input('Enter food stock: ')
        
        item = {'food_name':food_name,'food_quantity':food_quantity,'food_price':food_price,'food_discount':food_discount,'food_stock':food_stock}
        foodid=len(self.fooditems)+1
        self.fooditems[foodid]=item
        
        with open('food_items.json','w') as f:
            json.dump(self.fooditems,f)

#edit food items fronm menu useing id of food           
    def edit_fooditems(self):
        Id = input('\nEnter food id to edit food item: ')
        
        with open('food_items.json','r') as f:
            data = json.load(f)
        
        for i,j in data.items():
            if Id == i:
                for k in j:
                    data[i][k]=input('Enter the changed '+k+' : ') 
        print('\nYour food item with food Id '+Id+' updated successfully!')
        
        with open('food_items.json','w') as f:
            json.dump(data,f)
    
 #display of menu       
    def view_fooditems(self):
        
        with open("food_items.json","r")as f:
            data=json.load(f)
            
        for i,j in data.items():
            print("\nfoodid:",i)
            for k in j:
                print(k+':'+j[k])
                
 #remove food items if they are out of stock            
    def remove_fooditem(self):
        self.foodid=input("enter food id to be removed:")
        with open("food_items.json","r")as f:
            data=json.load(f)
            data.pop(self.foodid)
        print('\nYour food item with food ID '+data[self.foodid]['food_name']+' removed successfully!')  
        with open('food_items.json','w') as f:
            json.dump(data,f)
 
 # User portal
 #user registartion   

    def user_registration(self):
        self.Full_name=input("Enter your name:")
        self.phoneno=int(input("Enter your no: "))
        self.Email=input('Enter your email:')
        self.Address=input("Enter your address:")
        self.password=input("Password:   ")
        
        user={"fullname":self.Full_name,"Phoneno:":self.phoneno,"Email":self.Email,"Address":self.Address,"Password":self.password}
         
        userid=len(self.user_info)+20000
        self.user_info[userid]=user
          
            
        with open("users_data.json","w")as f:
            json.dump(self.user_info,f)
        print('\nDear ', self.Full_name ,'! Your User ID: ', userid,' and Password: ', self.password ,' generated successfully!')
    
   #update user Information 
    def update_user_info(self):
        userid= input('\nEnter user ID to edit profile: ')
        
        with open('users_data.json','r') as f:
            data = json.load(f)
        
        for i,j in data.items():
            if userid== i:
                for k in j:
                    data[i][k]=input('Enter the changed '+k+' : ') 
        
        print('\nYour profile with user Id '+userid+' updated successfully!')
        with open('users_data.json','w') as f:
            json.dump(data,f)
  #login portal  
    def user_login(self):
        loginid=input("Enter login id:")
        password=input("Enter password:")
        
        with open("users_data.json ","r")as f:
            data=json.load(f)
            
        for i,j in data.items():
            if loginid==i:
                if j["Password"]==password:
                    print("welcome you have logged in successfullly")
                    
    #calling ordering functions                
                    while True:
                        self.input=int(input('\n1----place new order \n2----order history  \n0----logout'))
                        if self.input==1:
                            x.place_new_order()
                            add_new_item=int(input("add new item : \n1----yes  \n2----no"))
                            if add_new_item==1:
                                x.place_new_order
                            else:
                                x.order_history()
                        elif self.input==2:
                            x.order_history()
                        elif self.input==0:
                            print("your account has been logged out successfully")
                            print("Thank you....!")
                            sys.exit()
                            
            else:
                print("incorrect credentials")
 #ordeing function   
    def place_new_order(self):
        
        with open("food_items.Json","r") as f:
            data=json.load(f)
            
        print("Menu card")
        
        for i,j in data.items():
            print(i,j["food_name"],'(',j['food_quantity'],')'  ' ' "₹",j['food_price'])
    
        self.order_no=list(input("\nselect your food"))
        self.order_item=self.order_no
        
        print("\n your selected food list is:")
        for i,j in data.items():
            for k in self.order_no:
                if k == i:
                    print(i,data[i]['food_name'],' (',data[i]['food_quantity'],')',' [₹',data[i]['food_price'],']')
        
        
        confirm_order = int(input('\nConfirm this order --> \n1 --> Yes\n2 --> No'))
        order_number = random.randint(10000,99999)
        
        if confirm_order == 1:
            print('Your order is placed successfully, Order ID: ',order_number,'\n Thank You!!')
        
        elif confirm_order == 2:
            print('Your order has been cancelled')   

    def order_history(self):
        print('\nYour previous orders list is: ')
        
        with open('food_items.json','r') as f:
            data = json.load(f)
        
        for i,j in data.items():
            for k in self.order_food:
                if k == i:
                    print(i,data[i]['food_name'],' (',data[i]['food_quantity'],')',' [₹',data[i]['food_price'],']') 
            
            
#object calling            
            
x=Restaurant()
print("Wel come to" ' '+x.Restaurant_name)
#Main calling function
while True:
    entry= int(input("Please enter your in restaurant \n1.admin \n2.user \n0.exit"))
    if entry==1:
        while True:
            admin_input=int(input("enter your task \n1.add_fooditems \n2.edit_fooditems \n3.view_fooditems \n4.remove_foofitems \n0.exit"))
            if admin_input==1:
                x.add_fooditems()
                add_item=int(input('\nAdd more item: \n1. Yes\n2. No'))
                if add_item==1:
                    x.add_fooditems()
                
            elif admin_input == 2:
                x.edit_fooditems()
            
            elif admin_input == 3:
                x.view_fooditems()
            
            elif admin_input == 4:
                x.remove_fooditem()
            
            elif admin_input == 0:
                print('\nExit from the application!')                
                break
            
            else:
                print('\nPlease select the valid input from the options.')  
            
    elif entry == 2:
        while True:
            user_input = int(input('\n1.New User Registration \n2. User Login  \n3.update_info \n0. Exit'))
            
            if user_input == 1:
                x.user_registration()
            
            elif user_input == 2:
                x.user_login()
           
            elif user_input ==3 :
                x.update_user_info()
            
            elif user_input == 0:
                print('\nExit From Application')    
                sys.exit()

            else:
                print('\nPlease Enter valid input')    
                  
    elif entry == 0:
        print(' Thank You!, Visit Again',Restaurant.Restaurant_name) 
        sys.exit()