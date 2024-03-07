print("Hello World!")

# let variable = 21;
name = "James"
last_name = "Chon"
total = 69.69
age = 30
found = True

# if/else statement
# if(var==var2){
# logic
# }
if age < 100:
    print("Don't worry, you're not that old!")
elif age == 100:
    print("Congratz you're hella old!")
else:
    print("Sorry, seems that you're dead!")

# function
# function say_hello(){}

def say_hello():
    print("Hello there")

def say_goodbye(name):
    print("Goodbye" + name)

# call a function
say_hello()
say_goodbye(" Chon")

# Concatenate
print("Hello my name is" + name + "and I have" + str(age) + " years old")
