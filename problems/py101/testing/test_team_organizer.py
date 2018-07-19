from team_organizer import Person, Organizer
import pytest
import random
import string


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


@pytest.mark.skip(reason="broken test needs fixing")
def test_add_a_person_with_lower_than_median(organizer):
    median_lines = organizer.median_lines()
    less_than_median_lines = median_lines - 1000
    p = Person('a', '@a', less_than_median_lines)
    organizer.add(p)

    assert 1/0 == 0
    assert organizer.d[0] == p
    pass


# Pytest Fixture: https://docs.pytest.org/en/latest/fixture.html
@pytest.mark.skip(reason="broken test needs fixing")
@pytest.mark.parametrize("test_input,expected", [
    ([Person('a', '@a', 1),
     Person('b', '@b', 2),
     Person('c', '@c', 3),
     Person('d', '@d', 4)], 1),
    ([Person('a', '@a', 1)], 1)
])
def test_count_number_of_teams(organizer, test_input, expected):
    for p in test_input:
        organizer.add(p)
    assert len(organizer.teams()) == expected


def test_add_a_person_who_has_never_written_code_before(organizer):
    organizer.add(Person('a', '@a', 0))
    pass


def test_add_two_person_with_same_name_but_different_slack_handles(organizer):
    pass


def test_add_a_person_who_supplied_negative_lines_of_code(organizer):
    'Behavior not implemented. Decide & implement the behavior & the test.'
    pass


def test_add_same_person_twice():
    'Behavior not implemented. Decide & implement the behavior & the test.'
    pass
