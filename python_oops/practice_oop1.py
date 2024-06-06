# This is project which is going to replicate the Airlines booking and other facilities

class Airline():

    def __init__(self):
        self.passengers = []


    def add_passenger(self, pass_name, seat_number, meal_plan, age, meal_price):
        if self.is_passenger_exists(pass_name, age, seat_number):
            print(f"Passenger with name {pass_name}, seat number {seat_number}, and age {age} already exists. Please check the details.")
        else:
            passenger = {
                'name': pass_name,
                'seat_number': seat_number,
                'meal_plan': meal_plan,
                'age': age,
                'meal_price': meal_price
            }
            self.passengers.append(passenger)
            print(f"Passenger {pass_name} added successfully")


    def is_passenger_exists(self, pass_name, seat_number, age):
        for passenger in self.passengers:
            if passenger['name'] == pass_name and passenger['seat_number'] == seat_number and passenger['age'] == age:
                return True
        return False
        
    def meal_booking(self, pass_name, meal_plan, meal_price):
        for passenger in self.passengers:
            if passenger['name'] == pass_name:
                passenger['meal_plan'] = meal_plan
                passenger['meal_price'] = meal_price
                print(f"Meal plan {meal_plan} booked for passenger {pass_name}")
                return
        print(f"Passenger with name {pass_name} not found")

    def display_passenger_details(self):
        if not self.passengers:
            print("No passengers found")
        else:
            for passenger in self.passengers:
                print(f"Name: {passenger['name']}, Seat: {passenger['seat_number']}, Meal Plan: {passenger['meal_plan']}, Age: {passenger['age']}, Meal Price: {passenger['meal_price']}")



def main():
        # Example usage:
    airline = Airline()
    airline.add_passenger('John Doe', '12A', 'Vegetarian', 30, 20)
    airline.add_passenger('Jane Smith', '14B', 'Non-Vegetarian', 25, 25)
    airline.meal_booking('John Doe', 'Vegan', 30)
    airline.meal_booking('Smith Joe', 'Non-Vegan', 40)
    airline.meal_booking('Jane Smith', 'Non-Vegan', 40)

     
if __name__ == "__main__":
    main()

            
    

