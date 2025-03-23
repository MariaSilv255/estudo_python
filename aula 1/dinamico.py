import cherrypy
from datetime import date

class MinhaPrimeiraPaginaDinamica():
    def index(self):
        dia = str(date.today().day)
        mes = str(date.today().month)
        return f"hoje é dia:{dia};{mes}"
    index.exposed = True
    
cherrypy.quickstart(MinhaPrimeiraPaginaDinamica())