# Mentorship Program Web Project

## Objective
All developers in the modern day need to understand web technologies at some level. Whether you're interacting with a Jupyter notebook or querying a web api, understanding how a CLIENT requests information from a SERVER and to see how the SERVER produces its response is incredibly valuable.


## Overview
We will make a web app that serves as both a CLIENT to an external api (exchangeratesapi.io). This app will show conversion rates for currencies, and then add some more complex data.

 
## Prerequisites
For this project we recommend all use Atom (or Sublime) to write code and a shell/terminal to execute the program. All instructions will be given assuming a Python 3.6 install.

You should probably have the [Flask documentation](http://flask.pocoo.org/docs/1.0/quickstart/) up as we go through the exercise.


## Initial Setup

Create a folder for this project: `mkdir mentorship_web && cd mentorship_web`

If you are using Linux or OS X, run the following to create a new virtualenv

```
python3 -m venv venv
source venv/bin/activate
```

On Windows, run the following

```
python3 -m venv venv
venv\Scripts\activate
```

Install Flask, our main web-app: `pip install flask`

Create a new file called `app.py`

```
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)
```

Run your flask app: `python app.py`

It should display a link, paste that in your browser to see the running code.


## Display some Exchange Rates

Define a dictionary with three entries like the following inside your hello route:

```
exchange_rates = {
  'EUR': '...',
  'GBP': '...',
    ' 
```

Pick any currencies you want! We'll display the values as they convert to USD (because we are in Chicago). Better specify that now for clarity. Add this line just bellow your `app =` definition, we'll use it later:

```
BASE_CURRENCY = 'USD'
```

Of course, fill in the `...` with real currency values, otherwise our site is pointless! Use a tool like [X-Rates](https://www.x-rates.com/table/?from=USD&amount=1) to look up the currency conversions.

Now update the return string in the hello route to include the information about these currencies.


## Make it Beautiful
Returning strings is fine...I suppose. But I want big, beautiful HTML! Research Flask's [`render_template` function](http://flask.pocoo.org/docs/1.0/quickstart/#rendering-templates) and add some beautiful looking HTML to format your. Hint: You'll want to create a `templates/` folder in the same directory as your `app.py`, and if you aren't using a kind of loop in your template...it's going to get real tough for you later! 

Test your work by adding another currency to your `exchange_rates` dictionary and watch how your page changes.

## Refactor
Define a function right under your `BASE_CURRENCY` definition that looks like the following:

```
def exchange_rates():
  return # Move your dictionary here
```

Then replace any references in your code to use the function instead of defining the dictionary in your route!

## Automatic Data
Now comes the fun part. What if we could get the exchange rates on a live feed from a third party service? We can with [ExchangeRatesAPI.io](http://exchangeratesapi.io). This is a free api that runs over simple HTTPS! We'll have something like the following: 

```
def exchange_rates():
  response = requests.get('https://api.exchangeratesapi.io/latest')
  return # What are we going to put here now? 
```

Read up on [Requests' built in JSON Parsing](http://docs.python-requests.org/en/master/user/quickstart/#json-response-content) and try to extract the data from the API response. Your end goal is to return all of the 
currencies from this function. 

Hint: This problem is a great time to use the Python debugger ([`pdb`](https://docs.python.org/3/library/pdb.html))! Insert the following line before the `return` command and interact with your server on the command line. So cool! 

```
import pdb; pdb.set_trace()
```

### Correct Currency
Are we sure the previous step is getting us the currency in our `BASE_CURRENCY` variable? Investigate the [api docs](http://exchangeratesapi.io) to find out how you can change the base currency to the one we want.


# You DID it! Now what?
From here on out we are trusting that you can use the documentation, look for resources on your own, and come up with clever solutions to these problems. Try each one, and if you get stuck, move on to a different one! Ask for help if you want more clarification or can't think of a way to do it. 


## Information Overload
Could we provide a form that would let people get only the currency they want? I don't need every currency. We'd probably use some kind of html form. And I bet Flask has some documentation on receiving requests from the client.

e.g. Instead of `JPY->*` I only want to see `USD->GBP` or I only want to see `USD->JPY`.


## Order by Value
How could we order the currencies by the value of the currency?

e.g. If something is `.00001 USD`, lets list that last, and if something is `987654321 USD` lets list that first.


## User-Specified Base Currency
Some users of our product have complained, rightfully, that they can only get the currency listed in `USD`. We should let them specify what currency they want.

e.g. Instead of `USD->*` I want to see `CNY->*`

### Bonus: Links to each user-specified currency from the currency list
Wouldn't it be great if each currency as it appeared would link to its own currency conversion?

e.g. From the home page I could click on `JPY` to find out all of the conversions from `JPY->*`. 


## Caching
Do we really need to use an API request every time we do a call? How could we store the results of each run to avoid API abuse.