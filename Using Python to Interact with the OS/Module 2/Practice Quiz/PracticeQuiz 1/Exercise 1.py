''' EXERCISE 1 - READING AND WRITING FILES'''

guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")
    
guests.close()
# No output is generated for the above code cell. To check the contents of the newly created guests.txt file, run the following code.

with open("guests.txt") as guests:
    for line in guests:
        print(line)
# The output shows that our guests.txt file is correctly populated with each initial guest's first name on its own line. Cool!

# Now suppose we want to update our file as guests check in and out. Fill in the missing code in the following cell to add guests to the guests.txt file as they check in.

new_guests = ["Sam", "Danielle", "Jacob"]

with open("guests.txt", "a") as guests:
    for i in new_guests:
        guests.write(i + "\n")

guests.close()
# To check whether your code correctly added the new guests to the guests.txt file, run the following cell.

with open("guests.txt") as guests:
    for line in guests:
        print(line)

# The current names in the *guests.txt* file should be:  Bob, Andrea, Manuel, Polly, Khalid, Sam, Danielle and Jacob.

# Now let's remove the guests that have checked out already.  There are several ways to do this, however, the method we will choose for this exercise is outlined as follows:
# 1. Open the file in "read" mode.
# 2. Iterate over each line in the file and put each guest's name into a Python list.
# 3. Open the file once again in "write" mode.
# 4. Add each guest's name in the Python list to the file one by one.

# Ready? Fill in the missing code in the following cell to remove the guests that have checked out already.

checked_out=["Andrea", "Manuel", "Khalid"]
temp_list=[]

with open("guests.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())

with open("guests.txt", "w") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")

# To check whether your code correctly removed the checked out guests from the guests.txt file, run the following cell.
with open("guests.txt") as guests:
    for line in guests:
        print(line)
# The current names in the guests.txt file should be: Bob, Polly, Sam, Danielle and Jacob

# Now let's check whether Bob and Andrea are still checked in. How could we do this? We'll just read through each line in the file to see if their name is in there. Run the following code to check whether Bob and Andrea are still checked in.

guests_to_check = ['Bob', 'Andrea']
checked_in = []

with open("guests.txt","r") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))

