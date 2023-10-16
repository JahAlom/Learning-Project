from flask import Flask #importing Flask
from datetime import datetime #importing datetime module
import socket #importing socket module
app = Flask(__name__)

@app.route("/")
def index(): #Index function to return pong response, current time, and name of local machine
    now = datetime.now() #current time using datetime.now method to variable
    message = "pong" #pong response to string variable
    machine = socket.gethostname() #name of machine using socket.gethostname() method to variable
    return [str(now), message, machine]; #returns variables in list 

response = index() #index function data stored inside variable
print(response) #data of response printed

@app.route('/textcombine', methods=['GET','POST'])
def textcombine():
      test = "testing"
      return test;

#testresponse = textcombine()
#print(testresponse)      
    
if __name__ == "__main__":
	app.run()
