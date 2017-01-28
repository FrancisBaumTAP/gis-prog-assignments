
##  ASSIGNMENT01

# Part One - Github
# 1) Go through the Hello World Tutorial (https://guides.github.com/activities/hello-world/)
# 2) Create your new repository in your own Organization (not the WUSTLGIS organization)
# 3) After completing the tutorial, take a screen shot of the Github screen when it displays the "Pull request sucessfully merged and closed" message.
# 4) Save your screen shot as Assignment01.jpg and upload to your WUSTLGIS repo in your Assignments folder.

# Part Two - Working with numeric, string and list objects.
# 1) Create two numeric variables and then a third variable that adds them both together.
a = 1
b = 2
c = a + b

# 2) Add a print statement to print out the result of the third variable.
print c

# 3) Think of a phrase and create separate variables for each word in the phrase.
word1 = "Fight"
word2 = "fire"
word3 = "with"

# 4) Create another variable that concatenates all of the strings created in Step #3.
phrase = word1 + " " + word2 + " " + word3 + " " + word2 + "."

# 5) Add a print statement to print out the full phrase. (Note - don't forget spaces)
print phrase

# 6) Add another print statement that prints the character length of the phrase.  The print statement should read:
# <Phrase created in Step #4> contains <Length of Phrase> characters.
print '"' + phrase + '" contains ' + str(len(phrase)) + ' characters.'

# 7) Choose any directory on your machine and create a string variable with the path to this directory.
pathCommonFiles = r"C:\Program Files (x86)\Common Files"

# 8) Add a print statement that reads:
# <Directory> is the working directory.
print '"' + pathCommonFiles + '" is the working directory.'

# 9) Save your script as Assignment01.py and upload to your WUSTLGIS repo in your Assignments folder.
