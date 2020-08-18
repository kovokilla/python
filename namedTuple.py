# Import the 'namedtuple' function from the 'collections' module
from collections import namedtuple
# Set the tuple
#tuple je v podstate object
individual = namedtuple("Nazov_identifikacia", "name age height")
user = individual(name="Homer", age=37, height=178)
user2 = individual(name="Peter", age=33, height=175)
# Print the tuple
print(user)
print(user2)
people = (user, user2)
# Print each item in the tuple
#looping through tuple of tuples
#v pythone loopujes inak, ked das for item in (collection of items), tak “item” bude uz ten tuple, 
# takze ak chces jeho .name tak das item.name a nie collection[item].
for i in people:
  print(i.name)
  print(i.age)
  print(i.height)