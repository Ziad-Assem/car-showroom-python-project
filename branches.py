from database import Database
from datetime import datetime
from decimal import Decimal
from beautifultable import BeautifulTable

class Branch:

    def __init__(self, branch):
        self.db = Database()
        if self.first_run_check() == 1 or branch != 'smouha':
            self.db.create_branch(branch)

    def add_branch(self, branch):
        self.db.create_branch(branch)

    def add_user(self,first_name, last_name, username, password, privilege, branch):

    def add_car(self, branch, brand, model, car_type, color, price):
        self.db.add_car(branch, brand, model, car_type, color, price)

    def purchase_car(self, branch):
        cars, car_table = self.display_cars(branch)
        print(car_table)
        choice_id= int(input("Please input ID of car to purchase.."))
        car_index=self.find_car_index(choice_id, cars)
        chosen_car=cars[car_index]
        print(f"\n\nChosen car was ID: {chosen_car[0]} with index of: {car_index}")
        current_time = datetime.now()

        print(f"DATA TO SEND TO SQL QUERY IS:\n {(branch, current_time, chosen_car[1], chosen_car[2], chosen_car[5])}")
        self.db.add_sales_record(branch, current_time, chosen_car[1], chosen_car[2], chosen_car[5])
        self.db.remove_car(branch, chosen_car[0])

    def find_car_index(self, chosen_car_id, cars):
        for i in range(len(cars)):
            if cars[i][0]==chosen_car_id:
                return i
        return -1

    def display_cars(self, branch):
        # return self.create_car_table(self.db.get_all_cars(branch))
        cars = self.db.get_all_cars(branch)
        car_table=self.create_car_table(cars)

        return cars, car_table

    def create_car_table(self, car_list):
        table = BeautifulTable()
        table.columns.header = ["ID", "Brand", "Model", "Category", "Color", "Price"]

        for car in car_list:
            car_id, brand, model, category, color, price = car
            table.rows.append([car_id, brand, model, category, color, price])

        return table

    def check_user(self,username, password):
        result = self.db.search_user(username, password)
        if result[0][0] == username and result[0][1] == password:
            print(f"Welcome back {username}\n")
            return (username, result[0][2])
        else:
            print(f"Wrong info please try again!{result}")
            return (result[0], result[1])

    def first_run_check(self):
        count = self.db.count_total_tables()
        return count