import time
import sys
from text_strings import all_strings

print all_strings['welcome']

time.sleep(1.5)

# this variable will +1 each time player scores correctly #
cumulative_score = 1

def graceful_exit(): 
	print "This is your score: " + str(cumulative_score)
	sys.exit()

print "Are you ready?"
ready_statement = raw_input("Type yes or no: ")

if ready_statement == "no":
	print "Nevermind! Didn't think you got the guts either. I'll give you a point for participation."
	graceful_exit()
elif ready_statement != "yes":
	print "no, I don't understand what you said. Aliens are not allowed to participate here. Goodbye."
	graceful_exit()

print "Here's a challenge question: is 2 X 4 X 6 X 8...X 100 +1 divisible by a prime number under 50?"
challenge1_answer = raw_input("Type yes or no: ")

if challenge1_answer == "yes":
	print "Ah.. I see math is not your forte... It's okay... we can go on"
elif challenge1_answer == "no":
	print "You got your divisibility down. That's important to filter down to the right list of lovers. +1 point"
	cumulative_score += 1
else:
	print "I see you're not serious about this game. Do you want to exit?"
	time.sleep(1.5)
	ready_statement = raw_input("Type yes or no: ")
	if ready_statement == "no":
		print "Nevermind! Didn't think you got the guts either. I'll give you a point for participation."
		cumulative_score += 1
		graceful_exit()
	elif ready_statement != "yes":
		print "no, I don't understand what you said. Aliens are not allowed to participate here. Goodbye."
		cumulative_score += 1
		graceful_exit()

print "I'm sleepy and will continue making this game tomorrow. More contents coming!"
time.sleep(1.5)
graceful_exit()