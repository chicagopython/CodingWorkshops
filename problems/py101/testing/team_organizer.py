import cmd
import collections

Person = collections.namedtuple('Person', 'name slackhandle lines')


def parse(arg):
    try:
        name, slackhandle, lines = arg.split()
        return Person(name, slackhandle, int(lines))
    except ValueError:
        print("Invalid entry format")


class Organizer:
    def __init__(self):
        self.d = collections.deque()

    def median_lines(self):
        return self.d[len(self.d) // 2].lines

    def add(self, p):
        '''Takes a person and adds it to the queue
        if the number of lines is higher than the median
        it adds to the end else it adds to the front '''

        if len(self.d) == 0:
            self.d.append(p)
            return

        if self.median_lines() >= p.lines:
            self.d.appendleft(p)
        else:
            self.d.append(p)

    @staticmethod
    def _names(persons):
        return ', '.join(p.name for p in persons)

    def teams(self):
        ''' Makes teams by taking 2 from the front of the queue
            and two from the end of the queue till teams of 4
            can be made. '''
        teams = []
        while len(self.d) >= 4:
            ps = self.d.popleft(), self.d.popleft(), self.d.pop(), self.d.pop()
            teams.append([self._names(ps)])

        if self.d:
            teams.append(self._names(self.d))
            self.d.clear()
        return teams


class OrganizerShell(cmd.Cmd):
    intro = 'Welcome to Chicago Python Project Night Team Organizer'
    prompt = 'org> '

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.org = Organizer()

    def do_add(self, arg):
        'Adds a new user. Needs Name, slackhandle, number of lines'
        p = parse(arg)
        self.org.add(p)

    def do_print(self, arg):
        'Print the team organization'
        for team in self.org.teams():
            print(team)

    def do_exit(self, args):
        return True


if __name__ == '__main__':
    OrganizerShell().cmdloop()
