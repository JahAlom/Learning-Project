from flask import Flask, jsonify, request #importing Flask
from datetime import datetime #importing datetime module
import socket #importing socket module
from bannedWordChecker import hasBannedWords
from bs4 import BeautifulSoup
import json
import requests
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

    #Checks if any words in Banned Words list appears in User's Message
    isbanned = hasBannedWords(fstMessage,secMessage)
    if isbanned:
        return "Banned Word in Message", 400
    return jsonify(combinedMessage = (cmbMessage))

@app.route("/google", methods = ['GET', 'POST'])
def google():
    search = request.args.get('q')
    q = {'q': search}
    r = requests.get("https://google.com/search", params=q)

    #parse HTML for title of search results and return
    soup = BeautifulSoup(r.text, 'html.parser')
    titles = soup.find_all('h3')
    url = soup.find_all('a')

    results = []
    for title, link in zip(titles,url):
         result = {'Title': str(title.text), 'URL': link.get('href')}
         results.append(result)
    return jsonify(results)
    


if __name__ == "__main__":
	app.run(port = 8000)
