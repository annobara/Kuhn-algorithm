from flask import Flask, render_template, request
from kuhn import Graph
from form_parser import *


app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        params = parse_form(request)
        if (params):
            graph = Graph(params)
            res = graph.maxMatching()
            return render_template('results.html', res=res)
    return render_template('index.html')


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()