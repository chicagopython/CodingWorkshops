from __future__ import unicode_literals
import sys

from prompt_toolkit import prompt, AbortAction
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.contrib.completers import WordCompleter
import meetup.api


def get_names():
    client = meetup.api.Client('3f6d3275d3b6314e73453c4aa27')

    rsvps = client.GetRsvps(event_id='239174106', urlname='_ChiPy_')
    member_id = ','.join([str(i['member']['member_id']) for i in rsvps.results])
    members = client.GetMembers(member_id=member_id)

    names = []
    for member in members.results:
        try:
            names.append(member['name'])
        except Exception:
            pass  # ignore those who do not have a complete profile

    return names


command_completer = WordCompleter(['add'], ignore_case=True)


def execute(command):
    return "You issued:" + command


def main():
    history = InMemoryHistory()

    while True:
        try:
            text = prompt('> ',
                          completer=command_completer,
                          history=history,
                          on_abort=AbortAction.RETRY)
            messages = execute(text)

            print(messages)
        except EOFError:
            break  # Control-D pressed.

    print('GoodBye!')


if __name__ == '__main__':
    main()
