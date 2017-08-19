from team_organizer import OrganizerShell, Person, Organizer
import pytest
import random
import string


# Pytest Fixture: https://docs.pytest.org/en/latest/fixture.html

@pytest.fixture
def person():
    ''' Factory function that returns a function to get new Person '''
    def rand_data_person():
        name = ''.join(random.sample(string.ascii_lowercase, 3))
        handle = '@' + name
        lines = random.randint(0, 100000)
        return Person(name, handle, lines)
    return rand_data_person


@pytest.fixture
def organizer(person):
    '''Uses the person fixture factory to create an organizer
    and adds 4 persons to it.'''
    org = Organizer()
    for _ in range(4):
        org.add(person())

    return org


def test_add_person_with_higher_than_median(organizer):
    median_lines = organizer.median_lines()
    more_than_median_lines = median_lines + 1000
    p = Person('a', '@a', more_than_median_lines)
    organizer.add(p)

    assert organizer.d[len(organizer.d) - 1] == p


def test_add_a_person_with_lower_than_median(organizer):
    print(organizer.d)
    pass


def test_add_a_person_who_has_never_written_code_before(organizer):
    print(organizer.d)
    pass


def test_add_a_person_who_supplied_negative_lines_of_code(organizer):
    'Behavior not implemented. Decide & implement the behavior & the test.'
    pass


def test_add_two_person_with_same_name_but_different_slack_handles(organizer):
    pass


def test_add_same_person_twice():
    'Behavior not implemented. Decide & implement the behavior & the test.'
    pass


# TODO
@pytest.fixture
def shell(person):
    shell = OrganizerShell()
    return shell


def test_print_cmd(capsys, shell):
    pass
