from flaskblog import create_app

'''see migal green burg talk about imports'''

app = create_app()

if __name__ == ('__main__'):
	app.run(debug = True)