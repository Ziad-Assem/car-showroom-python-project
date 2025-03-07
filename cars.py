####class cars
class Car:
    def __init__(self, brand, model, year, price, status, description):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.status = status
        self.description = description

    ##########hna hn3ml 2n customer hwa ale ydef 3rbeto llbe3 msln l22rb branch
    def add_to_branch(self, db, branch_id):
        table_name = f"cars_branch_{branch_id}"
        query = f"INSERT INTO {table_name} (brand, model, year, price, status, description) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        db.execute(query, (self.brand, self.model, self.year, self.price, self.status, self.description))
        print(f"Car {self.brand} {self.model} added to branch {branch_id}!")


######search car
class CarSearch:
    @staticmethod
    def search_in_branches(db, brand, model, num_branches=3):
        results = []
        for branch_id in range(1, num_branches + 1):
            table_name = f"cars_branch_{branch_id}"
            query = f"SELECT * FROM {table_name} WHERE brand = %s AND model = %s"
            cars = db.fetchall(query, (brand, model))

            for car in cars:
                results.append({"branch_id": branch_id, "car": car})

        return results