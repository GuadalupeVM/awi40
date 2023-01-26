import web

urls = (
    '/', 'Formulario'
)
app = web.application(urls, globals())

render = web.template.render('templates')


class Formulario(object):
    def GET(self):
        
        return render.formulario()

    def POST(self):
          form= web.input()
          return form["nombre2"]
          

if __name__ == "__main__":
    # web.confing.debug = False
    app.run()
