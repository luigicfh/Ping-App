from flask import Flask
import os


app = Flask(__name__)


def check_ping(hostname):
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        pingstatus = f"Network Communication Active for {hostname}"
    else:
        pingstatus = f"Network Communication Error for {hostname}"
    return pingstatus


@app.route('/ping')
def hello():
    ping_test = check_ping("www.google.com")
    return f"<h1>{ping_test}<h1/>"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
