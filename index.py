


menu_Mastery =[]
orders = []
def Display_Menu():
    if not menu_Mastery:
        print("No dish available in the zomato menu.")
        print("---------------------------------------")
    else:
        print("Zomato Menu...")  
        print("ID  |  Name  |  Price  | Stock | Availability")
        for dish in menu_Mastery:
            print(f"{dish['id']:3} | {dish['name']:6} | {dish['price']:7.2f} | {dish['stock']}     | {dish['availability']}"
            )

def Add_Dish():
    dish = {}
    dish["id"] = int(input("Enter the Dish ID: "))
    dish["name"] = input("Enter the Dish name: ")
    dish["price"] = float(input("Enter the Dish price: "))
    dish["stock"] = int(input("Enter the Dish stock: "))
    if dish["stock"] <= 0:
        dish['availability'] = 'no'
    else:
        dish['availability'] = 'yes'
    menu_Mastery.append(dish)
    print("Dish added successfully.")
1
def Remove_Dish():
    dish_id =  int(input("Enter the dish ID to remove: "))   
    for dish in menu_Mastery:
        if dish["id"]==dish_id:
            menu_Mastery.remove(dish)   
            print("Dish removed successfully.")
            return
    print("dish not found.")


def Update_Dish_Stock():
    dish_id =  int(input("Enter the dish ID to update: ")) 
    for dish in menu_Mastery:
        if dish["id"]==dish_id:
            dish["stock"] =  int(input("Enter the updated stock: ")) 
            print("Dish stock updated successfully.")
            return
    print("dish not found.")


def take_new_order():
    customer_name = input("Enter customer name: ")
    dish_ids = input("Enter dish IDs (separated by commas): ").split(",")
    dish_ids = [int(dish_id.strip()) for dish_id in dish_ids]

    for dish_id in dish_ids:
        dish_available = False
        for dish in menu_Mastery:
            if dish["id"] == dish_id and dish["availability"] == "yes" and dish["stock"] > 0:
                dish_available = True
                dish["stock"] -= 1
                if dish["stock"]<=0:
                    dish["availability"] = "no"
                break

        if not dish_available:
            print(f"Dish with ID {dish_id} is not available.")
            return

    order_id = len(orders) + 1
    order_bill = sum([dish["price"] for dish in menu_Mastery if dish["id"] in dish_ids])

    order = {
        "order_id": order_id,
        "customer_name": customer_name,
        "dish_ids": dish_ids,
        "status": "received",
        "order_bill": order_bill
    }

    orders.append(order)
    print(f"Order placed successfully. Order ID is {order_id}.")

def update_order_status():
    order_id = int(input("Enter the order ID to update status: "))
    status = input("Enter the new status: ")

    for order in orders:
        if order["order_id"] == order_id:
            order["status"] = status
            print("Order status updated.")
            return

    print("Order not found.")

def review_orders():
    for order in orders:
        print(f"Order ID: {order['order_id']}")
        print(f"Customer Name: {order['customer_name']}")
        print(f"Dish IDs: {order['dish_ids']}")
        print(f"Status: {order['status']}")
        print(f"Order Bill: {order['order_bill']}")
        print("-------------------------")



def main():
    while True:
        print("\n===== Zomato Chronicles: The Great Food Fiasco =====")
        print("1. Display Menu")
        print("2. Add Dish to Menu")
        print("3. Remove Dish from Menu")
        print("4. Update Dish stock")
        print("5. Take New Order")
        print("6. Update Order Status")
        print("7. Review Orders")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            Display_Menu()
        elif choice == '2':
            Add_Dish()
        elif choice == '3':
           Remove_Dish()
        elif choice == '4':
            Update_Dish_Stock()
        elif choice == '5':
            take_new_order()
        elif choice == '6':
            update_order_status()
        elif choice == '7':
            review_orders()
        elif choice == '8':
            print("Thank you for using Zomato Chronicles. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()