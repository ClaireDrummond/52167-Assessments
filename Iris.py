# Claire Drummond 2018-02-28
# Iris Data Set Exercise 5

with open("data/iris.csv") as f: #importing of the Iris Data Set
    for line in f:
        data = line.split(',') #creating space between the data
        print('{0[0]:12} {0[1]:12} {0[2]:12} {0[3]:12} {0[4]:12}'.format(data))

 # the formatting of the data        
     
