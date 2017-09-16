from __future__ import unicode_literals
import sys

from prompt_toolkit import prompt, AbortAction
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.contrib.completers import WordCompleter
import meetup.api

def get_names():
    client = meetup.api.Client('3f6d3275d3b6314e73453c4aa27')

    rsvps=client.GetRsvps(event_id='239174106', urlname='_ChiPy_')
    member_id = ','.join([str(i['member']['member_id']) for i in rsvps.results])
    members = client.GetMembers(member_id=member_id)

    names = []
    for member in members.results:
        try:
            names.append(member['name'])
        except:
            pass # ignore those who do not have a complete profile

    return names


command_completer = WordCompleter(['add', 'show'] + get_names(), ignore_case=True)

class TeamBuilder:
    def execute(self, command):
        return "You issued:" + command


def main(team_builder):
    history = InMemoryHistory()

    while True:
        try:
            text = prompt('> ',
                          completer = command_completer,
                          history=history,
                          on_abort=AbortAction.RETRY)
            team_builder.execute(text)
            messages = team_builder.execute(text)

            print(messages)
        except EOFError:
            break  # Control-D pressed.
            
    print('GoodBye!')

if __name__ == '__main__':
    team_builder = TeamBuilder()
    main(team_builder)
