#####TESTING DB FUNCTIONS#######
from branches import Branch
from  users import User
import functions


# sodo_branch=Branch("sodo")
#
# # sodo_branch.add_car("sodo", "Toyota", "Corolla", "Sedan", "White", 25000.00)
# #
# # sodo_branch.add_car("sodo", "Honda", "Civic", "Sedan", "Black", 27000.50)
# #
# # sodo_branch.add_car("sodo", "Ford", "Mustang", "Coupe", "Red", 55000.75)
# #
# # sodo_branch.add_car("sodo", "Chevrolet", "Camaro", "Sports", "Yellow", 60000.00)
# #
# # sodo_branch.add_car("sodo", "BMW", "X5", "SUV", "Blue", 75000.99)
#
# cars, table = sodo_branch.display_cars("sodo")
# branch="sodo"
#
# # print(f"{table} \n with len of: {cars[0][0]}")
# sodo_branch.purchase_car(branch)
# # sodo_branch.purchase_car()

#######################################################################
#######################################################################
#######################################################################
# count = sodo_branch.first_run_check()
# print(f"Number of tables in DB: {count}")
functions.welcome_message()
functions.main_login()
