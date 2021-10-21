from flask import Flask, request, render_template, make_response
import datetime
import random, string
from random import randrange

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():

    a = randrange(100)
    b = randrange(100)

    # random letter
    c = random.choice(string.ascii_letters)
    print(a,b,c)

    data= {"y1": a, "y2": b, "x": c}

    return render_template('test.html', a=a, b=b, c=c, data=data)

if __name__ == '__main__':
    app.run(debug=True)