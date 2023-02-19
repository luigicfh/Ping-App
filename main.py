from flask import Flask, request
import os


app = Flask(__name__)


def check_ping(hostname):
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        pingstatus = f"Network Communication Active for {hostname}"
    else:
        pingstatus = f"Network Communication Error for {hostname}"
    return pingstatus


@app.route('/ping', methods=['GET', 'POST'])
def hello():
    if request.method == "GET":
        return """
            <p>Enter host IP or domain:<p/>
            <form action="/ping" method="POST">
                <input type="text" name="host"/>
                <input type="submit" value="Submit"/>
            <form />
        """
    elif request.method == "POST":
        ping_test = check_ping(request.form['host'])
        return f"""
            <p>{ping_test}<p/>
            <a href="/ping">Try another host<a/>
        """
    else:
        return "<p>404 not found.<p/>"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
