import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="marvenmarven",  #na2s check  complex password
            database="car_showroom"   # da name bta3 el Table
        )
        self.cursor = self.conn.cursor() #create cursor to excute instructions 

    #this functions to excute table's functions  
    #query -->insert update delete select
    #params---> the data will give with table's functions
    
    def execute(self, query, params=None): #to excute INSERT, UPDATE, DELETE
        self.cursor.execute(query, params or ())
        self.conn.commit() #commit to save changes 

    def fetchall(self, query, params=None):#to excute SELECT
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def fetchone(self, query, params=None):#to get only one row 
        self.cursor.execute(query, params or ())
        return self.cursor.fetchone()

    def close(self):#the connection should be closed after excute
        self.conn.close()

#######class branches###########

class Branch:
   
    @classmethod ##34an ha5od cls anfz mnha 7agat fhwa kda byt3aml 3la class kolo 
    def add_branch(cls, db, name, location, manager):



         ##### add manager name function (CALL FUNCTION IN CLASS USERS)



        query = "INSERT INTO branches (name, location, manager) VALUES (%s, %s, %s)"
        db.execute(query, (name, location, manager))

        branch_id = db.fetchone("SELECT LAST_INSERT_ID()")[0]#zero to get first element from tupple
        cls.create_branch_cars_table(db, branch_id)#bn3ml gdwl llcars bta3t el branch ale lsa 3mleno 

        print(f"Branch '{name}' added with ID {branch_id}")

    @staticmethod
    def create_branch_cars_table(db, branch_id):
        table_name = f"cars_branch_{branch_id}"
        #de mn chat m4 fhmha 
        query = f""" 
        CREATE TABLE {table_name} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            brand VARCHAR(50) NOT NULL,
            model VARCHAR(50) NOT NULL,
            year INT NOT NULL,
            price DECIMAL(10,2) NOT NULL,
            status ENUM('Available', 'Sold') NOT NULL,
            description TEXT
        );
        """
        db.execute(query)
        print(f"Table {table_name} created successfully!")
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
    

class users:
    def __init__(self,db):
        ###FUNCTION OF ADD MANAGER DATA WHEN WE ADD BRANCH 
        pass