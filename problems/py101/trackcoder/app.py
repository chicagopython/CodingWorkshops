from __future__ import unicode_literals
import sys

from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.completion import WordCompleter
from peewee import *
import datetime
import click

command_completer = WordCompleter(['add', 'show'], ignore_case=True)

db = SqliteDatabase('to_do_list.db')


class ToDo(Model):
    task = CharField(max_length=255)
    description = CharField(max_length=255)
    timestamp = DateTimeField(default=datetime.datetime.now)
    mins = IntegerField()
    done = BooleanField(default=True)

    class Meta:
        database = db


def initialize():
    """Connect to database, create tables if they don't exist"""
    db.connect()
    db.create_tables([ToDo], safe=True)

def parse(input):
    """
        a b 10 first blog post
        a c 10 finished cli
        a p 120
    """
    input = input.strip()
    cmd, task, mins, description, done = ['']*5
    try:
        cmd, task, mins, *description, done = input.split()
        description = ' '.join(description)
        if done == 'False':
            done = False
        return cmd, task, mins, description, done
    except Exception as e:
        print('this is continuing to fail and we do not know why')
        print(e)
        return input, task, mins, description, done


def add(**kwargs):
    try:
        ToDo.create(task=kwargs['task'],
                    mins=kwargs['mins'],
                    description=kwargs['description'],
                    done=kwargs['done'])
    except Exception:
        print("Please check your ego")



def show(**kwargs):
    total = {}
    for t in ToDo.select():
        print(t.task, t.description, t.mins, t.done)
        if t.task in total:
            total[t.task]+=t.mins
        else:
            total[t.task]=t.mins
    for k,v in total.items():
        print('{} minutes spent {}'.format(v,k))



def execute(**kwargs):
    cmds = {
        'add': add,
        'show': show
    }

    cmds.get(kwargs['cmd'])(**kwargs)


@click.command()
@click.option('--interactive', '-i', help='needs some help text', is_flag=True, default=False)
@click.option('--show', '-s', help='needs some help text', is_flag=True, default=False)
@click.option('--add', '-a', nargs=4, type=(click.STRING, int, click.STRING, bool), default=(None, None, None, False))
def main(interactive, add, show):
    initialize()

    if interactive:
        history = InMemoryHistory()
        session = PromptSession()

        while True:
            try:
                text = session.prompt('% ')
            except KeyboardInterrupt:
                continue
            except EOFError:
                break
            else:
                cmd, task, mins, description, done = parse(text)
                execute(cmd=cmd, task=task, mins=mins, description=description, done=done)
    elif show:
        execute(cmd='show')
    else:
        task, mins, description = add
        execute(cmd='add', task=task, mins=mins, description=description, done=done)
    print('GoodBye!')


if __name__ == '__main__':
    main()
