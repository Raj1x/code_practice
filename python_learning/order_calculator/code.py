def calculate_order(price, discount):
    if discount == "Raj1x":
        price = price * 0.9
    else:
        print("Price stays without any changes!")
    if price >= 150:
        delivery_cost = 0
    elif price < 150:
        delivery_cost = 20

    return price, delivery_cost

product_price = int(input("How much does the product cost?: "))
discount_code = input("Type discount code: ")

price_after_discount, delivery_cost = calculate_order(product_price, discount_code)

price_to_pay = price_after_discount + delivery_cost

print(f"- Delivery cost = {delivery_cost}")
print(f"- To pay: {price_to_pay} $, (In it product: {price_after_discount})")
