from flask import render_template,send_file
from matplotlib import pyplot as plt
import numpy as np
from io import BytesIO
from . import graphApp

'''
To draw a graph with matplotlib, must have a 2 times route. it is a trick in Flask.
Here is a sample: first call /g, then in the template will route to /fig again to do the actual drawing.
'''
@graphApp.route('/g')
def images():
    return render_template("real-graph.html")
    # return render_template("high-chart-test.html")

@graphApp.route('/fig')
def graph():
    fig = plt.figure()
    t = np.arange(0,5,0.2)
    plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
    plt.xlabel('time')
    plt.ylabel('current')
    plt.title('sample graph')
    figData = BytesIO()
    fig.savefig(figData, format='png')
    figData.seek(0)
    return send_file(figData, mimetype='image/png')

@graphApp.route('/admin')
def admin():
    return render_template("admin-sample.html")

if __name__ == "__main__":
    t = np.arange(0,5,0.2)
    plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
    plt.xlabel('time')
    plt.ylabel('current')
    plt.title('sample graph')
    plt.show()