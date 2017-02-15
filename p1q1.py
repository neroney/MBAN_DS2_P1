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

import pandas as pd
import numpy as np
import os

intes = pd.read_csv("interests.csv")				# read the data
char_users = intes['user_id'].astype(str)			# Convert users to str
#new_users = np.array([user_id[0] for user_id in char_users]) 	#Take first letter
#intes["user_id"] = pd.Categorical(new_users)			# Save the new cabin var

intes[0].value_counts()

#pd.crosstab(index=intes['user_id'],     # Make a crosstab
#                      columns="count")      # Name the count column


