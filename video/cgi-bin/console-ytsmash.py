#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# enable debugging
import cgitb
cgitb.enable()
import cgi
import subprocess
from subprocess import Popen, PIPE, STDOUT
from flask import Flask, Response, request, render_template, redirect, url_for
import time

app = Flask(__name__)

@app.route('/out/<searchterms>/<number>/<s1>')
def out(searchterms, number, s1):
  def output():
    yield """<html><body style='color:MediumSeaGreen;'><h1><div id='data' style='text-align: center;'>nothing received yet...for </div></h1><script>var div = document.getElementById('data');</script></body></html>"""
    p = subprocess.Popen('sudo python3 /var/video/cgi-bin/ytsmash.py '+str(searchterms)+' '+str(number)+' '+str(s1), shell=True, stdout=subprocess.PIPE, stderr=STDOUT)
    while True:
        out = ((p.stdout.readline()).strip()) 
        out =str(out)
        if out != "b''":
            print (out)
            yield """<html><body><h1><script>div.innerHTML = "OUTPUT: """+out+""" " ;</script></h1></body></html>"""
            time.sleep(.27)
    else:
        yield """<html><body><h3>Watch Movie After Output is done...</h3><form action='https://lftr.biz:8080/movies/output2.mp4'>
<input type="submit" value="Watch Movie!!!"></form></body></html>"""
  return Response(output())

@app.route('/ytsmash',methods = ['POST', 'GET'])
def searchterms():
    if request.method == 'POST':
        searchterms = request.form['searchterms']
        number = request.form['number']
        s1 = request.form['s1']
        return redirect(url_for('out',searchterms = searchterms, number = number, s1 = s1))
    else:
        searchterms = request.args.get('searchterms')
        number = request.args.get('number')
        s1 = request.args.get('s1')
        return """<html><style>body {background: #1339de;} #data { text-align: center; }</style><body>
<h1>YouTube Smash-up Compiler!!!</h1><br><br>
<form method ='POST'>
   Select Search Type...<br>
   Search Type:  <input type="radio" id="s1" name="s1" value="general"><label for="s1">General YouTube Search</label><br>
   Search Type:  <input type="radio" id="s1" name="s1" value="channel"><label for="s1">Channnel YouTube Search</label><br>
   Search Terms: <input type="text" name="searchterms" id="searchterms">
   Query Length: <input type="number" name="number" id="number" value="4">
   <input type="submit" value="Make a YouTube SmashUp!!!">
</form></body></html>"""

if __name__ == "__main__":  
    app.run(host='0.0.0.0', debug=True, ssl_context=('/var/security/lftr.biz.crt', '/var/security/lftr.biz.key'), port=8000)
