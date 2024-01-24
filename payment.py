from flask import flask

app = flask(__name__)

def calculate (a, b):
    c = a+b
    return c

#new line

@app.route("/") #function which tells that the next coming function will be on HTTP request
def index():

    return "This is a credit card page! Please pay %s USD"%(calculate(10,20))



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)