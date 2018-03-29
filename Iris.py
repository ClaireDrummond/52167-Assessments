# Claire Drummond 2018-02-28
# Iris Data Set Exercise 5

# ref: https://en.wikipedia.org/wiki/Iris_flower_data_set
# ref: https://pyformat.info/

with open("data/iris.csv") as f: #importing of the Iris Data Set.  This will close the file after the program has run
    for line in f:
        data = line.split(',') #creating space between the data
        print('{0[0]:10} {0[1]:10} {0[2]:10} {0[3]:10} {0[4]:10}'.format(data))

 # the formatting of the data 
 # The curly brackets, followed by .format tells the script that I want the data formatted in a certain way
 # The square bracket tells script what element in the list I am referring to
 # The number '10' tells the script how many spaces to leave between each of the values       
     
