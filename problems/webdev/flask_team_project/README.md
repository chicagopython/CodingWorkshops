The organizers of Project Nights need your help! Grouping people for project night team project is such a manual task! Why do it manually, when we can automate it? We open the problem to you.
We want a person (henceforth gatekeeper) to record project night preferences of people as they walk through the door. There are two simple questions in order to assign people into groups. Last assignment you built a command line program for this. In this exercise we would like enhance it to be a flask app.

Lets first set up the environment.


    pip install flask
    pip install Flask-WTF
    pip install meetup-api

How to create a basic Flask app: Follow the instructions [here](http://flask.pocoo.org/docs/0.11/quickstart/).

    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    if __name__ == '__main__':
        app.run(debug=True)

Now run it!

    python app.py

Next let’s hook up meetup.com api using the API key you get from https://secure.meetup.com/meetup_api/key/

    from flask import Flask
    app = Flask(__name__)
    import meetup.api

    def get_names():
        client = meetup.api.Client(‘get your key’)

        rsvps=client.GetRsvps(event_id='235484841', urlname='_ChiPy_')
        member_id = ','.join([str(i['member']['member_id']) for i in rsvps.results])
        members = client.GetMembers(member_id=member_id)

        foo=''
        for member in members.results:
            try:
                foo+='{0}, {1}, {2}'.format(member['name'], member['id'], member['photo']['thumb_link'])
            except:
                pass # ignore those who do not have a complete profile

        return foo

    @app.route('/')
    def hello_world():
        return get_names()

    if __name__ == '__main__':
        app.run(debug=True)



Using some WTF templates, you can make it look like below (hopefully prettier than this). Remember that you should ask which Projects they would like work on and how many lines of Python they’ve written (in lieu of any better assessment). You may want to ask for more:



This UI allows the gatekeeper to scroll through the RSVP list, and check in people for solo or team projects. In addition he/she would also ask the number of lines of code (Python or similar) an attendee has written till date.  We are looking for a rough estimate for line count, but the entries should be a valid number.
After checkin of all the attendees is complete - the gatekeeper can hit submit to kick off the grouping algorithm. For this you will need to know how to a form submit is done using flask.

The algorithm groups those willing to attend a team-project together into groups of four and displays each group with a team name and a room name. Ideally you should be able to import the algorithm from the work you did last project night.

The criteria for the groups are:
* 2 person who have written less than median lines of code
* 2 person who has written more than written more than median


### Bonus questions
* Provide the text search area, that allows searching by attendee
* If the search finds a match, it shows a page for the user with his/her name, choice for solo/team project, and input for line count. Finally a button to hit submit to insert the recorded info.
* Make it pretty
* Do error validation
* Deploy this on a cloud hosting
* Integrate this solution in chipy.org
