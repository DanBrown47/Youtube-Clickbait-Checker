from flask import Flask, render_template, request


# Strictly related to the web mechanism is written out her all else are called from
# src/ using the OS library [Hope it works for you]

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
    # Need to reverify if it is a youtube link or not
    # To test the same, I'm embedding the youtube link into the web
    return render_template('input.html') # Change the same to a dashboard



if __name__ == '__main__':
  app.run()
