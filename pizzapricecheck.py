print("Welcome to Python Pizza Deliveries!\n")

size = input("What size of pizza do you want? S M or L\n").upper()
add_pepperoni = input("Do you want peporoni?, Y or N\n").upper()
extra_cheese = input("Do you want extra cheese? Y or N\n").upper()

final_price = 15

if size == "S":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            final_price += 3
        else:
            final_price += 2
    else:
        if extra_cheese == "Y":
            final_price += 1
        else:
            final_price = final_price
elif size == "M":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            final_price += 4+5
        else:
            final_price += 3+5
    else:
        if extra_cheese == "Y":
            final_price += 1+5
elif size == "L":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            final_price += 4+10
        else:
            final_price += 3+10
    else:
        if extra_cheese == "Y":
            final_price += 1+10
else:
    print("Please enter the matching orders as per guide!")

print(f"Your final price of pizza is: {final_price}$.")
