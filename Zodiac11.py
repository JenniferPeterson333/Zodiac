import time
# The following gives the time in seconds
start_time = time.time()
# Your main program could be placed here which would take
# time to run. To simulate that, I will put in a delay
# of 10 seconds.
#We will use this generator function to find all possible permutations of the indicies of our matrix. The number of possible permutations in this case goes into the billions, and we don't want to store all of them before we examine them - it will take up too much memory. This is why we want to use a generator function - a function that returns an object which can then, using the special yield keyword, be iterated over to return as many results at a time as we want.

def all_possible_permutations(mylist):
    #Base case, if list only has one item left...
	if len(mylist) <= 1:
		yield mylist
	else:
        #Using the perm built-in function, we iterate recursively over mylist, finding the permutations on either side of the first item in each iteration as we place it in each index in the list.  
		for perm in all_possible_permutations(mylist[1:]):
			for i in range(len(perm)+1):
				yield perm[:i] + mylist[0:1] + perm[i:]

#Read file, create a list of strings using the readlines() function, and strip the newline character at the end.
file = open("/home/nancy/zodiak/python/mat06-nospaces.txt", "r")
with open("/home/nancy/zodiak/python/mat06-nospaces.txt", "r") as file:
	listofstrings = file.readlines()
newlist = []
for str in listofstrings:
	newlist.append(str.rstrip("\n"))
#Find the number of columns so we can figure out how many indicies we have and create a list of the indices.
numberofcolumns = len(newlist[0])
templist = range(numberofcolumns)
listofindices = []	
for i in templist:
	listofindices.append(i)
#For each possible permutation, add scrambled row to string, only looking at the first 50 permutations so as to not take up too much memory. 
genobjstr = all_possible_permutations(listofindices)
counter = 0
counterj = 0
for j in genobjstr:
	counteri = 0
	counterk = 0	
	tempstring = ""
	finalstring = ""
	counterj += 1
	# print ("counterj = ")
	# print (counterj)
	# print ("j = ")
	# print (j)
	for i in newlist:
		counteri += 1
		# print ("counteri = ")
		# print (counteri)
		# print ("i = ")
		# print (i)
		for k in j:
			counterk += 1
			# print ("counterk = ")
			# print (counterk)
			# print ("k = ")
			# print (k)
			# print (i[k])
			tempstring += (i[k])
			# print (tempstring)
#If a desired word or letter grouping is in one of the scrambled strings, allow the user to examine it and then decide whether or not to continue.
	if "EA" in tempstring:
		finalstring += tempstring
		counter += 1
		print (finalstring)
		print (counter, "word(s)")
		answer = input("Another permutation? Press y for yes and n for no and then press enter: ") 
		if answer == "y":
			continue
		else:
			break		

time.sleep(10)
end_time = time.time()
run_time_sec = end_time - start_time
run_time_hours = run_time_sec/3600.0
run_time_days = run_time_hours/24.0
print("Runtime is", run_time_sec, "sec =", run_time_hours, "hours =", run_time_days, "days")
