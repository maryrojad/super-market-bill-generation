

name=input("Enter your name:")
#list of items
lists='''
Rice   RS 65/kg
oil    Rs 100/ltr 
dal    Rs 62/kg
pastes Rs 40/items 
soaps  Rs 90/pack 
'''
#declaration
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
plist=[]
qlist=[]

#rates for items
items={"rice":65,"oil":100,"dal":62,"pastes":40,"soaps":90}
option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter your qunatity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("Sorry you entered item is not avilable")    
else:
    print("you entered the wrong number")
inp=input("can i bill items yes or no:") 
if inp=='yes':
 pass
 if finalamount!=0:
  print(25*"=","Roja supermarket",25*"=")
print(25*"=","vizag",25*"=")
print("Name:",name,30*" ","import Datetime.now=datetime.now()")
print(75*"-")
print("sno",8*" ",'items',8*" ",'quantity',5*" ",'price')
for i in range(len(pricelist)):
            print(i,8*' ',8*' ',ilist[i],3*' ',qlist[i],plist[i])
print(75*"-")
print(50*" ",'Totalamount:','RS',totalprice)
print("gst amount",50*" ",'RS',gst)
print(75*"-")
print(50*" ",'FinalAmount:','RS',finalamount)
print(75*"-")
print(50*" ",'THANK YOU FOR VISITING',50*" ")
print(75*"-")


        

   
            
            
   

