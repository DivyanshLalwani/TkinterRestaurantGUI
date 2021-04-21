from tkinter import *
import tkinter.font as tkFont
def set_dpi_awareness():
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass
set_dpi_awareness()

root = Tk()
root.title("User")
root.geometry("600x400")

elementFont = tkFont.Font(family="Segoe UI", size=16, weight="bold")

available_tables = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

table1 = IntVar()
table2 = IntVar()
table3 = IntVar()
table4 = IntVar()
table5 = IntVar()
table6 = IntVar()
table7 = IntVar()
table8 = IntVar()
table9 = IntVar()
table10 = IntVar()
table11 = IntVar()
table12 = IntVar()
table13 = IntVar()
table14 = IntVar()
table15 = IntVar()
table16 = IntVar()
table17 = IntVar()

table_status = [table1, table2, table3, table4, table5, table6, table7, table8, table9, table10, table11, table12, table13, table14, table15, table16, table17]

AvailableTables = None
TableBooking = None
OrderScreen = None
BillWindow = None
ConsumerWindow = None
UpdateMenuWindow = None

def show_available_tables():
    global AvailableTables
    AvailableTables = Toplevel()
    AvailableTables.title("Available Tables")
    Label(AvailableTables, text="1-10: 2-seaters\n11-15: 4-seaters\n16-17: 10-seaters\nAvailable Seats:", font=elementFont).grid(row=0, column=0)
    for table in available_tables:
        if table_status[table-1].get() == 0:
            Label(AvailableTables, text=str(table)).grid(row=table, column=0)
        else:
            pass

def confirm_book_tables():
    global TableBooking
    global AvailableTables
    TableBooking.destroy()
    AvailableTables.destroy()
    show_available_tables()

def book_tables():
    global TableBooking
    global table_checkboxes
    TableBooking = Toplevel()
    TableBooking.title("Tables")

    Label(TableBooking, text="2-seaters\navailable", font=elementFont).grid(row=0, column=0)
    Checkbutton(TableBooking, text=f"Table 1", variable=table1).grid(row=1, column=0)
    Checkbutton(TableBooking, text=f"Table 2", variable=table2).grid(row=2, column=0)
    Checkbutton(TableBooking, text=f"Table 3", variable=table3).grid(row=3, column=0)
    Checkbutton(TableBooking, text=f"Table 4", variable=table4).grid(row=4, column=0)
    Checkbutton(TableBooking, text=f"Table 5", variable=table5).grid(row=5, column=0)
    Checkbutton(TableBooking, text=f"Table 6", variable=table6).grid(row=6, column=0)
    Checkbutton(TableBooking, text=f"Table 7", variable=table7).grid(row=7, column=0)
    Checkbutton(TableBooking, text=f"Table 8", variable=table8).grid(row=8, column=0)
    Checkbutton(TableBooking, text=f"Table 9", variable=table9).grid(row=9, column=0)
    Checkbutton(TableBooking, text=f"Table 10", variable=table10).grid(row=10, column=0)

    Label(TableBooking, text="4-seaters\navailable", font=elementFont).grid(row=0, column=1)
    Checkbutton(TableBooking, text=f"Table 11", variable=table11).grid(row=1, column=1)
    Checkbutton(TableBooking, text=f"Table 12", variable=table12).grid(row=2, column=1)
    Checkbutton(TableBooking, text=f"Table 13", variable=table13).grid(row=3, column=1)
    Checkbutton(TableBooking, text=f"Table 14", variable=table14).grid(row=4, column=1)
    Checkbutton(TableBooking, text=f"Table 15", variable=table15).grid(row=5, column=1)

    Label(TableBooking, text="10-seaters\navailable", font=elementFont).grid(row=0, column=2)
    Checkbutton(TableBooking, text=f"Table 16", variable=table16).grid(row=1, column=2)
    Checkbutton(TableBooking, text=f"Table 17", variable=table17).grid(row=2, column=2)

    confirm_tables = Button(TableBooking, text="Confirm Table(s)", command=confirm_book_tables)
    confirm_tables.grid(row=11, column=1)

# format: type_of_food = [[Item, Price], [Item, Price]]
foods = [["Pizza", 12], ["Hamburger", 10], ["Noodles", 11]]
drinks = [["Coffee", 5], ["Tea", 3], ["Juice", 10], ["Milkshake", 8]]
total_items = foods + drinks
total_sales = 0

int_quantity_list = []

def quit_consumer():
    global AvailableTables
    global TableBooking
    global OrderScreen
    global BillWindow
    global ConsumerWindow
    try:
        AvailableTables.destroy()
    except:
        pass
    try:
        TableBooking.destroy()
    except:
        pass
    try:
        OrderScreen.destroy()
    except:
        pass
    try:
        BillWindow.destroy()
    except:
        pass
    try:
        ConsumerWindow.destroy()
    except:
        pass

def billing():
    global foods
    global drinks
    global total_items
    global total_sales
    global BillWindow

    total_items = foods + drinks

    BillWindow = Toplevel()
    BillWindow.title("Bill")
    BillWindow.geometry("600x400")
    RestaurantLabel = Label(BillWindow, text="Restaurant La Ratatoulie", font=elementFont)
    RestaurantLabel.grid(row=0, column=1)

    Label(BillWindow, text="Item", font=elementFont).grid(row=2, column=0)
    Label(BillWindow, text="Price", font=elementFont).grid(row=2, column=1)
    Label(BillWindow, text="Quantity", font=elementFont).grid(row=2, column=2)
    Label(BillWindow, text="Charged\nPrice", font=elementFont).grid(row=2, column=3)

    total_cost = 0

    r = 3
    for item in total_items:
        Label(BillWindow, text=item[0]).grid(row=r, column=0)
        Label(BillWindow, text=f"${str(item[1])}").grid(row=r, column=1)
        quantity = (item[2]).get()
        Label(BillWindow, text=quantity).grid(row=r, column=2)
        cost = item[1]*int(quantity)
        Label(BillWindow, text=f"${str(cost)}").grid(row=r, column=3)
        total_cost += cost
        r += 1

    total_sales += total_cost
    Label(BillWindow, text="Total Cost", font=elementFont).grid(row=r, column=0)
    Label(BillWindow, text=f"${str(total_cost)}", font=elementFont).grid(row=r, column=3)
    Button(BillWindow, text="Confirm & Quit", command=quit_consumer, width=20).grid(row=r+1, column=2)

def ordering():
    global foods
    global drinks
    global total_items
    global OrderScreen

    total_items = []
    for each_food in foods:
        try:
            each_food.remove([each_food[2]])
        except:
            pass
    for each_drink in drinks:
        try:
            each_drink.remove([each_food[2]])
        except:
            pass

    print(foods)
    print(drinks)

    OrderScreen = Toplevel()
    OrderScreen.title("Order Food and Drinks")
    OrderScreen.geometry("700x400")

    food_frame = Frame(OrderScreen)
    food_frame.grid(row=0, column=0)

    Label(food_frame, text="Food\nItem", font=elementFont).grid(row=0, column=0)
    Label(food_frame, text="Price\n(in $)", font=elementFont).grid(row=0, column=1)
    Label(food_frame, text="Quantity", font=elementFont).grid(row=0, column=2)

    x = 1
    for food in foods:
        y = 0
        Label(food_frame, text=food[0]).grid(row=x, column=y)
        Label(food_frame, text=f"${str(food[1])}").grid(row=x, column=y+1)

        food_quantity_entry = Entry(food_frame)
        food_quantity_entry.grid(row=x, column=y+2)
        try:
            if food[2] == True:
                food.remove(food[2])
                food.append(food_quantity_entry)
        except:
            food.append(food_quantity_entry)
        print(foods)
        x += 1

    drink_frame = Frame(OrderScreen)
    drink_frame.grid(row=0, column=1)
    Label(drink_frame, text="Drink", font=elementFont).grid(row=0, column=0)
    Label(drink_frame, text="Price\n(in $)", font=elementFont).grid(row=0, column=1)
    Label(drink_frame, text="Quantity", font=elementFont).grid(row=0, column=2)
    for drink in drinks:
        y = 0

        Label(drink_frame, text=drink[0]).grid(row=x, column=y)
        Label(drink_frame, text=f"${str(drink[1])}").grid(row=x, column=y+1)

        drink_quantity_entry = Entry(drink_frame)
        drink_quantity_entry.grid(row=x, column=y+2)
        try:
            if drink[2] == True:
                drink.remove(drink[2])
                drink.append(drink_quantity_entry)
        except:
            drink.append(drink_quantity_entry)
        print(drinks)
        x += 1

    total_items = foods + drinks
    confirm_order = Button(OrderScreen, text="Confirm Order", command=billing)
    confirm_order.place(relx=.5, rely=.5, anchor='center')

def open_cust_window():
    global ConsumerWindow
    CustomerWindow = Toplevel()
    CustomerWindow.title("Customer")
    CustomerWindow.geometry("500x200")
    available_table_list = Button(CustomerWindow, text="Available Tables", command=show_available_tables)
    available_table_list.pack()
    book_tables_button = Button(CustomerWindow, text="Book Tables", command=book_tables)
    book_tables_button.pack()
    order_button = Button(CustomerWindow, text="Place Order", command=ordering)
    order_button.pack()

def update_menu():
    global UpdateMenuWindow
    global foods
    global drinks

    UpdateMenuWindow = Toplevel()
    UpdateMenuWindow.title("Update Menu Window")
    UpdateMenuWindow.geometry("300x200")

    def update_food():
        global foods
        global total_items
        UpdateFoodWindow = Toplevel()
        UpdateFoodWindow.title("Update Food Window")
        UpdateFoodWindow.geometry("300x200")

        def confirm_food_update():
            global foods
            foods.append([new_food_item.get(), int(new_food_price.get())])
            print(foods)
            UpdateFoodWindow.destroy()

        Label(UpdateFoodWindow, text="Food Item: ").grid(row=0, column=0)
        new_food_item = Entry(UpdateFoodWindow)
        new_food_item.grid(row=0, column=1)
        Label(UpdateFoodWindow, text="Price:\n(in $) ").grid(row=1, column=0)
        new_food_price = Entry(UpdateFoodWindow)
        new_food_price.grid(row=1, column=1)
        Button(UpdateFoodWindow, text="Confirm Update", command=confirm_food_update).grid(row=2, column=1)

    def update_drink():
        global drinks
        UpdateDrinkWindow = Toplevel()
        UpdateDrinkWindow.title("Update Drink Window")
        UpdateDrinkWindow.geometry("300x200")

        def confirm_drink_update():
            global drinks
            drinks.append([new_drink_item.get(), int(new_drink_price.get())])
            print(drinks)
            UpdateDrinkWindow.destroy()

        Label(UpdateDrinkWindow, text="Drink Item: ").grid(row=0, column=0)
        new_drink_item = Entry(UpdateDrinkWindow)
        new_drink_item.grid(row=0, column=1)
        Label(UpdateDrinkWindow, text="Price:\n(in $) ").grid(row=1, column=0)
        new_drink_price = Entry(UpdateDrinkWindow)
        new_drink_price.grid(row=1, column=1)
        Button(UpdateDrinkWindow, text="Confirm Update", command=confirm_drink_update).grid(row=2, column=1)

    total_items = foods + drinks

    Button(UpdateMenuWindow, text="Update Food Items", command=update_food).pack()
    Button(UpdateMenuWindow, text="Update Drink Items", command=update_drink).pack()


def display_total_sales():
    TotalSales =Toplevel()
    global total_sales
    Label(TotalSales, text=str(total_sales)).pack()

def open_ad_window():
    AdminWindow = Toplevel()
    AdminWindow.title("Admin")
    AdminWindow.geometry("600x400")

    Label(AdminWindow, text="Admin").pack()
    Button(AdminWindow, text="Change Table Status", command=book_tables).pack()

    Button(AdminWindow, text="Change Menu", command=update_menu).pack()

    Button(AdminWindow, text="Total Sales", command=display_total_sales).pack()

def admin_login():
    LoginWindow = Toplevel()
    LoginWindow.title("Admin Login")

    actual_username = "admin"
    actual_password = "12345"

    Label(LoginWindow, text="Username: ").grid(row=0, column=0)
    username_entry = Entry(LoginWindow)
    username_entry.grid(row=0, column=1)

    Label(LoginWindow, text="Password: ").grid(row=1, column=0)
    password_entry = Entry(LoginWindow, show="•")
    password_entry.grid(row=1, column=1)

    def confirm_login():
        if username_entry.get() == "admin" and password_entry.get() == "12345":
            Label(LoginWindow, text="Access Granted").grid(row=3, column=1)
            LoginWindow.destroy()
            open_ad_window()
        else:
            Label(LoginWindow, text="Access Denied").grid(row=3, column=1)
            LoginWindow.destroy()

    Button(LoginWindow, text="Confirm Login", command=confirm_login, width=20).grid(row=2, column=1)

Label(root, text="User").pack()
customer_button = Button(root, text="Customer", command=open_cust_window)
customer_button.pack()
admin_button = Button(root, text="Admin", command=admin_login)
admin_button.pack()

root.mainloop()
