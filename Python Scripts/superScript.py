
# Function to print all subsequences of the specified string
def findPowerSet(str):
	n = len(str)
	N = int(pow(2, n))
	result = []
	for i in range(N):
		s = ""
		for j in range(n):
			if (i & (1 << j)) != 0:
				s += str[j]
		result.append(s)
	return(result)


if __name__ == '__main__':

	str = "apple"
	findPowerSet(str)





def findSet(str):
	n = len(str)
	set = []
	base_string = ""
	for i in range(len(str)):
		base_string = str[i]
		for j in range(i,len(str)):
			if j == i:
				new_string = ""
			else:
				new_string = str[j]
			set.append(base_string + new_string)
	return set



checkList = findSet(str)











## Create an array:

n = 3
arr2 = [[x for x in range(n)] for y in range(n)]


# Iterate through the array
for i in range(len(arr2)):
	ele = arr2[i]
	for j in range(len(ele)):
		print(arr2[i][j])

# Iterate through the array (alt)
for i in range(len(arr2)):
	ele = arr2[i]
	for j in range(len(arr2)):
		print(arr2[j][i])



# 2-D List of planets
planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]

# Nested List comprehension with an if condition
flatten_planets = [planet for sublist in planets for planet in sublist if len(planet) < 6]

print(flatten_planets)







#Knapsack problem


def knapSack(weights, prices, capacity):
	ppw = []
	for i in range(len(weights)):
		ppw.append(prices[i]/weights[i])
	ppw.sort(reverse = True)

	while(capacity > 0):
		
