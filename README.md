# TkinterRestaurantGUI
A simple GUI built using Python and the Tkinter module to provide a simple interface for dine-in customers to select tables and order from the menu in a restaurant. This also allows the restaurant operators (admins) to see which tables are occupied and generate itemised bills for the orders of the specific tables.  

Note: 
1. All intra-code explanations are given as comments starting with “#” symbol and highlighted in blue. 
2. String concatenation is mostly implemented using f-string literals which require operating Python interpreter versions to be greater than 3.6. 
1. Objective 
To design a Graphical User Interface for a restaurant owner to ease customer and administrator side operations. 
2. Tasks to accomplish 
a. Plan the interface 
b. Designing the structure of the interface 
c. Choosing a framework for implementation 
d. Designing the interface 
e. Program Design 
f. Customer-side operations: 
i. Check for available tables 
ii. Book tables 
iii. Place orders 
iv. Receive bills 
g. Admin-side operations 
i. Check for available tables 
ii. Change table status(occupied/vacant) 
iii. Update menu 
iv. Check total sales 
3. Planning 
a. Planning the interface 
The interface should be: 
● Easy to use
● Chronological in approach(customers or admins 
shouldn’t be allowed to skip entering necessary details) 
Two possible approaches to designing the interface: 
1. To use separate windows for each function. 
2. To use separate frames for each function all on the same window. 
The approach chosen was the first one, to use several windows for three primary reasons: 
1. For easier segregation of functionality 
2. For reduced congestion, hence greater aesthetic appeal. 3. For easier validation and verification of previously entered values(the user would not be allowed to move to the next window until the necessary details on the current window are entered) 
b. Structure of the interface 
Since the program was to use separate windows for each of the functions listed in Tasks to accomplish, each window had to be designed separately. 
Windows used: 
Parent windows are in greater indentation than children windows. 1. User 
a. Customer 
i. Available Tables 
ii. Book Tables 
iii. Place Order 
iv. Bill 
b. Admin 
i. Admin Login 
ii. Update Table Status 
iii. Update Menu 
1. Update Food 
2. Update Drink 
c. Choosing a framework for development 
The question of the right GUI framework boils down to Tkinter and PyQt5.
Assessment of the advantages and disadvantages were made after reading this blog .1 
Advantages of using Tkinter include(refer to the blog post for elaborated reasoning): 
1. No royalties or intellectual property infringement 
2. Ease of creating executables due to lack of dependencies 3. Simpler to understand and master 
4. Existence of all widgets to create the program at hand 
d. Designing the interface 
The design was kept to be minimalistic with no extra graphics to avoid possible sources of confusion or distraction. 
Every window except the Book Tables window only had buttons. Book Tables had checkboxes. 
Program Design 
The entire program is function-dependendent. Functions ensure reusability of code, and make adding updates easier and more general. 
Functions used: 
General: 
1. set_dpi_awareness() 
Customer Side: 
1. open_cust_window() 
2. show_available_tables() 
3. book_tables() 
4. confirm_book_tables() 
5. ordering() 
6. billing() 
7. quit_customer() 
Admin Side: 
1. open_ad_window() 
2. admin_login() 
3. book_tables() 
4. update_menu() 
a. update_food() 
1 Amigos-Maker. “Python GUI, PyQt vs TKinter.” DEV Community, DEV Community, 22 May 2020, dev.to/amigosmaker/python-gui-pyqt-vs-tkinter-5hdd.
b. upadte_drink() 
5. display_total_sales() 
Global variables used: 
1. AvailableTables 
2. TableBooking 
3. OrderScreen 
4. BillWindow 
5. ConsumerWindow 
6. UpdateMenuWindow 
7. foods 
8. drinks 
9. available_tables 
In Tkinter, all button widgets have to be specified with a “command” parameter which specifies the function that runs whenever the button is clicked 
User Window: 
Customer Window: 
Admin Window:


Admin Login: 
Login Details: Username: admin Password: 12345 


Since the function open_ad_window() only runs if the details are entered correctly, there is no way of bypassing the login. 
The password entry widget has the specified “show” parameter which enables entered characters to be concealed by a “•”. 
Table Booking and Updating Table Status(Admin and customer side): 
Out of the many ways that could have been implemented to input the required tables, the one enabling checkbox widgets to be checked to select a table was chosen. This was done to avoid any validation errors or type check errors that come with text entry widgets, of the unnecessary multiplicity of entering each table one at a time with a drop down menu. With a checkbox, table status is easier to be changed dynamically, and the user can select or deselect multiple tables at once.

Once “Confirm Table(s)” is clicked a window showing all the currently available windows is displayed, and has removed all of the tables previously selected. If a table gets cleared, the admin can just deselect the checkbox of that particular table and the status of the table will return to vacant(unchecked). 
>> Images above show the tables now available after the tables in the Book Tables window image above were selected. As visible, tables 3, 5, 7, 13, 14, 16, 17 are not available. 
This is the code implementing the AvailableTables window: 
def show_available_tables(): 
 global AvailableTables 
 AvailableTables = Toplevel() #creating new window  AvailableTables.title("Available Tables") 
 Label(AvailableTables, text="1-10: 2-seaters\n11-15: 4-seaters\n16-17: 10-seaters\nAvailable Seats:", font=elementFont).grid(row=0, column=0) #indexing the numbers of the tables by the number of seats. 
# available_tables contains all the table variables from the checkboxes of the Book Tables window. If a table is available, then it will have a value of 0 (unchecked), else, it is occupied. 
 for table in available_tables: 
 if table_status[table-1].get() == 0: 
 Label(AvailableTables, 
text=str(table)).grid(row=table, column=0) 
 else: 
 pass
Ordering(Customer-side): 
Code executing the Food Item, corresponding Price and Quantity columns: (code is explained in comments) 
OrderScreen = Toplevel() # creating a new window OrderScreen.title("Order Food and Drinks") 
OrderScreen.geometry("700x400") 
Ordering window is divided into two frames: Foods and Drinks. Each frame contains the item listed, its price and the quantity demanded by the customer. 
food_frame = Frame(OrderScreen)# creating frame for foods food_frame.grid(row=0, column=0) 
Label(food_frame, text="Food\nItem", 
font=elementFont).grid(row=0, column=0) # labelling headings Label(food_frame, text="Price\n(in $)", 
font=elementFont).grid(row=0, column=1) 
Label(food_frame, text="Quantity", 
font=elementFont).grid(row=0, column=2) 
x = 1 
for food in foods: 
# foods is a global list containing all the food items on the menu; it is in the format: 
[[Item_name, Price, Quantity], [Item_name, Price, Quantity]] # this for loop iterates through each one of these lists inside foods and labels each item, its price and quantity demanded on the same row(hence the same variable, x) and different columns(y increasing by one for each label and entry)
 y = 0 
 Label(food_frame, text=food[0]).grid(row=x, column=y)  Label(food_frame, text=f"${str(food[1])}").grid(row=x, column=y+1) 
 food_quantity_entry = Entry(food_frame) 
 food_quantity_entry.grid(row=x, column=y+2)  try: 
# checking if there is a pre-existing quantity for the particular food item; if there is, it needs to be removed and updated with the new quantity from the entry. 
 if food[2] == True: 
 food.remove(food[2]) 
 food.append(food_quantity_entry) 
 except: 
 food.append(food_quantity_entry) 
 print(foods) 
 x += 1 
● Variables x, y are used as positioning coordinates for the .grid() method being used to place the items on the window. 
Billing(for the order shown above; customer-side): 
def billing(): 
 global foods 
 global drinks 
 global total_items 
 global total_sales 
 global BillWindow
 # total_items is a compiled list of all the items on the menu and their corresponding prices and quantities demanded by the customer 
 total_items = foods + drinks 
 BillWindow = Toplevel() # creating a window for the bill  BillWindow.title("Bill") 
 BillWindow.geometry("600x400") 
 RestaurantLabel = Label(BillWindow, text="Restaurant La Ratatouille", font=elementFont) 
 RestaurantLabel.grid(row=0, column=1) 
# bill has 4 columns: Item, Price, Quantity, Charged Price #labelled and placed on grid here: 
 Label(BillWindow, text="Item", 
font=elementFont).grid(row=2, column=0) 
 Label(BillWindow, text="Price", 
font=elementFont).grid(row=2, column=1) 
 Label(BillWindow, text="Quantity", 
font=elementFont).grid(row=2, column=2) 
 Label(BillWindow, text="Charged\nPrice", 
font=elementFont).grid(row=2, column=3) 
 total_cost = 0 
 r = 3 
# since foods list is added first, food element details appear first in total_items and are hence labelled first, this removes the nuisance of recently added food items getting billed after drinks, hence maintaining order  for item in total_items: 
 Label(BillWindow, text=item[0]).grid(row=r, column=0)  Label(BillWindow, text=f"${str(item[1])}").grid(row=r, column=1) 
 quantity = (item[2]).get() 
 Label(BillWindow, text=quantity).grid(row=r, column=2)  # charged cost is calculated as price * quantity:  cost = item[1]*int(quantity) 
 Label(BillWindow, text=f"${str(cost)}").grid(row=r, column=3) 
 total_cost += cost 
 r += 1
Updating Menu(Admin-side): 

Updating food items(Admin-side): 

def update_menu(): 
 global UpdateMenuWindow 
 global foods 
 global drinks 
 UpdateMenuWindow = Toplevel()# creating a new window  UpdateMenuWindow.title("Update Menu Window")  UpdateMenuWindow.geometry("300x200") 
 # update_menu() has two main functions: update_food() and update_drink for foods and drinks correspondingly. The idea is that with update_food(), the foods list will be updated,  def update_food(): 
 global foods 
 global total_items 
 UpdateFoodWindow = Toplevel() 
 UpdateFoodWindow.title("Update Food Window")  UpdateFoodWindow.geometry("300x200") 
 def confirm_food_update(): 
 global foods 
 foods.append([new_food_item.get(), int(new_food_price.get())])
 # this function adds the added details to the foods list in the form [[new_food_item, new_item_price]]  UpdateFoodWindow.destroy() 
 Label(UpdateFoodWindow, text="Food Item: ").grid(row=0, column=0) 
 new_food_item = Entry(UpdateFoodWindow)  new_food_item.grid(row=0, column=1) 
 Label(UpdateFoodWindow, text="Price:\n(in $) ").grid(row=1, column=0) 
 new_food_price = Entry(UpdateFoodWindow)  new_food_price.grid(row=1, column=1) 
 Button(UpdateFoodWindow, text="Confirm Update", command=confirm_food_update).grid(row=2, column=1) 
The same foods list then goes for billing when the customer clicks the “Confirm Order” button on the Place Order window. 
This function-oriented approach makes for a fast-operating, error less program.
