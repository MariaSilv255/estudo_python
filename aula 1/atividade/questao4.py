from flask import Flask
from datetime import date

app = Flask(__name__)
@app.route('/')

def tipoDia():
    dia = date.today().day
    if(dia % 2 == 0):
        return f'hoje é dia {dia} e ele é par'
    else:
        return f'hoje é dia {dia} e ele é impa'

if __name__ == '__main__':
	app.run()