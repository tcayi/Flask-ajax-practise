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

    # random letter //Actual aim isn't randomly generated, random is just a test
    c = random.choice(string.ascii_letters)
    print(a,b,c)

    data= {"y1": a, "y2": b, "x": c}
    datap = json.dumps(datap)
    print(datap)

    return render_template('test.html', a=a, b=b, c=c, datap=datap)

if __name__ == '__main__':
    app.debug = False
    webbrowser.open('http://127.0.0.1:5000/check', 0, False)
    app.run(debug=True)
