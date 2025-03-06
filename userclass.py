class User:
    def __init__(self, db, username, role):
        self.db = db
        self.username = username
        self.role = role  # 'Administrator', 'Manager', 'User'
    
    @staticmethod
    def create_root_user(db):
        query = "SELECT COUNT(*) FROM users WHERE role = 'Administrator'"
        count = db.fetchone(query)[0]
        if count == 0:
            query = "INSERT INTO users (username, role) VALUES (%s, %s)"
            db.execute(query, ('root', 'Administrator'))
            print("Root administrator user created successfully.")
        else:
            print("Administrator already exists.")
    
    def create_user(self, new_username, new_role):
        if self.role != 'Administrator':
            print("Access Denied: Only administrators can create users.")
            return
        query = "INSERT INTO users (username, role) VALUES (%s, %s)"
        self.db.execute(query, (new_username, new_role))
        print(f"User {new_username} created with role {new_role}.")
    
    def delete_car(self, branch_id, car_id):
        if self.role not in ['Administrator', 'Manager']:
            print("Access Denied: Only administrators and managers can delete cars.")
            return
        table_name = f"cars_branch_{branch_id}"
        query = f"DELETE FROM {table_name} WHERE id = %s"
        self.db.execute(query, (car_id,))
        print(f"Car with ID {car_id} deleted from branch {branch_id}.")
    
    def add_car(self, branch_id, brand, model, year, price, status, description):
        if self.role not in ['Administrator', 'Manager']:
            print("Access Denied: Only administrators and managers can add cars.")
            return
        table_name = f"cars_branch_{branch_id}"
        query = f"INSERT INTO {table_name} (brand, model, year, price, status, description) VALUES (%s, %s, %s, %s, %s, %s)"
        self.db.execute(query, (brand, model, year, price, status, description))
        print(f"Car {brand} {model} added to branch {branch_id}!")
    
    def search_car(self, brand, model, num_branches=3):
        if self.role not in ['Administrator', 'Manager', 'User']:
            print("Access Denied: Invalid role.")
            return
        results = []
        for branch_id in range(1, num_branches + 1):
            table_name = f"cars_branch_{branch_id}"
            query = f"SELECT * FROM {table_name} WHERE brand = %s AND model = %s"
            cars = self.db.fetchall(query, (brand, model))
            
            for car in cars:
                results.append({"branch_id": branch_id, "car": car})
        
        return results
