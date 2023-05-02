from flask import Flask, render_template, request
from socket_code import UDP

app = Flask(__name__)

IP = '192.168.1.100'
udp = UDP(IP)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/toggle', methods=['POST'])
def toggle():
    state = request.form.get('state')
    message = f'{{"method": "setPilot", "params":{{"state": {state}}}}}'.encode()
    udp.call(message)
    return {'status': 'success'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')