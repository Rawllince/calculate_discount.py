def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        
        discount_amount = (price * discount_percent) / 100
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for the original price and discount percentage
try:
    original_price = float(input("Enter the original price: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Calculate the final price using the function
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Print the result
    if final_price < original_price:
        print(f"The final price after the discount is: ${final_price:.2f}")
    else:
        print(f"No discount was applied. The original price is: ${original_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numerical values for price and discount.")