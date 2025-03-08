import mysql.connector
import constants
import queries


class Database:
    def __init__(self):
        self.host=constants._DB_HOST
        self.user=constants._DB_USER
        self.password=constants._DB_PASSWORD
        self.database=constants._DB_NAME

    def establish_database_connection(self):
        db_connection = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
        cursor = db_connection.cursor()
        return db_connection, cursor

    def add_new_user(self, first_name, last_name, username, password, privilege, branch):
        try:
            db_connection, cursor= self.establish_database_connection()
            cursor.execute(queries.add_user_query(first_name, last_name, username, password, privilege, branch))
            db_connection.commit()
            self.close_connection(db_connection)
        finally:
            print("Couldn't add a new user! please try again!")

    def search_user(self, username, password):
        try:
            db_connection, cursor= self.establish_database_connection()
            cursor.execute(queries.verify_user_query(username, password))
            result = cursor.fetchall()

            self.close_connection(db_connection)
            return result
        finally:
            print("Couldn't find user!, please try again!")

    def create_branch(self, branch):
        db_connection, cursor = self.establish_database_connection()

        try:
            if not self.table_exists(branch):  # 🔹 Corrected logic: Proceed only if branch doesn't exist
                cursor.execute(queries.create_cars_table_query(branch))
                cursor.execute(queries.create_sales_table_query(branch))  # 🔹 Run both in the same session

                db_connection.commit()  # 🔹 Save changes before closing
                print(f"Branch '{branch}' created successfully!")
            else:
                print("Can't create this branch as it already exists!")

        except Exception as e:
            print(f"Error creating branch: {e}")

        finally:
            self.close_connection(db_connection)  # 🔹 Close only once at the end


    def table_exists(self, branch):
        db_connection, cursor = self.establish_database_connection()

        query = f"SHOW TABLES LIKE 'cars_{branch}';"
        cursor.execute(query)
        result = cursor.fetchone()  # Fetch one result

        self.close_connection(db_connection)

        return result is not None  # Return True if the table exists, False otherwise


    def add_car(self, branch, brand, model, car_type, color, price, min_price, stock):
        db_connection, cursor = self.establish_database_connection()
        if self.table_exists(branch):
            cursor.execute(queries.add_car_query(branch, brand, model, car_type, color, price, min_price, stock))
            print(f"Adding {model}")
            db_connection.commit()
            self.close_connection(db_connection)
        else:
            print("This branch does not exist!")

        self.close_connection(db_connection)

    def remove_car(self, branch, car_id):
        db_connection, cursor = self.establish_database_connection()
        cursor.execute(queries.delete_car_query(branch, car_id))
        print("Car was sold successfully!")
        db_connection.commit()
        self.close_connection(db_connection)

    def search_car(self, branch, model):
        db_connection, cursor = self.establish_database_connection()
        cursor.execute(queries.search_car_query(branch, "model", model))
        result = cursor.fetchall()

        self.close_connection(db_connection)
        return result

    def get_all_cars(self,branch):
        db_connection, cursor = self.establish_database_connection()
        cursor.execute(queries.get_all_cars_query(branch))
        result = cursor.fetchall()

        self.close_connection(db_connection)
        return result

    def add_sales_record(self,branch, date_time, brand, model, price, units):
        db_connection, cursor = self.establish_database_connection()
        cursor.execute(queries.add_sale_query(branch, date_time, brand, model, price, units))
        db_connection.commit()
        self.close_connection(db_connection)

    def get_branch_sales(self, branch):
        db_connection, cursor = self.establish_database_connection()
        cursor.execute(queries.search_sales_by_branch_query(branch))

        result=cursor.fetchall()
        self.close_connection(db_connection)

        return result


    def close_connection(self, db_connection):
        db_connection.close()
