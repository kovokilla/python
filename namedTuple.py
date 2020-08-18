# Import the 'namedtuple' function from the 'collections' module
from collections import namedtuple
# Set the tuple
individual = namedtuple("Individual", "name age height")
user = individual(name="Homer", age=37, height=178)
# Print the tuple
print(user)
# Print each item in the tuple
print(user.name)
print(user.age)
print(user.height)