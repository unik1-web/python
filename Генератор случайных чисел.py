# importing  uuid module
import uuid
# Initialize the variable
num = 0
# Iterating using while loop to produce 5 UUIDs 
while(num<10):
  # Generate a random number using UUID 4 method
  print(num, "----->",uuid.uuid4())
  # Increment the value by one
  num+=1