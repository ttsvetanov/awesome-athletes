from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
@app.route('/index')
def hello_world():
    print "change made"
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
