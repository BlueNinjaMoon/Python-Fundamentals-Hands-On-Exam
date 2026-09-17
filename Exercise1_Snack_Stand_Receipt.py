#Christian Lehman

name = input("Enter your name: ").strip().title()
snack = input("Enter name of snack: ").strip().title()
snkprice = input("Enter the snack price: ").strip()
if snkprice.isdigit() == True:
    snkprice = int(snkprice)
elif snkprice.count(".") == 1:
    snkprice = float(snkprice)
else:
    print("Inavlid snack price.")
snkquantity = input("Enter the quantity of the snack: ").strip()
if snkquantity.isdigit() == True:
    snkquantity = int(snkquantity)
else:
    print("Inavlid snack quantity.")
subtotal = (snkprice)*(snkquantity)
if subtotal >= 10:
    discount1 = 10%subtotal
    discount = subtotal - discount1
else:
    discount = 0

print(f"Customer: {name}")
print(f"Snack: {snack}")
print(f"Quantity: {snkquantity}")
print(f"Subtotal: ${subtotal}")
print(f"Discount: ${discount1}")
print(f"Final Total: ${discount}")