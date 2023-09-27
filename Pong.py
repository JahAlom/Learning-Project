from flask import Flask #importing Flask
from datetime import datetime #importing datetime module
app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.now()
    return str(now)
    
if __name__ == "__main__":
	app.run()
