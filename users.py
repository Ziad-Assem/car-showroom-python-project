class User:
    def __init__(self, db, agentname, role):
        self.db = db
        self.agentname = agentname
        self.role = role  # 'admin', 'manager', 'agent'
    
    @staticmethod
    def create_root_agent(db):
        ##query = "SELECT COUNT(*) FROM agents WHERE role = 'admin'"
        count = db.fetchone(query)[0]
        if count == 0:
            ##query = "INSERT INTO agents (agentname, role) VALUES (%s, %s)"
            db.execute(query, ('root', 'admin'))
            print("Root admin agent created successfully.")
        else:
            print("admin already exists.")
    
    def create_agent(self, new_agentname, new_role):
        if self.role != 'admin':
            print("Access Denied: Only admins can create agents.")
            return
        ##query = "INSERT INTO agents (agentname, role) VALUES (%s, %s)"
        self.db.execute(query, (new_agentname, new_role))
        print(f"agent {new_agentname} created with role {new_role}.")
    
    def delete_car(self, branch, car_id):
        if self.role not in ['admin', 'manager']:
            print("Access Denied: Only admins and managers can delete cars.")
            return
        table_name = f"cars_branch_{branch}"
        ##query = f"DELETE FROM {table_name} WHERE id = %s"
        self.db.execute(query, (car_id,))
        print(f"Car with ID {car_id} deleted from branch {branch}.")
    
    def add_car(self, branch, brand, model, year, price, status, description):
        if self.role not in ['admin', 'manager']:
            print("Access Denied: Only admins and managers can add cars.")
            return
        table_name = f"cars_branch_{branch}"
        ##query = f"INSERT INTO {table_name} (brand, model, year, price, status, description) VALUES (%s, %s, %s, %s, %s, %s)"
        self.db.execute(query, (brand, model, year, price, status, description))
        print(f"Car {brand} {model} added to branch {branch}!")
    
    def search_car(self, brand, model, num_branches=3):
        if self.role not in ['admin', 'manager', 'agent']:
            print("Access Denied: Invalid role.")
            return
        results = []
        for branch in range(1, num_branches + 1):
            table_name = f"cars_branch_{branch}"
            ##query = f"SELECT * FROM {table_name} WHERE brand = %s AND model = %s"
            cars = self.db.fetchall(query, (brand, model))
            
            for car in cars:
                results.append({"branch": branch, "car": car})
        
        return results
