import random
# Generate a floor of blocks with random 0 and 1
# floor -> list
def rand_stack():
	stack = []
	for i in range(3):
		floor = []
		for j in range(9):
			floor.append(random.randint(0,1))
		stack.append(floor)

	return stack

# Detect a floor satisfy mirror-different or not
def judge_stack(stack):
	s1 = [False,False,False]
	s2 = [False,False,False]
	flag = False
	# Check for mirror in-variant and rotation in-variant
	for floor in stack:
		i=0
		if (floor[0]==floor[6] and floor[1]==floor[7] and floor[2]==floor[8]):
			s1[i] = True
		if (floor[0]==floor[8] and floor[1]==floor[7] and floor[2]==floor[6] and floor[3]==floor[5]):
			s2[i] = True
		i+=1

	flag1 = s1[0] and s1[1] and s1[2]
	flag2 = s2[0] and s2[1] and s2[2]
	if flag1 or flag2 == True:
		flag = True

	return flag

# Detect if a stack satisfy shape and numeric conditions 
def detector(stack):
	invariant = judge_stack(stack)
	count = 0
	# Loop through every elements
	for i in range(3):
		for j in range(9):
			# Count for number of blocks
			if stack[i][j] == 1:
				count += 1
	return invariant, count

# Convert the stack in list into a string
def list_parser(stack):
	line = ""
	for i in range(3):
		for j in range(8):
			line += str(stack[i][j])
			line += ','
		line += str(stack[i][8])
		line += ';'
	line += str(10) + '\n'
	return line

# Generate data by given number
def data_generate(num):
	collection = []
	for i in range(num):
		s = rand_stack()
		flag, count = detector(s)
		if (flag == False and count >= 11):
			line = list_parser(s)
			collection.append(line)
	# Remove same stacks created due to the randomization
	unique_stack = set(collection)
	# 4000dataset, split by 500 for each part
	for i in range(0,4500,500):
		temp_file = open("test_data_" + str(i) + ".txt",'w')
		unique_list_stack = list(unique_stack)
		for stack in unique_list_stack[i-500:i]:
			temp_file.write(stack)
		temp_file.close()

	f = open("test_data_" + str(len(unique_stack)) + ".txt", 'w')
	for stack in unique_stack:
		f.write(stack)
	f.close()

data_generate(12000)