# PROJECT ON GROCERY MANAGEMENT

import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import date

pd.set_option("display.max_rows",500)
pd.set_option("display.max_columns",500)
pd.set_option("display.width",1000)

#CART
def viewcart():
    print("------------------------------CART-------------------------------")
    if (os.path.isfile("CART.csv")):
        df=pd.read_csv("CART.csv",index_col=0)
        print(df)
        print("TOTAL AMOUNT = ",df["TOTAL PRICE"].sum())
        order=input("DO YOU WANT TO PLACE AN ORDER (Y/N): ")
        if order=="Y" or order=="y":
            d=date.today()
            items=df["QUANTITY"].sum()
            
            SUM=0
            for i in range(1,len(df)+1):
                SUM=SUM+df["TOTAL PRICE"][i]
                
            gst=12.5/100*SUM #GST 12.5%
            discount=0.10*SUM # FIXED DISCOUNT 10%
            net_bill=SUM+gst-discount
            
            c_id=input("ENTER CUSTOMER ID:") 
            em=input("ENTER EMAIL ID:")
            n=input("ENTER NAME:")
            pn=input("ENTER PHONE NUMBER:")
        
            if (os.path.isfile("ORDERS.csv")):
                df1=pd.read_csv("ORDERS.csv",index_col=0)
                order_id=df1.iloc[len(df1)-1,0]+1
                
                dic={"ORDER_ID":order_id,"DATE":d,"CUSTOMER_ID":c_id,"NO. OF ITEMS":items,
                 "TOTAL AMOUNT":SUM,"NET BILL AMOUNT":net_bill}
                df=pd.DataFrame(dic,index=[len(df1)+1])
                print(df)
                df.to_csv("ORDERS.csv",mode="a",header=None)
            else:
                order_id=101
                dic={"ORDER_ID":order_id,"DATE":d,"CUSTOMER_ID":c_id,"NO. OF ITEMS":items,
                 "TOTAL AMOUNT":SUM,"NET BILL AMOUNT":net_bill}
                df=pd.DataFrame(dic,index=[1])
                df.to_csv("ORDERS.csv")
            
            print("ORDER CONFIRMED ")
            
            print("*"*70)
            print(" "*30,"BILLING INVOICE"," "*30)
            print("*"*70)
            
            print("NAME: ",n,"\t EMAIL ID: ",em)
            print("PHONE NUMBER: ",pn)
            print("DATE: ",d)
            bi=pd.read_csv("CART.csv",index_col=0)
            print()
            print("-"*29,"your Items","-"*29)
            print(bi)
           
            print()
            print("Total Amount to pay with gst and discount:",net_bill)
            print("*"*70)
            print()
            os.remove("CART.csv")
            
        elif order=="N" or order=="n":
            print("")
            print("1.ADD MORE ITEMS TO CART")
            print("2.EXIT TO MAIN MENU")
            print("")
            ch=int(input("ENTER YOUR CHOICE : "))
            if ch==1:
                print("1.STAPLES")
                print("2.BEVERAGES")
                print("3.SNACKS")
                print("4.BREAKFAST AND DAIRY")
                print("5.BABY AND KIDS")
                TYPE=int(input("ENTER THE TYPE OF THE PRODUCT YOU WANT TO ADD TO CART :"))
                if TYPE==1:
                    c="STAPLES.csv"
                elif TYPE==2:
                      c="BEVERAGES.csv"    
                elif TYPE==3:
                    c="SNACKS.csv"   
                elif TYPE==4:
                    c="BREAKFAST DAIRY.csv"
                elif TYPE==5 :
                    c="KIDS.csv"
                else:
                    print("WRONG CHOICE ENTERED")
                if TYPE in[1,2,3,4,5]:
                    df=pd.read_csv(c,index_col=0)
                    print(df[["PRODUCT ID","PRODUCT NAME"]])
                    p_id=input("ENTER THE PRODUCT ID YOU WANT TO ADD TO CART: ")
                    print("")
                    for i in range (1,len(df)+1):
                        if df["PRODUCT ID"][i]==eval(p_id):
                               c_id=df["PRODUCT ID"][i]
                               c_name=df["PRODUCT NAME"][i]
                               price=df["PRICE"][i]
                               quan=int(input("ENTER QUANTITY :"))
                               total=price*quan
                               dic={"PRODUCT ID":c_id,"PRODUCT NAME":c_name,"PRICE":price,"QUANTITY":quan,"TOTAL PRICE":total}
                               if (os.path.isfile("CART.csv")):
                                  df2=pd.read_csv("CART.csv",index_col=0)
                                  df=pd.DataFrame(dic,index=[len(df2)+1])
                                  df.to_csv("CART.csv",mode="a",header=None)
                               else:
                                  df=pd.DataFrame(dic,index=[1])
                                  df.to_csv("CART.csv")
                               print("------------------------------CART-------------------------------")
                               if (os.path.isfile("CART.csv")):
                                   df=pd.read_csv("CART.csv",index_col=0)
                                   print(df)
                                   print("TOTAL AMOUNT = ",df["TOTAL PRICE"].sum())
                               else:
                                   print("YOU HAVE NO ITEMS IN THE CART")
                
            elif ch==2:
                mainmenu()
            
            else:
                print("WRONG CHOICE ENTERED")
    else:
        print("YOU HAVE NO ITEMS IN THE CART")

#MENU CHOICES
def mainmenu():
    while(True):
        print("")
        print("----------------------MAIN MENU----------------------")
        print("")
        print("1. CUSTOMER DETAILS ")
        print("2. PRODUCTS ")
        print("3. VIEW CART")
        print("4. VIEW ORDER DETAILS")
        print("5. STATISTICS")
        print("6. BACK TO HOME PAGE ")
       
        opt=int(input("ENTER YOUR CHOICE FROM THE ABOVE MENTIONED CHOICES : "))
        if opt==1 :
            print("")
            print("----------------CUSTOMER MENU----------------")
            print("")
            print("1. ADD NEW CUSTOMER DETAILS")
            print("2. UPDATE CUSTMOER DETAILS")
            print("3. VIEW ALL CUSTOMERS")
            print("4. DELETE THE CUSTOMER ")
            optn=int(input("ENTER YOUR CHOICE  : "))
            if optn==1 :
                print("------------------------")
                print("ADD NEW CUSTOMER DETAILS")
                print("------------------------")
                cid=input("ENTER CUSTOMER ID : ")
                cname=input("ENTER CUSTOMER NAME : ")
                phn=input("ENTER CUSTOMER'S PHONE NUMBER : ")
                email=input("ENTER CUSTOMER'S EMAIL ID :  ")
                dic={"NAME":cname,"ID":cid,"PHONE NO":phn,"EMAIL":email}
                if (os.path.isfile("CUSTOMER.csv")):
                    df1=pd.read_csv("CUSTOMER.csv")
                    df=pd.DataFrame(dic,index=[len(df1)+1])
                    df.to_csv("CUSTOMER.csv",mode="a",header=None)
                else:
                    df=pd.DataFrame(dic,index=[1])
                    df.to_csv("CUSTOMER.csv")
                
            elif optn==2 :
                print("")
                print("-------------------------")
                print("UPDATE CUSTOMER'S DETAILS")
                print("-------------------------")
                print("")
                df=pd.read_csv("CUSTOMER.csv",index_col=0)
                print(df[["NAME","ID"]])
                cid=int(input("ENTER CUSTOMER ID YOU WANT TO UPDATE :"))
                for i in range(1,len(df)+1) :
                    if  df["ID"][i]==cid:
                        print("YOUR RECORD HAS BEEN FOUND ")
                        op=int(input("PRESS 1 TO MAKE CHANGES IN NAME OR 0 TO RETAIN THE SAME VALUE : "))
                        if op==1:
                            cname=input("ENTER NEW CUSTOMER NAME : ")
                            df.loc[i,"NAME"]=cname
                            df.to_csv("CUSTOMER.csv")
                           
                        op=int(input("PRESS 1 TO MAKE CHANGES IN PHONE NUMBER OR 0 TO RETAIN THE SAME VALUE : "))
                        if op==1 :
                            phn=int(input("ENTER NEW PHONE NUMBER : "))
                            df.loc[i,"PHONE NO"]=phn
                            df.to_csv("CUSTOMER.csv")
                        op=int(input("PRESS 1 TO MAKE CHANGES IN EMAIL OR 0 TO RETAIN THE SAME VALUE : "))
                       
                        if op==1:
                            email=input("ENTER NEW EMAIL : ")
                            df.loc[i,"EMAIL"]=email
                            df.to_csv("CUSTOMER.csv")
                        break
                        print("YOUR RECORD UPDATED SUCCESSFULLY")
                else:
                    print("NO RECORD FOUND")
                
            elif optn==3:
                print("")
                print("-----------------ALL CUSTOMER'S DETAILS-----------------")
                print("")
                df=pd.read_csv("CUSTOMER.csv",index_col=0)
                print(df)
                
            else :
                print("-------------------------")
                print("DELETE CUSTOMER'S DETAILS")
                print("-------------------------")
                print("")
                df=pd.read_csv("CUSTOMER.csv",index_col=0)
                print(df[["NAME","ID"]])
                cust=input("ENTER CUSTOMER NAME WHOSE DETAILS YOU WANT TO DELETE : ")
                custid=input("ENTER CUSTOMER ID WHOSE DETAILS YOU WANT TO DELETE : ")
                for i in range(1,len(df)+1) :
                    if df["NAME"][i]==cust and df["ID"][i]==eval(custid):
                        df=df.drop([i])
                        df=df.to_csv("CUSTOMER.csv")
                        print("CUSTOMER SUCCESSFULLY DELETED")
                        break
                else :
                    print("NO MATCH FOUND")
                    
#------------------------------------------------------------------------------------------------#
        elif opt==2:
            print("")
            print("-----------PRODUCT MENU-----------")
            print("")
            print("1. Add New Product Details")
            print("2. Modify Existing Product Details")
            print("3. Search a product")
            print("4. View all the products ")
            print("5. Delete Product Details")
            choice=int(input("ENTER YOUR CHOICE : "))
            if choice==1 :
                print("-----------------------")
                print("ADD NEW PRODUCT DETAILS")
                print("-----------------------")
                P_ID=input("ENTER PRODUCT ID : ")
                p_name=input("ENTER PRODUCT NAME : ")
                quantity=int(input("ENTER THE QUANTITY OF THE PRODUCT : "))
                PRICE=float(input("ENTER THE PRICE OF THE PRODUCT : "))
                stock=input("IS THE PRODUCT IN STOCK (Y/N):")
                print("1.STAPLES")
                print("2.BEVERAGES")
                print("3.SNACKS")
                print("4.BREAKFAST AND DAIRY")
                print("5.BABY AND KIDS")
                TYPE=int(input("ENTER THE TYPE OF THE PRODUCT FROM THE ABOVE MENU :"))
                cat=input("ENTER THE CATEGORY OF THE PRODUCT : ")
                dic={"PRODUCT ID":P_ID,"PRODUCT NAME":p_name,"QUANTITY":quantity,"PRICE":PRICE,
                     "PRODUCT TYPE":TYPE,"CATEGORY":cat,"STOCK":stock}
               
                
                if TYPE==1 :
                   if (os.path.isfile("STAPLES.csv")):
                      df2=pd.read_csv("STAPLES.csv",index_col=False)
                      df=pd.DataFrame(dic,index=[len(df2)+1])
                      df.to_csv("STAPLES.csv",mode="a",header=None)
                   else:
                      df=pd.DataFrame(dic,index=[1])
                      df.to_csv("STAPLES.csv")
                      
                elif TYPE==2 :
                    if (os.path.isfile("BEVERAGES.csv")):
                       df2=pd.read_csv("BEVERAGES.csv",index_col=False)
                       df=pd.DataFrame(dic,index=[len(df2)+1])
                       df.to_csv("BEVERAGES.csv",mode="a",header=None)
                    else:
                       df=pd.DataFrame(dic,index=[1])
                       df.to_csv("BEVERAGES.csv")
               
                elif TYPE==3 :
                    if (os.path.isfile("SANCKS.csv")):
                       df2=pd.read_csv("SNACKS.csv",index_col=False)
                       df=pd.DataFrame(dic,index=[len(df2)+1])
                       df.to_csv("SNACKS.csv",mode="a",header=None)
                    else:
                       df=pd.DataFrame(dic,index=[1])
                       df.to_csv("SNACKS.csv")
                    
                elif TYPE==4 :
                    if (os.path.isfile("BREAKFAST DAIRY.csv")):
                       df2=pd.read_csv("BREAKFAST DAIRY.csv",index_col=False)
                       df=pd.DataFrame(dic,index=[len(df2)+1])
                       df.to_csv("BREAKFAST DAIRY.csv",mode="a",header=None)
                    else:
                       df=pd.DataFrame(dic,index=[1])
                       df.to_csv("BREAKFAST DAIRY.csv")
                      
                elif TYPE==5 :
                    if (os.path.isfile("KIDS.csv")):
                       df2=pd.read_csv("KIDS.csv",index_col=0)
                       df=pd.DataFrame(dic,index=[len(df2)+1])
                       df.to_csv("KIDS.csv",mode="a",header=None)
                    else:
                       df=pd.DataFrame(dic,index=[1])
                       df.to_csv("KIDS.csv")
                else:
                    print("WRONG CHOICE ENTERED FOR TYPE")
                    

                
            elif choice==2 :
                print("-------------------------------")
                print("MODIFY EXISTING PRODUCT DETAILS")
                print("-------------------------------")
                print("1.STAPLES")
                print("2.BEVERAGES")
                print("3.SNACKS")
                print("4.BREAKFAST AND DAIRY")
                print("5.BABY AND KIDS")
                TYPE=int(input("ENTER THE TYPE OF THE PRODUCT FROM THE ABOVE MENU :"))
                
                if TYPE==1:
                    c="STAPLES.csv"
                   
                elif TYPE==2:
                      c="BEVERAGES.csv"
                          
                elif TYPE==3:
                    c="SNACKS.csv"
                       
                elif TYPE==4:
                    c="BREAKFAST DAIRY.csv"
                        
                else :
                    c="KIDS.csv"

                df=pd.read_csv(c,index_col=0)
                print(df[["PRODUCT NAME","PRODUCT ID"]])
                pid=int(input("ENTER PRODUCT ID YOU WANT TO UPDATE :"))
                for i in range(1,len(df)+1) :
                    if  df["PRODUCT ID"][i]==pid:
                        print("YOUR RECORD HAS BEEN FOUND ")
                        op=int(input("PRESS 1 TO MAKE CHANGES IN PRODUCT NAME OR 0 TO RETAIN THE SAME VALUE : "))
                        if op==1:
                            cname=input("ENTER NEW PRODUCT NAME : ")
                            df.loc[i,"PRODUCT NAME"]=cname
                            df.to_csv(c)
                           
                        op=int(input("PRESS 1 TO MAKE CHANGES IN QUANTITY OR 0 TO RETAIN THE SAME VALUE : "))
                        if op==1 :
                            QUANTITY=int(input("ENTER NEW QUANTITY : "))
                            df.loc[i,"QUANTITY"]=QUANTITY
                            df.to_csv(c)
                        op=int(input("PRESS 1 TO MAKE CHANGES IN PRICE OR 0 TO RETAIN THE SAME VALUE : "))
                       
                        if op==1:
                            PRICE=input("ENTER NEW PRICE : ")
                            df.loc[i,"PRICE"]=PRICE
                            df.to_csv(c)
                        op=int(input("PRESS 1 TO MAKE CHANGES IN STOCK OR 0 TO RETAIN THE SAME VALUE : "))
                        
                        if op==1:
                            STOCK=input("ENTER UPDATED STOCK : ")
                            df.loc[i,"STOCK"]=STOCK
                            df.to_csv(c)
                        break
                        print("YOUR RECORD UPDATED SUCCESSFULLY")
                    
                else: 
                    print("NO RECORD FOUND")
                
            elif choice==3 :
                print("----------------")
                print("SEARCH A PRODUCT")
                print("----------------")
                print("1.STAPLES")
                print("2.BEVERAGES")
                print("3.SNACKS")
                print("4.BREAKFAST AND DAIRY")
                print("5.BABY AND KIDS")
                TYPE=int(input("ENTER THE TYPE OF THE PRODUCT FROM THE ABOVE MENU :"))

                if TYPE==1:
                    c="STAPLES.csv"
                   
                elif TYPE==2:
                      c="BEVERAGES.csv"
                          
                elif TYPE==3:
                    c="SNACKS.csv"
                       
                elif TYPE==4:
                    c="BREAKFAST DAIRY.csv"
                        
                elif TYPE==5:
                    c="KIDS.csv"
                    
                else :
                    print("WRONG CHOICE ENTERED")

                if TYPE in [1,2,3,4,5]:
                    
                    df=pd.read_csv(c,index_col=0)
                    print(df[["PRODUCT NAME","PRODUCT ID"]])
                    p_id=input("ENTER THE PRODUCT ID YOU WANT TO SEARCH : ")
                    print("")
                    
                    for i in range (1,len(df)+1):
                        if df["PRODUCT ID"][i]==eval(p_id):
                            print(df.loc[i])
                            
                            a=input("DO YOU WANT TO ADD THIS PRODUCT TO CART (Y/N): ")
                            if a=="Y" or a=="y":
                                c_id=df["PRODUCT ID"][i]
                                c_name=df["PRODUCT NAME"][i]
                                price=df["PRICE"][i]
                                quan=int(input("ENTER QUANTITY :"))
                                total=price*quan
                                dic={"PRODUCT ID":c_id,"PRODUCT NAME":c_name,"PRICE":price,"QUANTITY":quan,"TOTAL PRICE":total}
                                if (os.path.isfile("CART.csv")):
                                   df2=pd.read_csv("CART.csv",index_col=0)
                                   df=pd.DataFrame(dic,index=[len(df2)+1])
                                   df.to_csv("CART.csv",mode="a",header=None)
                                else:
                                   df=pd.DataFrame(dic,index=[1])
                                   df.to_csv("CART.csv")
                                print("------------------------------CART-------------------------------")
                                if (os.path.isfile("CART.csv")):
                                    df=pd.read_csv("CART.csv",index_col=0)
                                    print(df)
                                    print("TOTAL AMOUNT = ",df["TOTAL PRICE"].sum())
                                else:
                                    print("YOU HAVE NO ITEMS IN THE CART")
                                
                            elif a=="n" or a=="N":
                               print("")
                            else:
                                print("WRONG CHOICE ENTERED ")
                             
                            break
                    else:
                        print("NO MATCH FOUND")
                               
            elif choice==4 :
                print("")
                print("------------------")
                print("VIEW ALL PRODUCTS ")
                print("------------------")
                print("")
                print("1.STAPLES")
                print("2.BEVERAGES")
                print("3.SNACKS")
                print("4.BREAKFAST AND DAIRY")
                print("5.BABY AND KIDS")
                TYPE=int(input("ENTER THE TYPE OF THE PRODUCT FROM THE ABOVE MENU :"))

                if TYPE==1:
                    c="STAPLES.csv"
                   
                elif TYPE==2:
                      c="BEVERAGES.csv"
                          
                elif TYPE==3:
                    c="SNACKS.csv"
                       
                elif TYPE==4:
                    c="BREAKFAST DAIRY.csv"
                        
                elif TYPE==5:
                    c="KIDS.csv"
                    
                else :
                    print("WRONG CHOICE ENTERED")
                if TYPE in [1,2,3,4,5]:
                    df=pd.read_csv(c,index_col=0)
                    print("---------------------------")
                    print("DETAILS OF ALL THE PRODUCTS")
                    print("---------------------------")
                    print(df)
                    S=input("DO YOU WANT TO ADD A PRODUCT IN CART (Y/N) : ")
                    if S=="Y" or S=="y":
                        p_id=input("ENTER THE PRODUCT ID YOU WANT TO ADD TO CART: ")
                        print("")
                        for i in range (1,len(df)+1):
                            if df["PRODUCT ID"][i]==eval(p_id):
                                   c_id=df["PRODUCT ID"][i]
                                   c_name=df["PRODUCT NAME"][i]
                                   price=df["PRICE"][i]
                                   quan=int(input("ENTER QUANTITY :"))
                                   total=price*quan
                                   dic={"PRODUCT ID":c_id,"PRODUCT NAME":c_name,"PRICE":price,"QUANTITY":quan,"TOTAL PRICE":total}
                                   if (os.path.isfile("CART.csv")):
                                      df2=pd.read_csv("CART.csv",index_col=0)
                                      df=pd.DataFrame(dic,index=[len(df2)+1])
                                      df.to_csv("CART.csv",mode="a",header=None)
                                   else:
                                      df=pd.DataFrame(dic,index=[1])
                                      df.to_csv("CART.csv")
                                   print("------------------------------CART-------------------------------")
                                   if (os.path.isfile("CART.csv")):
                                       df=pd.read_csv("CART.csv",index_col=0)
                                       print(df)
                                       print("TOTAL AMOUNT = ",df["TOTAL PRICE"].sum())
                                   else:
                                       print("YOU HAVE NO ITEMS IN THE CART")
                                   break
                        else:
                            print("NO RECORD FOUND")
                    elif S=="n" or S=="N":
                        print("")
                    else:
                        print("WRONG CHOICE ENTERED ")

                                
            elif  choice==5 :
               print("----------------------")
               print("DELETE PRODUCT DETAILS")
               print("----------------------")
               print("")
               print("1.STAPLES")
               print("2.BEVERAGES")
               print("3.SNACKS")
               print("4.BREAKFAST AND DAIRY")
               print("5.BABY AND KIDS")
               TYPE=int(input("ENTER THE TYPE OF THE PRODUCT FROM THE ABOVE MENU :"))
               if TYPE==1:
                   c="STAPLES.csv"  
               elif TYPE==2:
                     c="BEVERAGES.csv"
               elif TYPE==3:
                   c="SNACKS.csv"
               elif TYPE==4:
                   c="BREAKFAST DAIRY.csv"
               elif TYPE==5:
                   c="KIDS.csv"
               else :
                   print("WRONG CHOICE ENTERED")

               if TYPE in [1,2,3,4,5]:
                   df=pd.read_csv(c,index_col=0)
                   print(df[["PRODUCT ID","PRODUCT NAME"]])
                   p_id=input("ENTER THE PRODUCT ID YOU WANT TO DELETE : ")
                   print("")
                   for i in range(1,len(df)+1) :
                       if  df["PRODUCT ID"][i]==eval(p_id):
                           df=df.drop([i])
                           df.index=range(1,len(df)+1)
                           df=df.to_csv(c)
                           print("PRODUCT SUCCESSFULLY DELETED")
                           break
                   else :
                       print("NO MATCH FOUND")
                
#--------------------------------------------------------------------------------------------#                             
        elif opt==3:
            print("")
            viewcart()
            
 
#----------------------------------------------------------------------------------------------#
        elif opt==4:
            print("1.VIEW ALL ORDER DETAILS")
            print("2.VIEW CUSTOMER ORDER DETAILS")
            ord=int(input("ENTER YOUR CHOICE FROM THE ABOVE MENU : "))
            if ord==1:
                df=pd.read_csv("ORDERS.csv",index_col=0)
                print("-------------------------ALL ORDERS-------------------------")
                print(df)
                
            elif ord==2:
                c_id=input("ENTER CUSTOMER ID YOU WANT THE DETAILS OF : ")
                df=pd.read_csv("ORDERS.csv",index_col=0)
                for i in range (1,len(df)+1):
                    if eval(c_id)==df["CUSTOMER_ID"][i]:
                        print("ORDER DETAILS FOUND")
                        print("--------------ORDER DETAILS--------------")
                        print(df.loc[i])
                        break
                else:
                    print("NO RECORD FOUND")
            else:
                print("WRONG CHOICE ENTERED")
            
                
#-----------------------------------------------------------------------------------------------#
        elif opt==5:
            print("----------")
            print("STATISTICS")
            print("----------")
            print("1. VIEW STAPLE CATEGORIES AND THIER NUMBER OF PRODUCTS")
            print("2. VIEW BEVERAGE CATEGORIES AND THIER NUMBER OF PRODUCTS")
            print("3. VIEW SNACKS CATEGORIES AND THIER NUMBER OF PRODUCTS")
            print("4. VIEW BREAKFAST ANS DAIRY CATEGORIES AND THIER NUMBER OF PRODUCTS")
            print("5. VIEW BABY AND KIDS PRODUCTS CATEGORIES AND THIER NUMBER OF PRODUCTS")
            csv=int(input("ENTER YOUR CHOICE FROM THE ABOVE MENU : "))
            if csv==1:
               df=pd.read_csv("STAPLES.csv",index_col=False)
               df1=df.groupby("CATEGORY").size()
               df1.plot(kind="bar",x="STAPLE CATEGORIES",y="NUMBER OF PRODUCTS",title="STAPLE CATEGORY V/S NUMBER OF PRODUCTS GRAPH",color="pink",edgecolor="black")
               plt.ylabel("NUMBER OF PRODUCTS")
               plt.xlabel("STAPLE CATEGORIES")
               plt.show()

            elif csv==2:
                df=pd.read_csv("BEVERAGES.csv",index_col=False)
                df1=df.groupby("CATEGORY").size()
                df1.plot(kind="bar",x="BEVERAGES CATEGORIES",y="NUMBER OF PRODUCTS",title="BEVERAGES CATEGORY V/S NUMBER OF PRODUCTS GRAPH",color="lightblue",edgecolor="black")
                plt.ylabel("NUMBER OF PRODUCTS")
                plt.xlabel("BEVERAGE CATEGORIES")
                plt.show()


            elif csv==3:
                df=pd.read_csv("SNACKS.csv",index_col=False)
                df1=df.groupby("CATEGORY").size()
                df1.plot(kind="bar",x="SNACKS CATEGORIES",y="NUMBER OF PRODUCTS",title="SNACKS CATEGORY V/S NUMBER OF PRODUCTS GRAPH",color="mediumpurple",edgecolor="black")
                plt.ylabel("NUMBER OF PRODUCTS")
                plt.xlabel("SNACKS CATEGORIES")
                plt.show()


            elif csv==4:
                df=pd.read_csv("BREAKFAST DAIRY.csv",index_col=False)
                df1=df.groupby("CATEGORY").size()
                df1.plot(kind="bar",x="BREAKFAST AND DAIRY PRODUCTS CATEGORIES",y="NUMBER OF PRODUCTS",title="BREAKFAST AND DAIRY PRODUCTS CATEGORY V/S NUMBER OF PRODUCTS GRAPH",color="lightgreen",edgecolor="black")
                plt.ylabel("NUMBER OF PRODUCTS")
                plt.xlabel("BREAKFAST AND DAIRY PRODUCTS CATEGORIES")
                plt.show()


            elif csv==5:
                df=pd.read_csv("KIDS.csv",index_col=False)
                df1=df.groupby("CATEGORY").size()
                df1.plot(kind="bar",x="BABY AND KIDS PRODUCTS CATEGORIES",y="NUMBER OF PRODUCTS",
                         title="BABY AND KIDS PRODUCTS CATEGORY V/S NUMBER OF PRODUCTS GRAPH",
                         color="lightcyan",edgecolor="black")
                plt.ylabel("NUMBER OF PRODUCTS")
                plt.xlabel("BABY AND KIDS PRODUCTS CATEGORIES")
                plt.show()

            else:
                print("PLEASE ENTER A VALID CHOICE")
            

#----------------------------------------------------------------------------------------------#
        elif opt==6:
            #BACK TO HOME PAGE
            break
                  
#----------------------------------------------------------------------------------------------#          
        else :
            print("WRONG CHOICE ENTERED FROM THE MAIN MENU")

###*****************************************admin window **********************************************
print("--------------------------------------")
print("--------------------------------------")
print(" WELCOME TO GROCERY MANAGEMENT SYSTEM ")
print("--------------------------------------")
print("--------------------------------------")

while (True):
    print("--------------------ADMIN MENU--------------------")
    print("1.SIGN IN")
    print("2.SIGN UP")
    print("3.LOG OUT")
    OPTION=int(input("ENTER YOUR CHOICE FROM THE ABOVE MENU : "))
    if(OPTION==1):
        user_id=input("ENTER YOUR USER ID : ")
        pss=input("ENTER PASSWORD : ")
        if (os.path.isfile("LOGIN_DETAILS.csv")):
            df=pd.read_csv("LOGIN_DETAILS.csv",index_col=False)
            for i in range (0,len(df)):
                if (df["ID"][i]==eval(user_id) and df["PASSWORD"][i]==pss) :
                    print("")
                    print("WELCOME BACK TO GROCERY MANAGEMENT SYSTEM")
                    input("PRESS ANY KEY TO DISPLAY THE MAIN MENU")
                    mainmenu()
                    break
            else :
                print("INVALID USERNAME OR PASSWORD ENTERED")
        else :
            print("ADMIN NOT REGISTERED !!! PLEASE REGISTER YOURSELF ")
    elif(OPTION==2):
        print("HELLO NEW USER WELCOME TO GROCERY STORE MANAGEMENT SYSTEM ")
        user_id=input("ENTER USER_ID : ")
        pss=input("ENTER PASSWORD : ")
        re_pss=input("CONFIRM YOUR PASSWORD AGAIN : ")
        if (pss==re_pss):
            name=input("ENTER YOUR NAME PLEASE : ")
            dob=input("ENTER YOUR DOB : ")
            gender=input("ENTER GENDER : ")
            phone_no=input("ENTER YOUR PHONE NUMBER : ")
            email_id=input("ENTER YOUR EMAIL ID : ")
            dic={"NAME":name,"ID":user_id,"PASSWORD":pss,"DOB":dob,"GENDER":gender,
                 "PHONE NO":phone_no,"EMAIL":email_id}
            if (os.path.isfile("LOGIN_DETAILS.csv")):
                df1=pd.read_csv("LOGIN_DETAILS.csv")
                df=pd.DataFrame(dic,index=[len(df1)])
                df.to_csv("LOGIN_DETAILS.csv",mode="a",header=None)
            else:
                df=pd.DataFrame(dic,index=[1])
                df.to_csv("LOGIN_DETAILS.csv")
            print("-------------------------------")
            print("YOU ARE SUCCESSFULLY REGISTERED")
            print("-------------------------------")
        else :
            print("PASSWORD DOESN'T MATCH")
            
    elif(OPTION==3):
        print("THANK YOU FOR USING OUR SYSTEM")
        break
