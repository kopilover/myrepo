# application.py
from flask import Flask, render_template
import random

application = Flask(__name__)

# list of quotes :
quotes = ["Logic will get you from A to B. Imagination will take you everywhere.",
    "There are 10 kinds of people. Those who know binary and those who don't.",
    "There are two ways of constructing a software design. One way is to make it so simple that there are obviously no deficiencies and the other is to make it so complicated that there are no obvious deficiencies.",
    "It's not that I'm so smart, it's just that I stay with problems longer.",
    "It is pitch dark. You are likely to be eaten by a grue."]


# defining a route
@application.route("/")
def home():
    # returning a response by using random to generate index to get the quote for display
    quote_index = random.randint(0,4)
    quote_str = quotes[quote_index]
    return render_template('index.html', title="Home", content=quote_str)

# running the server
if __name__ == '__main__':
    application.run(debug=True) # to allow for debugging and auto-reload
