# 10% discount

purchase_value = float(input("Enter the product price: "))
coupon = input("Enter a coupon code: ")

if purchase_value >= 1000 or coupon == "PARTY":
    purchase_value = purchase_value * 0.9
else:
    print("Purchase without discount!!")

print("Your purchase will cost: {}".format(purchase_value))