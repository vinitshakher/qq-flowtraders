##################################################################################
##################################################################################
## Template file for problem 1. 						##
## First, fill in your answer logic below					##
##################################################################################
#                                LOGIC GOES BELOW                     		#
##################################################################################
#Each roll has equal probality of 1/6 or 0.166~0.17.
#So the total expexted pay off is equals to 0.17*1+0.17*2+0.17*3+0.17*4+0.17*5+0.17*6 which comes out to be 3.57.
# We keep rolling the dice untill we get the value of Expected Pay off greater then 3.57.
# once We get 6 in the initial roll  we stop the program and return the sum value of the program.
#
##################################################################################
##################################################################################
## You have to fill in two functions BELOW 					##
## Both take in input n = number of sides in the die 				##
## 										##									##
## 1. findSumDieRoll(n)	: Return expected value of sum 				##
## 2. findNumberOfRolls(n)  : Return expected value of number of rolls 		##
## 										##									##
## For both, you only have to fill in the math function where indicated     	##
## 										##									##
## You can run this template file to see the output of your functions       	##
## for a 6 sided die.								##
## Simply run: `python problem1_template.py`                            	##
## You should see the output printed once your program runs.                	##
##                                                                          	##
## DO NOT CHANGE ANYTHING ELSE BELOW. ONLY FILL IN THE LOGIC.      		##
##                                                                          	##
## Good Luck!                                                               	##
##################################################################################
##################################################################################


def findSumDieRoll(n):
	##################################
	##          FILL ME IN          ##
	##################################
	# n is a float
	sumRolls = n/2 # Replace me with your answer

	return round(sumRolls, 2)

def findNumberOfRolls(n):
	##################################
	##          FILL ME IN          ##
	##################################
	# n is a float
	numRolls = n/2	# Replace me with your answer

	return round(numRolls, 2)

if __name__ == "__main__":
	numberOfSides = 6.0
	sumOfRolls = findSumDieRoll(numberOfSides)
	numberOfRolls = findNumberOfRolls(numberOfSides)
	print('For a %i-sided die, expected value of sum: %.2f and number of rolls: %.2f'%(numberOfSides, sumOfRolls, numberOfRolls))
