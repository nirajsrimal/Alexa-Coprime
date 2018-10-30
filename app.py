#!/usr/bin/env python
from flask import Flask
from flask_ask import Ask, statement, question, session
import requests

app = Flask(__name__)
ask = Ask(app, '/')
  
def __gcd(a, b): 
  
    if (a == 0 or b == 0): return 0

    if (a == b): return a 

    if (a > b):  
        return __gcd(a - b, b) 
              
    return __gcd(a, b - a)

@app.route('/')
def homepage():
    return 'Welcome to Coprime Nmber'

@ask.launch
def start_skill():
    message = 'Hey.. Ask me whether two numbers are  coprime number or not?'
    return question(message)

@ask.intent("NumberIntent", convert = {"first" : int, "second" : int})
def number_intent(first, second):
    if (__gcd(first, second) == 1): 
        return statement("Yes, They are coprime")
    else: 
        return statement("No, They are not coprime")
    
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
    message = 'Say a number. A number is said to be a magic number, if the sum of its digits are calculated till a single digit recursively by adding the sum of the digits after every addition. If the single digit comes out to be 1,then the number is a magic number.'
    return question(message)

if __name__ == '__main__':
    app.run(threaded = True)