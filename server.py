from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

counts = 0


@app.route('/request-counter')
def request_counter():
    global counts
    counts += 1
    return render_template('request-counter.html', counts=counts)


if __name__ == '__main__':
    app.run()
