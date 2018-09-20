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
    cmd, task, mins, dispcription = ['']*4
    try:
        cmd, task, mins, *description = input.split()
        description = ' '.join(description)
        return cmd, task, mins, description
    except ValueError:
        return input, task, mins, dispcription


def add(**kwargs):
    ToDo.create(task=kwargs['task'],
                mins=kwargs['mins'],
                description=kwargs['description'])


def show(**kwargs):
    for t in ToDo.select():
        print(t.task, t.description, t.mins, t.done)


def execute(**kwargs):
    cmds = {
        'add': add,
        'show': show
    }

    cmds.get(kwargs['cmd'])(**kwargs)


@click.command()
@click.option('--interactive', '-i', help='needs some help text', is_flag=True, default=False)
@click.option('--show', '-s', help='needs some help text', is_flag=True, default=False)
@click.option('--add', '-a', nargs=3, type=(click.STRING, int, click.STRING), default=(None, None, None))
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
                cmd, task, mins, description = parse(text)
                execute(cmd=cmd, task=task, mins=mins, description=description)
    elif show:
        execute(cmd='show')
    else:
        task, mins, description = add
        execute(cmd='add', task=task, mins=mins, description=description)
    print('GoodBye!')


if __name__ == '__main__':
    main()
