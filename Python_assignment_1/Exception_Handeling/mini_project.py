
'''
MINI PROJECT
You had saved the items and their pricedetails in a text file,which you purchased yesterday from a nearby super market.

 You need to know:
 1.How many items did you purchase?
 2.How many itemsarefree?
 3.What is the total amount you had to pay?
 4.What is the discount amount?
 5.What is the final amount did you payafter the discount?
 
 Help yourself by writing a python code to do this.Include necessary code to handle the possible exceptions.
 Note:Data is stored in a text file Purchase-1.txt.
 Each line contains oneitem’s details.
 Item name and price isseparated by a space.
 You have to enter the file name during run time.
 Sample input1:Purchase-1.txtChocolate 50Biscuit 35
Icecream 50(blank line)Discount  5
'''

try:
    filename = input("Enter the file name: ").strip() + ".txt"
    with open(filename, 'r') as file:
        lines = file.readlines()

    total_items = 0
    free_items = 0
    total_amount = 0
    discount = 0
    is_discount_section = False

    for line in lines:
        line = line.strip()
        if line == "":
            is_discount_section = True
            continue
        if is_discount_section:
            if line.lower().startswith("discount"):
                try:
                    discount = int(line.split()[-1])
                except ValueError:
                    discount = 0
        else:
            parts = line.split()
            if len(parts) < 2:
                continue
            item = parts[0]
            price = parts[1]
            if price.lower() == "free":
                free_items += 1
            else:
                try:
                    total_amount += int(price)
                    total_items += 1
                except ValueError:
                    pass  # skip invalid lines

    final_amount = total_amount - discount

    print("No of items purchased:", total_items)
    print("No of free items:", free_items)
    print("Amount to pay:", total_amount)
    print("Discount given:", discount)
    print("Final amount paid:", final_amount)

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An unexpected error occurred:", e)
