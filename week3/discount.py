def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price*(discount_percent/100)
        return(price-discount)
    else:
        return(price)
    

item_price = float(input("Enter price of item "))
discount = float(input("Enter discount percentage "))
final_price = calculate_discount(item_price, discount)

if discount<20:
    print(f"No discount applied\nFinal price = {item_price}")
else:
    print(f"The final discount for Kshs {item_price} at {discount}% discount is Kshs {final_price}")