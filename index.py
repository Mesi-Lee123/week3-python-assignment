print("enter the product price")
product_price=input()
print("enter the product discount")
discount=input()


def calculate_discount(price,discount_percent):
    
    if int(discount_percent) < 20:
        print("the price is" ,price)
    elif int(discount_percent) >= 20:
        discount_price=int(discount_percent)/100* int(price)
        print ("price after discount is", int(price) - discount_price)


calculate_discount(product_price,discount)