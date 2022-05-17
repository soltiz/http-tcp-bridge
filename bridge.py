
# Run this with
#    FLASK_APP=bridge flask run

from flask import Flask
from flask import request
from flask import Response
import socket


app = Flask(__name__)

@app.route("/hi")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/ingest', methods=['POST'])
def hello_data():

    incoming = request.get_data()
    if len(incoming) == 0 or incoming[-1:] != b'\n':
        incoming = incoming + b'\n'


    # print("Incoming data : " + str(incoming))
    try:
        host = socket.gethostname()
        port = 12345                   # The same port as used by the server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.sendall(incoming )
        #data = s.recv(1024)
        #print('Received', repr(data))
        s.close()
        status_code = Response(status=200)
    except Exception as e:
        return {"error": str(e)}, 500

        #status_code = Response(status=500)
    return status_code




    return "<p>" + str(data) + "</p>"

