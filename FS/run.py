from flask import Flask, request, Response
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
    data = {
            "TYPE": "A",
            "NAME": hostname,
            "VALUE": ip,
            "TTL": 10
        }
    data = json.dumps(data)
    print("data: ", data)
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.sendto(data.encode(), ('127.0.0.1', as_port))
        # print (s.recv(1024).decode())
        client_socket.close()
    except socket.error as e:
        print(e)
        response = {
            "message": "Bad Request",
            "status_code": 400
        }
        return Response(response=json.dumps(response), status=400, mimetype='application/json')
    response = {
        "status_code": 201,
        "hostname": hostname,
        "ip": ip,
        "as_ip": as_ip,
        "as_port": as_port
        }
    return Response(response=json.dumps(response), status=200, mimetype='application/json')

@app.route('/fibonacci', methods = ["GET"])
def fibonacci():
    number = request.args.get('number', None)
    if number is None or number.isdigit() == False:
        response = {
            "message": "Bad Request",
            "status_code": 400
        }
        return Response(response=json.dumps(response), status=400, mimetype='application/json')
    number = int(number)
    data = [0, 1]
    if number > 2:
        for i in range (2, number):
            data.append(data[i-1] + data[i-2])
    response = {
        "status_code": 200,
        "result": data[number-1]
    }
    return Response(response=json.dumps(response), status=200, mimetype='application/json')

app.run(host='0.0.0.0',
        port=9090,
        debug=True)
