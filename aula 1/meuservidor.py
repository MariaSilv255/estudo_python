import cherrypy

class MinhaPrimeiraPagina():
    def index(self):
        return "<h2>Assim sera nutela</h2>"
    index.exposed = True
    
cherrypy.quickstart(MinhaPrimeiraPagina())