Build a small web app using Flask which accepts the meetup.com event id for tonight
as a parameter and would fetch the profile pictures of all the attendees to create a
collage. [Here](https://twitter.com/Tathagata/status/746302962830540801) is an example
of such a collage.

You'll need:

 - `pip install flask`
 - `pip install Flask-WTF`
 - `pip install meetup-api`

To get you started, the following piece of code will help you fetch the thumbnail
images from meetup.com.

```python
import meetup.api
client = meetup.api.Client('your_key')

rsvps=client.GetRsvps(event_id='235484841', urlname='_ChiPy_')
member_id = ','.join([str(i['member']['member_id']) for i in rsvps.results])
members = client.GetMembers(member_id=member_id)

for member in members.results:
    try:
        print '{0},{1},{2}'.format(member['name'], member['id'], member['photo']['thumb_link'])
    except:
        pass # ignore those who do not have a complete profile
```

Bonus:
1. Can you include the name along with the images in your collage?

2. Currently we are accepting RSVPs on both ChiPy's site and Chicago Pythonista's
meetup page. Can you fetch the thumbnails from both the pages, eliminate the
duplicates, and merge them to generate the collage?

3. Deploy your app to a public hosting, share the link with the world!
