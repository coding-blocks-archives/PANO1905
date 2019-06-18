from flask import Flask, render_template, request
import scrapper
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
  # method of request
  # query parameters
  # request body
  products = []
  if request.method == "POST":
    query = request.form["query"]
    res = scrapper.scrapSnapdeal(query)
    products += res

  return render_template("index.html", products=products)

if __name__ == "__main__":
  app.run(port = 8080, debug = True)
