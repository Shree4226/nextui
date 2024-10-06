# Python3 implementation to 
# check if N is a super-d number

# Function to check if N
# is a super-d number
def isSuperdNum(n): 
	for d in range (2, 10):
		substring = str(d) * d;
		if substring in str(d * pow(n, d)):
			return True
	return False

# Driver Code 
n = 261
if isSuperdNum(n) == True:
	print("Yes")
else :
	print("No")
