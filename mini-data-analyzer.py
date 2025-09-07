def add_new_product(date, product, quantity, price):
    with open("salesdata.txt", "a") as file:
        file.write(f"{date},{product},{quantity},{price}\n")
    print("Product has been added successfully.")


def product_total_sales(product):
    with open("salesdata.txt", "r") as file:
        lines = file.readlines()
    total_sales = 0
    found = False
    for i in range(1, len(lines)):
        row = lines[i].strip().split(",")
        if row[1] == product:
            revenue = int(row[2]) * int(row[3])
            total_sales += revenue
            found = True

    if not found:
        print("No sales found for", product)
    else:
        print(f"Total sales of {product} is {total_sales}")


def date_total_sales(date):
    with open("salesdata.txt", "r") as file:
        lines = file.readlines()

    total_sales = 0
    for i in range(1, len(lines)):
        row = lines[i].strip().split(",")
        if row[0] == date:
            revenue = int(row[2]) * int(row[3])
            total_sales += revenue

    print(f"Total sales for {date} is {total_sales}")


def highest_and_lowest_sales_day():
    with open("salesdata.txt", "r") as file:
        lines = file.readlines()

    sales_by_date = {}
    for i in range(1, len(lines)):
        row = lines[i].strip().split(",")
        date, quantity, price = row[0], int(row[2]), int(row[3])
        revenue = quantity * price
        sales_by_date[date] = sales_by_date.get(date, 0) + revenue

    if not sales_by_date:
        print("No sales data available.")
        return

    highest_day = max(sales_by_date, key=sales_by_date.get)
    lowest_day = min(sales_by_date, key=sales_by_date.get)

    print(f"Highest sales day: {highest_day} with revenue {sales_by_date[highest_day]}")
    print(f"Lowest sales day: {lowest_day} with revenue {sales_by_date[lowest_day]}")


def highest_and_lowest_selling_product():
    with open("salesdata.txt", "r") as file:
        lines = file.readlines()

    product_sales = {}
    for i in range(1, len(lines)):
        row = lines[i].strip().split(",")
        product, quantity = row[1], int(row[2])
        product_sales[product] = product_sales.get(product, 0) + quantity

    if not product_sales:
        print("No product sales data available.")
        return

    sorted_products = dict(sorted(product_sales.items(), key=lambda x: x[1], reverse=True))
    products_list = list(sorted_products.keys())

    print(f"Highest sold product: {products_list[0]} with quantity {sorted_products[products_list[0]]}")
    print(f"Lowest sold product: {products_list[-1]} with quantity {sorted_products[products_list[-1]]}")


def sales_on_minimum_amount(amount):
    with open("salesdata.txt", "r") as file:
        lines = file.readlines()

    found = False
    for i in range(1, len(lines)):
        row = lines[i].strip().split(",")
        date, quantity, price = row[0], int(row[2]), int(row[3])
        revenue = quantity * price
        if revenue >= amount:
            print(f"On {date}, sales amount was {revenue}")
            found = True

    if not found:
        print(f"No date found with sales >= {amount}")


def total_sales():
    with open("salesdata.txt", "r") as file:
        lines = file.readlines()

    total_revenue = 0
    for i in range(1, len(lines)):
        row = lines[i].strip().split(",")
        total_revenue += int(row[2]) * int(row[3])

    print("Total sales revenue is", total_revenue)


def show_menu():
    print("\n===== Sales Data Analyzer =====")
    print("1. Add new product sales")
    print("2. Analyze total sales of a product")
    print("3. Show total sales of a date")
    print("4. Show highest and lowest sales day")
    print("5. Show highest and lowest sold product")
    print("6. Show sales on minimum amount")
    print("7. Show total sales revenue")
    print("8. Exit")
    return input("Enter your choice: ")


while True:
    choice = show_menu()

    if choice == "1":
        date = input("Enter the date: ")
        product = input("Enter the product: ")
        quantity = input("Enter the quantity sold: ")
        price = input("Enter the price of the product: ")
        add_new_product(date, product, quantity, price)

    elif choice == "2":
        product = input("Enter the product: ")
        product_total_sales(product)

    elif choice == "3":
        date = input("Enter the date: ")
        date_total_sales(date)

    elif choice == "4":
        highest_and_lowest_sales_day()

    elif choice == "5":
        highest_and_lowest_selling_product()

    elif choice == "6":
        amount = int(input("Enter the minimum amount: "))
        sales_on_minimum_amount(amount)

    elif choice == "7":
        total_sales()

    elif choice == "8":
        print("Thanks for using Sales Data Analyzer!")
        break

    else:
        print("Invalid choice. Please try again.")


