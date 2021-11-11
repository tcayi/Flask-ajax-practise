from flask import Flask, request, render_template, make_response
import datetime
import webbrowser
import random, string
from random import randrange

app = Flask(__name__)

@app.route('/check', methods=['GET','POST'])
def index():

    a = randrange(100)
    b = randrange(100)

    # random letter //My eventual aim isn't randomly generated data, random is to test if values can be properly sent back to frontend
    c = random.choice(string.ascii_letters)
    print(a,b,c)

    data= {"y1": a, "y2": b, "x": c}
    
    # Form the generated data into a json format
    datap = json.dumps(datap)
    print(datap)
    
    # Q: Am I supposed to use another flask route to recieve the request from the html front end?
    # If so, how to ensure that I return the updated json object to frontend? 
    # (I know a possible method is through (if request method == post), but im not sure about afterwards
    

    return render_template('test.html', a=a, b=b, c=c, datap=datap)

if __name__ == '__main__':
    app.debug = False
    webbrowser.open('http://127.0.0.1:5000/check', 0, False)
    app.run(debug=True)
