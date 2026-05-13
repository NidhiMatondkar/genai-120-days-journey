mobile =[]
n = int(input("Enter no of mobiles:"))
for i in range(n):
    Brand = input("Enter Brand name:").strip()
    price = int(input("Enter Price :"))
    phone = {"Brand":Brand,
         "Price":price
         }
    mobile.append(phone)
print(mobile)


found = False
name = input("Enter brand name:")
for phone in mobile:
    if phone["Brand"] == name:
         print(f"Brand: {phone['Brand']} | Price: {phone['Price']}")
         found = True
         break
if not found:
   print("Brand not found")

