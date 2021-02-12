from bottle import route, run, template,static_file
import sqlite3
import logging


dbhandle = sqlite3.connect('example.db')
dbhandle = sqlite3.connect('./instaboss.db');
@route('/')
def index():
    return template("""<pre>Instaboss server 0.1 
     logs dir: ./instaboss.log
     database dir: ./instaboss.db
     please see the docs
     
     
     
     </pre>""")

#serve javascript that will manage the scripted slave browsers
@route('/js/<filename>')
def staticfile(filename):
    return static_file(filename, root='./js')

#capture telemetry from scripted browser
@route('/telemetry',method="POST")
def post_telemetry():
    return template('ok')



#capture telemetry from scripted browser
@route('/task',method="POST")
def post_telemetry():
    return template('ok')



run(host='localhost', port=8080)