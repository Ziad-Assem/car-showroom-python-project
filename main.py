#####TESTING DB FUNCTIONS#######

from branches import Branch

sodo_branch=Branch("sodo")
#
# sodo_branch.add_car("sodo", "Toyota", "Corolla", "Sedan", "White", 25000.00, 23000.00, 5)
#
# sodo_branch.add_car("sodo", "Honda", "Civic", "Sedan", "Black", 27000.50, 25000.00, 3)
#
# sodo_branch.add_car("sodo", "Ford", "Mustang", "Coupe", "Red", 55000.75, 50000.00, 2)
#
# sodo_branch.add_car("sodo", "Chevrolet", "Camaro", "Sports", "Yellow", 60000.00, 57000.00, 4)
#
# sodo_branch.add_car("sodo", "BMW", "X5", "SUV", "Blue", 75000.99, 70000.00, 6)

print(sodo_branch.display_cars("sodo"))

# sodo_branch.purchase_car()