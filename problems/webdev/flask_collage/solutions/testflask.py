from flask import Flask
app = Flask(__name__)
import meetup.api

def get_names():
    client = meetup.api.Client('3f6d3275d3b6314e73453c4aa27')

    rsvps=client.GetRsvps(event_id='235484841', urlname='_ChiPy_')
    member_id = ','.join([str(i['member']['member_id']) for i in rsvps.results])
    members = client.GetMembers(member_id=member_id)

    foo=''
    for member in members.results:
        try:
            
            foo+='''<img src={2}><br>
            {0}<br>
            <input type="radio" name="project" value="solo" checked> Solo<br>
            <input type="radio" name="project" value="team"> Team<br>
            Line count: <input type=text>
            <br><br>'''.format(member['name'], member['id'], member['photo']['thumb_link'])
        except:
            pass # ignore those who do not have a complete profile

    return foo

@app.route('/')
def hello_world():
    html = '<form>' + get_names() + '<input type=submit></form>'
    return html

if __name__ == '__main__':
    app.run(debug=True)




