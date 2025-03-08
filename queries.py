###########################################
########## General DB Queries #############
###########################################

def check_table_exists_query(branch):
    return f"""
    SELECT COUNT(*) > 0 AS table_exists 
    FROM INFORMATION_SCHEMA.TABLES 
    WHERE TABLE_NAME LIKE {"%"+branch+"%"};
"""



###########################################
############ USERS TABLE ##################
###########################################

#create 'users' table
def create_users_table_query():
    return f"""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL, 
        privilege ENUM('admin', 'manager','agent') NOT NULL DEFAULT 'agent'
        branch VARCHAR(50) NOT NULL
    );
    """

#add user
def add_user_query(first_name, last_name, username, password, privilege, branch):
    return f"""
    INSERT INTO users (first_name, last_name, username, password, privilege, branch)
    VALUES ('{first_name}', '{last_name}', '{username}', '{password}', '{privilege}', '{branch}');
    """

#remove user
def remove_user_query(username):
    return f"DELETE FROM users WHERE username = '{username}';"

#update user
def update_user_query(username, field, new_value):
    return f"UPDATE users SET {field} = '{new_value}' WHERE username = '{username}';"


#search user for login purposes
def verify_user_query(username, password):
    return f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}';"


###########################################
############ CAR TABLE ####################
###########################################

#create 'cars' table
def create_cars_table_query(branch):
    return f"""
    CREATE TABLE IF NOT EXISTS {"cars_"+branch} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        brand VARCHAR(255) NOT NULL,
        model VARCHAR(255) NOT NULL,
        type VARCHAR(50) NOT NULL,
        color VARCHAR(50) NOT NULL,
        price DECIMAL(10,2) NOT NULL,
        min_price DECIMAL(10,2) NOT NULL,
        stock INT NOT NULL
    );
    """

#add car
def add_car_query(branch, brand, model, car_type, color, price, min_price, stock):
    return f"""
    INSERT INTO {"cars_"+branch} (brand, model, type, color, price, min_price, stock)
    VALUES ('{brand}', '{model}', '{car_type}', '{color}', {price}, {min_price}, {stock});
    """

#get all cars
def get_all_cars_query(branch):
    return f"SELECT * FROM {"cars_"+branch};"

#delete car
def delete_car_query(branch, car_id):
    return f"DELETE FROM {"cars_"+branch} WHERE id = {car_id};"

#search car
def search_car_query(branch, field, value):
    return f"SELECT * FROM {"cars_"+branch} WHERE {field} = '{value}';"

#search car by id
def get_car_by_id_query(branch, car_id):
    return f"SELECT * FROM cars_{branch} WHERE id = {car_id};"

###########################################
############ SALES TABLE ##################
###########################################

#create 'sales' table
def create_sales_table_query(branch):
    return f"""
    CREATE TABLE IF NOT EXISTS {"sales_"+branch} (
        transaction_id INT AUTO_INCREMENT PRIMARY KEY,
        date_time DATETIME NOT NULL,
        branch VARCHAR(50) NOT NULL,
        brand VARCHAR(50) NOT NULL,
        model VARCHAR(50) NOT NULL,
        price DECIMAL(10,2) NOT NULL,
        units INT NOT NULL
    );
    """

#add sale
def add_sale_query(branch, date_time, brand, model, price, units):
    return f"""
    INSERT INTO {"sales_"+branch} (date_time, branch, brand, model, price, units)
    VALUES ('{date_time}', '{branch}', '{brand}', '{model}', {price}, {units});
    """

#remove sale
def remove_sale_query(branch, transaction_id):
    return f"DELETE FROM {"sales_"+branch} WHERE transaction_id = {transaction_id};"

#get all sales fro branch
def search_sales_by_branch_query(branch):
    return f"SELECT * FROM {"sales_"+branch};"












