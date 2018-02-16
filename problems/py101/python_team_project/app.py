from __future__ import unicode_literals
import sys
import statistics
import datetime
from collections import OrderedDict, namedtuple
from prompt_toolkit import prompt, AbortAction
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.contrib.completers import WordCompleter
import meetup.api


class CommandError(Exception):
    pass


class Command:

    def __init__(self, args):
        self.args = args
        self.clean_args = None

    def usage(self):
        return ""

    def validate_args(self, storage):
        """
        Raise CommandError if invalid
        """

    def execute(self, storage):
        return []


class NullCommand(Command):

    def usage(self):
        return "Enter a command."

    def validate_args(self, storage):
        """
        Raise CommandError if invalid
        """
        raise CommandError("Not a valid command.")

    def execute(self, storage):
        return ["Invalid Args: {}".format(self.args)]


class AddCommand(Command):

    def usage(self):
        return "Usage: add [name] [lines]"

    def validate_args(self, storage):

        args = self.args
        if not args:
            raise CommandError("No name and lines provided.")
        Args = namedtuple(
            'Args', ['name', 'lines', ])
        lines = "".join(args[-1:])
        try:
            lines = int(lines)
        except Exception:
            raise CommandError("Lines must be an integer.")
        name = " ".join(args[:-1])
        self.clean_args = Args(lines=lines, name=name)

    def execute(self, storage):
        person = {
            "name": self.clean_args.name,
            "lines": self.clean_args.lines,
            "date": datetime.datetime.now()}
        storage.people[self.clean_args.name] = person
        storage.unassigned.append(person)
        return []


class ListCommand(Command):

    def usage(self):
        return "Usage: list"

    def validate_args(self, storage):
        pass

    def execute(self, storage):
        output = []
        for name, person in storage.people.items():
            output.append("{}, {}".format(
                person['name'], person['lines']))
        output.append("Number of people: {}".format(
            storage.num_people()))
        output.append("Median line count: {}".format(
            storage.get_median_lines()))
        return output


class TeamCommand(Command):

    def usage(self):
        return "Usage: list"

    def validate_args(self, storage):
        pass

    def execute(self, storage):
        if storage.unassigned:
            storage.calculate_teams()
        print(storage.teams)
        for name, members in storage.teams.items():
            print(
                "{}: {}".format(
                    name,
                    ", ".join(m['name'] for m in members if m)))
        output = []
        return output


class Storage:

    def __init__(self):
        self.people = OrderedDict()
        self.unassigned = []
        self.teams = {}

    def validate_args_cmd(self, cmd):
        cmd.validate_args(self)

    def execute_cmd(self, cmd):
        return cmd.execute(self)

    def num_people(self):
        return len(self.people)

    def get_median_lines(self):
        lines = [x[1]['lines'] for x in self.people.items()]
        return statistics.median(lines) if lines else None

    def calculate_teams(self, size=4):
        med = self.get_median_lines()
        lower_med = [x[1] for x in self.people.items() if x[1]['lines'] <= med]
        higher_med = [x[1] for x in self.people.items() if x[1]['lines'] > med]
        i = 0

        def first_available(list1, list2):
            try:
                x = list1.pop()
            except IndexError:
                x = None

            if not x:
                try:
                    x = list2.pop()
                except IndexError:
                    x = None

            return x

        while True:
            i += 1
            name = "Group {}".format(i)
            if not lower_med and not higher_med:
                break
            team = []
            for x in range(0, size):
                team.append(first_available(lower_med, higher_med))
            self.teams[name] = team


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


def execute(storage, command_str):
    command_and_args = command_str.rstrip().split(" ")
    command = command_and_args[:1][0]
    args = command_and_args[1:]
    print("COMMAND: {} - {}".format(command, args))

    if command == "add":
        cmd = AddCommand(args)
    elif command == "list":
        cmd = ListCommand(args)
    elif command == "teams":
        cmd = TeamCommand(args)
    else:
        cmd = NullCommand(args)

    try:
        storage.validate_args_cmd(cmd)
    except CommandError as e:
        print("{}\n  {}".format(cmd.usage(), str(e)))
    else:
        output = storage.execute_cmd(cmd)
        print("\n".join(output) if output else "")

    return "You issued:" + command


def main():
    history = InMemoryHistory()

    storage = Storage()

    while True:
        try:
            command_str = prompt(
                '> ',
                completer=command_completer,
                history=history,
                on_abort=AbortAction.RETRY)
            messages = execute(storage, command_str)

            print(messages)
        except EOFError:
            break  # Control-D pressed.

    print('GoodBye!')


if __name__ == '__main__':
    main()
