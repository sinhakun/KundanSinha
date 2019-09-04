#import flask
import requests
#or pip install flask within an activated environment

from flask import Flask
app = Flask(__name__)


@app.route("/")
#@app.route("/home")
def home():
    return "<h1>10 Random Chuck Norris Jokes</h1>"


@app.route("/getjokes")
def getjokes():
    jokes_str=""
    jokes_list=[]
    request=requests.get('http://api.icndb.com/jokes/random/10')
    request_json=request.json()
    request_jokes=request_json['value']
    for i in range(len(request_jokes)):
        jokes_list=jokes_list+["Joke#"+str(i+1),request_jokes[i]['joke']]
        jokes_str="\n".join(jokes_list)
    return (jokes_str)


if __name__ == '__main__':
    #debug=False for amendments ctrl+c exit production environment
    app.run(debug=True,host='0.0.0.0')
    

    