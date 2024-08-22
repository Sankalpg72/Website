from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')

if __name__ == "__main__":
  app.run(host = "0.0.0.0",debug = True)

#In Flask, the default convention for locating HTML templates is to look in a folder named templates. This is built into Flask's template rendering system. Here’s why using template instead of templates didn’t work:

# Flask Convention: Flask expects the directory where templates are stored to be named templates. This is a convention followed by the Flask framework. If the directory name is different, Flask won’t be able to locate the templates.

