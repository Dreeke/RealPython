# ---- Flask Hello World ---- # 2
# import the Flask class from the flask module
from flask import Flask

# create the application object
app = Flask(__name__)

app.config["DEBUG"] = True

# use decorators to link the function to a url
@app.route("/")
@app.route("/hello")
@app.route("/test/<search_query>")


def search(search_query):
	return search_query

def search():
    return "Hello"

# define the view using a function, which returns a string
def hello_world():
	return "Hello, World!"

# start the development server using the run() method
if __name__ == "__main__":
	app.run()