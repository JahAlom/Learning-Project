from flask import Flask, jsonify, request #importing Flask
from datetime import datetime, date #importing datetime module
from flask_caching import Cache
import socket #importing socket module
from bannedWordChecker import hasBannedWords
from bs4 import BeautifulSoup
import urllib.parse
import json
import requests

config = {
     "DEBUG": True,
     "CACHE_TYPE": "SimpleCache",
     "CACHE_DEFAULT_TIMEOUT": 300
}
app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)

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


    cache_key = f"combined_message_{fstMessage}_{secMessage}"
    result_cach = cache.get(cache_key)
    if result_cach is not None:
         return jsonify(combinedMessage = (cmbMessage))



    #Checks if any words in Banned Words list appears in User's Message
    isbanned = hasBannedWords(fstMessage,secMessage)
    if isbanned:
        return "Banned Word in Message", 400
    cache.set(cache_key,cmbMessage)
    return jsonify(combinedMessage = (cmbMessage))
    

@app.route("/google", methods = ['GET', 'POST'])
def google():
    search = request.args.get('q')
    q = {'q': search}
    r = requests.get("https://google.com/search", params=q)

    #parse HTML for title of search results and return
    soup = BeautifulSoup(r.text, 'html.parser')
    titles = soup.find_all('h3')

    results = []
    for title, h3_tag in zip(titles, titles):
         a_tag = h3_tag.find_parent('a')
         if a_tag:
              link = a_tag.get('href', '')
              link = urllib.parse.unquote(link.replace('/url?q=', ''))
              result = {'title': str(title.text), 'url': str(link)}
              results.append(result)
    return jsonify(results)
    
@app.route('/mlb/games', methods=['GET','POST'])
def mlb():

    request_data = request.get_json()
    startDate = request_data['startDate']
    endDate = request_data['endDate']

    if startDate and endDate == '':
         today = date.today()
         stats = requests.get(f"https://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&startDate={today}&endDate={today}")
         data = stats.json()
         return data
    else:
        stats = requests.get(f"https://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&startDate={startDate}&endDate={endDate}")
        data = stats.json()
        return data
    
    
if __name__ == "__main__":
	app.run(port = 8000)
