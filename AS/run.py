from flask import Flask

app = Flask(__name__)




app.run(host='0.0.0.0',
        port=53533,
        debug=True)