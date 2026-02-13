from flask import Flask, render_template, request

# Corrected the syntax here: '__name__' requires double underscores on both sides
app = Flask(__name__)

@app.route("/")
def hello_world():
    # This will look for 'index.html' inside a folder named 'templates'
    return render_template('index.html')

# Corrected the syntax here: '__name__' and '__main__' require double underscores
#if __name__ == '__main__':
    # debug=True is helpful during development to see errors in the browser

    #app.run(debug=True)
