#!/usr/bin/env python
from flask import Flask
from flask_ask import Ask, statement, question, session
import math

app = Flask(__name__)
ask = Ask(app, '/fiboalexa')


def __gcd(a, b): 
  
    # Everything divides 0  
    if (a == 0 or b == 0): return 0
      
    # base case 
    if (a == b): return a 
      
    # a is greater 
    if (a > b):  
        return __gcd(a - b, b) 
              
    return __gcd(a, b - a) 
  
@app.route('/coprime')
def homepage():
    return 'Welcome to Coprime Number Checker'

@ask.launch
def start_skill():
    message = 'Hi. Ask two number to check if they are coprime'
    return question(message)

@ask.intent("NumberIntent")
def team_intent(first, second):
    if ( __gcd(first, second) == 1): 
        return statement("Yes")
    else: 
        return statement("No")

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
    message = 'Say number to check for fibonacci..'
    return question(message)

if __name__ == '__main__':
    app.run(threaded = True)