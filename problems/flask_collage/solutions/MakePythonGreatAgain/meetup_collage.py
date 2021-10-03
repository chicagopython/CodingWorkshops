from flask import Flask, render_template
import meetup.api


API_KEY = '4572b1a352e2d564c687e3547541a67'


app = Flask(__name__)
client = meetup.api.Client(API_KEY)

rsvps = client.GetRsvps(event_id = '235484841', urlname = '_ChiPy_')
member_id = ','.join([str(result['member']['member_id']) for result in rsvps.results])
members = client.GetMembers(member_id = member_id)

class Member:
	def __init__(self, nameIn, photoIn):
		self.name = nameIn
		self.photo = photoIn

def get_member_list():
	member_list = []
	for member in members.results:
		try:
			# print('{0},{1},{2}'.format(member['name'], member['id'], member['photo']['thumb_link']))
			# print(member['photo']['thumb_link'])
			# photos.append(str(member['photo']['thumb_link']))
			member_list.append(Member(nameIn = str(member['name']), photoIn = str(member['photo']['thumb_link'])))
		except:
			pass # ignore those who do not have a complete profile
	return member_list


@app.route('/')
def index():
	member_list = get_member_list()
	print(member_list[0].name, member_list[0].photo)
	return render_template('index.html', members = member_list)

def main():
	app.run(debug = True)


if __name__ == '__main__':
	main()