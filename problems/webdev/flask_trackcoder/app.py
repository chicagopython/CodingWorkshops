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


class ToDoForm(Form):
    todo = StringField('Task')
 

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = ToDoForm(request.form)
    if request.method == 'POST':
        task, mins, description = form.todo.data.split(',')
        ToDo.create(task=task, mins=mins, description=description)
        flash('Thanks for registering')
        return redirect(url_for('/tasks'))
    return render_template('tasks.html', form=form)


@app.route('/tasks/', methods=['GET', 'POST'], defaults={'task':''})
@app.route('/tasks/<task>', methods=['GET', 'POST'])
def tasks(task):
    logging.debug(f"{task} was received.")
    if task:
        tasks = [t for t in ToDo.select().where(ToDo.task==task)]
    else:
        tasks = [t for t in ToDo.select()]
    return render_template('tasks.html', tasks=tasks)


@app.route('/search/<hashtag>', methods=['GET', 'POST'])
def search(hashtag):
        tasks = [t for t in ToDo.select().where(ToDo.description.contains(hashtag))]
        return render_template('tasks.html', tasks=tasks)


@app.context_processor
def hashtags():
    def top_tags():
            c=Counter()
            descs = (t.description for t in ToDo.select().where(ToDo.description.contains("#")))
            for desc in descs:
                x = re.findall(r"#(\w+)", desc)
                c+=Counter(x)
            logging.info(c)
            return c
    return {'hashtags':top_tags}


@app.context_processor
def effort():
    x = {t.task:t.mins for t in ToDo.select(fn.SUM(ToDo.mins).alias('mins'), ToDo.task).group_by(ToDo.task)}
    return x

if __name__ == '__main__':
    app.run(debug=True)
