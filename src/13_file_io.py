"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
with open('foo.txt', 'r') as f:
    print(f.read())


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
def new_file():

    f = open('bar.txt', "w+")

    for i in range(3):
        f.write("here is some text")

    f.close()

new_file()

with open('bar.txt', 'r') as q:
    print(q.read())