from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/input')
def input():
  return render_template('input.html')

@app.route('/fetch', methods=['POST'])
def output():
    YouTube_Link =  request.form['youtube']
    print(YouTube_Link)
    return render_template('input.html')



if __name__ == '__main__':
  app.run()
