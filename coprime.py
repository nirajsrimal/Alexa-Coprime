#!/usr/bin/env python
from flask import Flask
from flask_ask import Ask, statement, question, session
import requests

app = Flask(__name__)
ask = Ask(app, '/')

 
def gcd_nums(a, b): 
  
    # Everything divides 0  
    if (a == 0 or b == 0): return 0
      
    # base case 
    if (a == b): return a 
      
    # a is greater 
    if (a > b):  
        return gcd_nums(a - b, b) 
              
    return gcd_nums(a, b - a) 
  
     
@app.route('/')
def homepage():
    return 'Welcome to Co-Prime Number Checker'

@ask.launch
def start_skill():
    message = 'Hey.. Ask me whether two numbers are Co-Prime or not?'
    return question(message)

@ask.intent("NumberIntent")
def number_intent(first, second):
    if ( gcd_nums(first, second) == 1): 
        return statement("Yes, They are Co-Prime") 
    else: 
		return statement("No, They are Co-Prime")

@ask.intent("NoIntent")
def no_Intent():
    message = 'Well that is fine...Maybe next time'
    return statement(message)

@ask.intent("AMAZON.CancelIntent")
def cancel_Intent():
    message = 'See you again...bye'
    return statement(message)

@ask.intent("AMAZON.StopIntent")
def stop_Intent():
    message = 'See you again...bye'
    return statement(message)

@ask.intent("AMAZON.HelpIntent")
def help_Intent():
    message = 'Say a number.'
    return question(message)

if __name__ == '__main__':
    app.run(threaded = True)