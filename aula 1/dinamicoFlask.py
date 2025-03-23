from flask import Flask
import random

app = Flask(__name__)

@app.route('/')

def hello():
    lista = []
    for numero in range(0,6):
        lista.append(random.randrange(1,60))
    return 'numeros da mega' + str(sorted(lista))
 
 
if __name__ == '__main__':
	app.run()