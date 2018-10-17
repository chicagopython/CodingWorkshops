from flask import Flask, flash, redirect, render_template, \
     request, url_for
from peewee import *
import datetime
import logging
import re
from collections import Counter
from wtforms import Form, StringField

logger = logging.getLogger(__name__)

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'foobar'

db = SqliteDatabase('../../py101/trackcoder/to_do_list.db')

class ToDo(Model):
    task = CharField(max_length=255)
    description = CharField(max_length=255)
    timestamp = DateTimeField(default=datetime.datetime.now)
    mins = IntegerField()
    done = BooleanField(default=True)

    class Meta:
        database = db

@app.route('/tasks/', methods=['GET', 'POST'], defaults={'tasks':None})
def tasks(tasks):
    tasks = [t for t in ToDo.select()]
    return render_template('tasks.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
