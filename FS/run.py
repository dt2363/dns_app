from flask import Flask, request, redirect, url_for
import json
import socket
app = Flask(__name__)

@app.route('/register', methods = ["PUT"])
def register():
    content = request.get_json()
    hostname = content.get('hostname')
    ip = content.get('ip')
    as_ip = content.get('as_ip')
    as_port = int(content.get('as_port'))
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('127.0.0.1', as_port))
        data = f"TYPE=A\nNAME={hostname}\nVALUE={ip}\nTTL=10"
        print("data: ", data)
        s.send(data.encode())
        print (s.recv(1024).decode())
        s.close()
    except socket.error as e:
        print(e)
        return "Bad request", 400
    return f"{hostname} {ip} {as_ip} {as_port}"

@app.route('/fibonacci', methods = ["GET"])
def fibonacci():
    number = request.args.get('number', None)
    number = int(number)
    if number is None or type(number) != int:
        return json.dumps({"status": False, "message": "Bad Request"}), 400
    data = [0, 1]
    if number > 2:
        for i in range (2, number):
            data.append(data[i-1] + data[i-2])
    return json.dumps({"status": True, "result": data[number-1]}), 200

app.run(host='0.0.0.0',
        port=9090,
        debug=True)
