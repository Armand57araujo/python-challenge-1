# python-challenge-1


## Technology Used 

| Technology Used | Resource URL | 
| ------------- |:-------------:| 
| Python | [https://www.w3schools.com/python/python_reference.asp](https://www.w3schools.com/python/python_reference.asp) | 
| Git | [https://git-scm.com/](https://git-scm.com/) | 

## Description 
In this project I created an interactive ordering system for a food truck menu using python, that allows users to select items for purchase and after checkout receive a receipt with a subtotal for the items selected.

## Code Example 

<---- First we initialize the order list using the following empty list ----->
         
         customer_order = []

 <---- In this part of the code we launch the store and present a greeting to the customer ----->

         print("Welcome to the variety food truck.")

<---- Next we implement the main loop to handle the customer's order process ----->

         place_order = True
         while place_order:

<------ Here we prompt the customer asking them from which menu category they want to order ------>

         print("\nFrom which menu would you like to order?")

<----- Then we display menu categories and store them in a dictionary ------->

     i = 1
     menu_items = {}
     for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key
        i += 1

<-----  User is then prompted for menu selection and inputs are saved ------>

         menu_selection = input("Type menu number: ")

<------ Check if the customer's input is a number -------->
         if menu_selection.isdigit():
< ------ Convert menu_selection to integer ------>
         menu_selection = int(menu_selection)`





This project was a challenge... <-----ADD MORE + ADDITIONAL CODE SNIPPET --------> 



      

I was experiencing a problem ... <-----ADD MORE --------> 



## Learning Points 


I was happy with.... <-----ADD MORE -------> . Google, W3, MDN, and ChatGPT are still my best friends that I will always keep very close.


## Author Info
Armand Araujo
Age: 29
Location: Las Vegas, NV

 
* [LinkedIn](https://www.linkedin.com/in/armand-araujo-a82ba2291/) 
* [Github](https://github.com/Armand57araujo) 


## Credits 