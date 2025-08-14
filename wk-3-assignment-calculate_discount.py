# Step 1: Define the function
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Step 2: Get user input
original_price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Step 3: Calculate final price
final_price = calculate_discount(original_price, discount_percent)

# Step 4: Display the result
if discount_percent >= 20:
    print(f"Final price after discount: {final_price}")
else:
    print(f"No discount applied. Price remains: {final_price}")
    
#Stel 5: Expected Output:
Enter the original price: 1000
Enter the discount percentage: 25
Final price after discount: 750.0

Enter the original price: 1000
Enter the discount percentage: 10
No discount applied. Price remains: 1000.0
