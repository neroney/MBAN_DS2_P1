#####################################################################
#
#	Data Science 2 - Project 1
#	Due: March 1st
#
#
#####################################################################

#####################################################################
#
# Part A:
#
# Help the client gain some basic understanding of their data. 
# You should answer basic questions such as:
#	-How many users are there?
#	-How many interest categories were created by users? 
#	-What is the distribution of interests in the entire population of individuals? 
#	-How many declared interests do individual users have (histogram)?
#	-Determine and plot appropriate social network measures such as connection degree distribution. 
#	-Can you make any comparison to well-studied social networks such as Twitter?
#
#######################################################################

# Two data sets
# 
# Num	Name		Column1		Column2
#
# 1.	follows.csv:	follower_id	followee_id
# 2.	interests.csv: 	user_id  	category

####

# How many users are there?

# I will need the interests.csv data set to count the number of unique
# user_id's
import csv

f = open('interests.csv')
csv_f = csv.reader(f)

user_id = []
for row in csv_f:
    print row
    user_id.append(row[0])

print user_id[0]

# so the first row of user_ID is the column title user_ID
# i need to remove that

del user_id[0]		# this will remove the 0th value from the data set
print user_id[0]	# success !!


# now to get a list of the unique user ID's I just need to use the set statement

unique_user_id = set(user_id)	# gets the unqiue values
num_users = len(unique_user_id)
print 'Number of users = ' + str(num_users) # The number of users!


####

# How many interest categories were created by users? 

#g = open('interests.csv')
csv_g = csv.reader(open('interests.csv'))

cat = []
for row in csv_g:
    print row
    cat.append(row[1])

print cat[0]

# so the first row of cat is the column title 'category'
# i need to remove that

del cat[0]		# this will remove the 0th value from the data set
print cat[0]	# success !!

# now to get a list of the unique categories's I just need to use the set statement

unique_cat = set(cat)	# gets the unqiue values
num_cat = len(unique_cat)
print 'Number of categories = ' + str(num_cat) # The number of categories!


####

# What is the distribution of interests in the entire population of individuals? 

# Get a frequency distribution of everything in the list





#####################################################################
#
# Part B:
# Train a classifier capable of predicting which user will follow another user. 
# The client hopes this will enable the app to make recommendations on who a user should follow 
# and thereby increase the number of user follows, ultimately leading to increased revenue. 
# In other words, they hope by leveraging technology they will be able to move towards a "push" model, # where the agency in initiating connections moves to the application, 
# by suggesting appropriate new connections.
#
# Validate, and assess the performance characteristics of your classifier.
# State any assumptions you are making.
#
#####################################################################
