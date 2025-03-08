from database import Database
from datetime import datetime

class Branch:

    def __init__(self, branch):
        self.db=Database()
        self.db.create_branch(branch)

    def add_branch(self, branch):
        self.db.create_branch(branch)

    def add_car(self, branch, brand, model, car_type, color, price, min_price, stock):
        self.db.add_car(branch, brand, model, car_type, color, price, min_price, stock)

    def purchase_car(self, branch, car_id):
        result = self.display_cars(branch)
        # current_time = datetime.now()
        print(f"purchase_car func{result}")
        # self.db.add_sales_record(branch,)
        self.db.remove_car(branch, car_id)


    def display_cars(self, branch):
        return self.db.get_all_cars(branch)




    # @classmethod  ##34an ha5od cls anfz mnha 7agat fhwa kda byt3aml 3la class kolo
    # def crea(cls, db, name, location, manager):
    #     ##### add manager name function (CALL FUNCTION IN CLASS USERS)
    #
    #     query = "INSERT INTO branches (name, location, manager) VALUES (%s, %s, %s)"
    #     db.execute(query, (name, location, manager))
    #
    #     branch_id = db.fetchone("SELECT LAST_INSERT_ID()")[0]  # zero to get first element from tupple
    #     cls.create_branch_cars_table(db, branch_id)  # bn3ml gdwl llcars bta3t el branch ale lsa 3mleno
    #
    #     print(f"Branch '{name}' added with ID {branch_id}")
    #
    # @staticmethod
    # def create_branch_cars_table(db, branch_id):
    #     table_name = f"cars_branch_{branch_id}"
    #     # de mn chat m4 fhmha
    #     query = f"""
    #     CREATE TABLE {table_name} (
    #         id INT AUTO_INCREMENT PRIMARY KEY,
    #         brand VARCHAR(50) NOT NULL,
    #         model VARCHAR(50) NOT NULL,
    #         year INT NOT NULL,
    #         price DECIMAL(10,2) NOT NULL,
    #         status ENUM('Available', 'Sold') NOT NULL,
    #         description TEXT
    #     );
    #     """
    #     db.execute(query)
    #     print(f"Table {table_name} created successfully!")