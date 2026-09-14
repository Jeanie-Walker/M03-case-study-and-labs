"""
Name:        Jeanie Walker
File:        auto.py

Description:
    This program asks a user for input about their car and stores it in the 
    automobile object, then prints put the results. 

Variables:
    vehicle_type: what kind of vehicle
    year: year the car was manufactured
    make: the maker of the car (Honda, Toyota, etc)
    model: The car's model (Accord, Corolla, etc)
    doors: the number of doors
    roof: what type of roof it has
    car: automobile object that holds the values above
"""


class Vehicle:

    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):

    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display(self):
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")


def user_input(prompt, valid):
    while True:
        answer = input(prompt).strip().lower()
        if answer in valid:
            return answer
        print(f"Please enter one of the two options as shown: {', '.join(valid)}")


def main():
    print("Enter the following information about your car.\n")

    year = input("Year: ").strip()
    make = input("Make: ").strip().title()
    model = input("Model: ").strip().title()
    doors = user_input("Number of doors (2 or 4): ", ["2", "4"])
    roof = user_input("Type of roof (solid or sun roof): ", ["solid", "sun roof"])

    car = Automobile("car", year, make, model, doors, roof)

    print()
    car.display()


if __name__ == "__main__":
    main()