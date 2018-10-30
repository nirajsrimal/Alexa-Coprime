#!/usr/bin/env python
from flask import Flask
from flask_ask import Ask, statement, question, session
import math
import requests


# This script relies on Cricinfo RSS Live Feed (http://static.cricinfo.com/rss/livescores.xml)


app = Flask(__name__)
ask = Ask(app, '/')

def __gcd(a, b): 
  
    # Everything divides 0  
    if (a == 0 or b == 0): return 0
      
    # base case 
    if (a == b): return a 
      
    # a is greater 
    if (a > b):  
        return __gcd(a - b, b) 
              
    return __gcd(a, b - a) 
     
@app.route('/')
def homepage():
    return 'Welcome to Coprime Number Checker'

@ask.launch
def start_skill():
    message = 'Hey.. Ask me whether a two numbers are coprime or not?'
    return question(message)

@ask.intent("NumberIntent",convert = {"num" : int})
def number_intent(first, second):
    if ( __gcd(a, b) == 1):
        return statement("Yes, It is a Fibonacci Number")
    else: 
        return statement("Not coprime")

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