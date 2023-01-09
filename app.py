from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/input')
def input():
  return render_template('input.html')

@app.route('/output', methods=['POST'])
def output():
  text = request.form['text']
  return render_template('output.html', text=text)

if __name__ == '__main__':
  app.run()
