from flask import Flask, request, Response
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
        response = {
            "message": "Bad Request",
            "status_code": 400
        }
        return Response(response=json.dumps(response), status=400, mimetype='application/json')
    response = {
        "status_code": 200,
        "hostname": hostname,
        "fs_port": fs_port,
        "as_ip": as_ip,
        "as_port": as_port,
        "number": number
        }
    return Response(response=json.dumps(response), status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0',
        port=8080,
        debug=True)
