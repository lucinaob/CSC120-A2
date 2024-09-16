"""
    Filename: oo_resale_shop.py
Description: an object-oriented adaptation of procedural_resale_shop
             as a part of A2: Object-ification. Details the construction
             of a computer to be resold at the resale shop.
    Author: Lucy O'Brien (@lucinaob)
    Date: September 16, 2024
"""

class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int


    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # What methods will you need?

def main():
     # First, let's make a computer
    computer = Computer(
    "Mac Pro (Late 2013)",
    "3.5 GHc 6-Core Intel Xeon E5",
    1024, 64,
    "macOS Big Sur", 2013, 1500
    )
    print(Computer)

#only run main() if running program directly
if __name__ == "__main__":
    main()