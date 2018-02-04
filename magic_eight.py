import random

def ask_question():
	question = input("What is your question? ")
<<<<<<< HEAD
	return(question)
=======
	return(question)

def check_question(question_in):
	if(question_in[-1] != "?"):
		print("I'm sorry, I can only answer questions.")
		return False
	else:
		return True

def random_response():
	return(random.choice(ans))

ans = ['It is certain', 'It is decidedly so', 'Without a doubt',
		'Yes definitely', 'You may rely on it', 'As I see it, yes',
		'Most likely', 'Outlook good', 'Yes', 'Signs point to yes',
		'Reply hazy try again', 'Ask again later', 'Better not tell you now',
		'Cannot predict now', 'Concentrate and ask again', "Don't count on it",
		'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

keep_going = True
while(keep_going):
	user_question = ask_question()
	
	if(user_question == "quit"):
		keep_going = False

	if(check_question(user_question) == True):
		print(random_response())
>>>>>>> check_question
