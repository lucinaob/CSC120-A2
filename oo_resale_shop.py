"""
    Filename: oo_resale_shop.py
Description: an object-oriented adaptation of procedural_resale_shop
             as a part of A2: Object-ification. Details the methods
             of different operations of a resale shop.
    Author: Lucy O'Brien (@lucinaob)
    Date: September 16, 2024
"""

#Importing necessary components
from computer import Computer
from typing import Dict, Optional

class ResaleShop:

    # Establishing the inventory and ID system
    inventory : Dict
    global itemID
    itemID = 0

    #Setting the inventory to start with nothing
    def __init__(self):
        self.inventory = {}

    #Initalizing the inventory with a base set of computers
    def InitializeInventory(self, computer: Computer):
        global itemID
        itemID += 1 # incrementing itemID for each computer
        self.inventory[itemID] = computer #Adding given computer to inventory
        return itemID

    #Method to view computers in the inventory
    def ViewInventory(self): 
        if self.inventory:
            # For each item
            for item_id in self.inventory:
                # Print its details
                print(f'Item ID: {item_id} : {vars(self.inventory[item_id])}')
        else:
            #Error message
            print("No inventory to display.")
    
    #Method to add a new computer to the inventory
    def BuyComputer(self):
        #Adding a new item to the inventory, increasing ID
        global itemID
        itemID += 1
        #Asking questions to specify details of the computer being bought
        description = input("What kind of computer is this? ")
        processor_type = input("What is the processor type? ")
        hard_drive_capacity = int(input("What is the hard drive capacity? (Integer) "))
        memory = int(input("What is the memory? (Integer) "))
        operating_system = input("What is the operating system? ")
        year_made = int(input("What is the year it was made? (Integer) "))
        price = int(input("What is the price? (Integer) "))
        #Collecting this manual input into a computer object
        computer = Computer(description, 
                            processor_type,
                            hard_drive_capacity, 
                            memory, 
                            operating_system,
                            year_made,
                            price)
        #Adding this item to the inventory
        self.inventory[itemID] = computer
        return itemID
    
    #Method to take a computer out of the inventory
    def SellComputer(self):
        #Select computer from inventory to sell
        itemID = int(input("Which item would you like to sell? "))
        if itemID in self.inventory:
            del self.inventory[itemID] #Removes item from inventory
            print("Item", itemID, "sold!")
        else:
            #Error message
            print("Item", itemID, "not found. Please try again.")
    
    #Method to update price of an item
    def UpdatePrice(self):
        #Selecting price to update
        itemID = int(input("Which item would you like to update? Enter the corresponding integer. "))
        if itemID in self.inventory:
            #Input of new price
            NewPrice = int(input("What should the new price be? Please enter an integer. "))
            #Changing price attribute to new price
            self.inventory[itemID].price = NewPrice
        else:
            #Error message
            print("Item not in inventory.")
            
    def Refurbish(self):
        #Select computer to refurbish
        itemID = int(input("Which item would you like to refurbish? Enter the corresponding integer. "))
        if itemID in self.inventory:
            #Auto-updating price based on age of the computer
            computer = self.inventory[itemID]
            if int(computer.year_made) < 2000:
                computer.price = 0
            elif int(computer.year_made) < 2012:
                computer.price = 250
            elif int(computer.year_made) < 2018:
                computer.price = 550
            else:
                computer.price = 1000
            
            #Updating OS of a computer
            if computer.operating_system is not None:
                #User input if OS needs to be updated
                answer = input("Should this computer have a different OS? (Y/N) ")
                if answer == "Y":
                    #User input of new OS
                    new_os = input("What OS should the computer have?")
                    #Changing attribute to user-inputted OS
                    computer.operating_system = new_os
                else:
                    #Skipping step if not relevant
                    pass
        else:
            #Error message
            print("Item", itemID, "not found.")

def main():
    shop = ResaleShop()
    #Creating two computer objects for the inventory
    computerOne = Computer("2019 MacBook Pro", 
                               "Intel", 256, 16, 
                               "High Sierra", 2019, 1000)
    computerTwo = Computer("Mac Pro (Late 2013)",
                               "3.5 GHc 6-Core Intel Xeon E5",
                               1024, 64, "macOS Big Sur", 2013, 1500)
    #Adding these two to inventory
    shop.InitializeInventory(computerOne)
    shop.InitializeInventory(computerTwo)
    #Printing operations user can complete
    print("Below are the actions you can complete as shop owner.")
    print("1 - Buy a computer")
    print("2 - Sell a computer")
    print("3 - Update the price of an item")
    print("4 - View inventory")
    print("5 - Refurbish a computer")
    #User chooses an operation
    choice = int(input("What would you like to do? Please type the integer corresponding to the action. "))
    #Completing methods based on operation chosen
    #Inventory is printed when user must choose a computer to sell, update, etc.
    if choice == 1:
        shop.BuyComputer()
        shop.ViewInventory()
    elif choice == 2:
        shop.ViewInventory()
        shop.SellComputer()
        shop.ViewInventory()
    elif choice == 3:
        shop.ViewInventory()
        shop.UpdatePrice()
        shop.ViewInventory()
    elif choice == 4:
        shop.ViewInventory()
    elif choice == 5:
        shop.ViewInventory()
        shop.Refurbish()
        shop.ViewInventory()
    else: #Error message
        print("Input not valid. Please try again!")

main()
