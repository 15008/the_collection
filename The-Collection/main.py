from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template('home.html')

@app.route("/pageone")
def pageone():
  return render_template('pageone.html')

@app.route("/pagetwo")
def pagetwo():
  return render_template('pagetwo.html')

@app.route("/contacts")
def contacts():
  return render_template('contacts.html')

if __name__ == "__main__":
  app.run(debug = True , host="0.0.0.0" , port=0000)