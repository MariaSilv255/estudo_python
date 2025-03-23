from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello():
	return 'meu site estatico com flask'
if __name__ == '__main__':
	app.run()