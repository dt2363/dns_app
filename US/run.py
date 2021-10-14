from flask import Flask, request, redirect, url_for
import json
app = Flask(__name__)

@app.route('/fibonacci', methods = ["GET"])
def user():
    hostname = request.args.get('hostname', None)
    fs_port = request.args.get('fs_port', None)
    number = request.args.get('number', None)
    as_ip = request.args.get('as_ip', None)
    as_port = request.args.get('as_port', None)
    if hostname == None or fs_port == None or number == None or as_ip == None or as_port == None:
        return json.dumps({"status": False, "message": "Parameter Missing"}), 400
    return json.dumps(
        {
            "hostname": {hostname},
            "fs_port": {fs_port},
            "number": {number},
            "as_ip": {as_ip},
            "as_port": {as_port},
            "message": "Parameter Missing"}), 200

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
