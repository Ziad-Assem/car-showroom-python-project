#####TESTING DB FUNCTIONS#######
from branches import Branch
from  users import User
import functions
import constants



# smouha_branch=Branch("smouha")
# gleem_branch=Branch("gleem")
# #
# # gleem_branch.add_car("gleem", "Toyota", "Corolla", "Sedan", "White", 25000.00)
# # # #
# # smouha_branch.add_car("smouha", "Honda", "Civic", "Sedan", "Black", 27000.50)
# # # #
# # gleem_branch.add_car("gleem", "Ford", "Mustang", "Coupe", "Red", 55000.75)
# # # #
# gleem_branch.list_all_branch_cars()
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
branches_objects={}

#initializing with smouha, the first branch
branch, obj = functions.create_branch(constants._FIRST_BRANCH)
branches_objects[branch]=obj

functions.welcome_message()
functions.main_login(obj)
