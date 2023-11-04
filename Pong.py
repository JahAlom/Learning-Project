from flask import Flask, jsonify, request #importing Flask
from datetime import datetime #importing datetime module
import socket #importing socket module
import json
app = Flask(__name__)

@app.route("/")
def index(): #Index function to return pong response, current time, and name of local machine
    now = datetime.now() #current time using datetime.now method to variable
    message = "pong" #pong response to string variable
    machine = socket.gethostname() #name of machine using socket.gethostname() method to variable
    return [str(now), message, machine]; #returns variables in list 

response = index() #index function data stored inside variable
print(response) #data of response printed

@app.route('/textcombine', methods=['POST'])
def textcombine():
    
    request_data = request.get_json() #requesting data from user
    fstMessage = request_data['firstMessage']
    secMessage = request_data['secondMessage']
    cmbMessage = fstMessage + secMessage #combined messagees
    bannedWords = ['Fail', 'Wrong', 'Bad']

    #Checks if any words in Banned Words list appears in User's Message
    for word in bannedWords :
        if (word.lower() in cmbMessage.lower()):
            return "Banned Word in Message", 400
    return jsonify(combinedMessage = (cmbMessage))

    
if __name__ == "__main__":
	app.run()
