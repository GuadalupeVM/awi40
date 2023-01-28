import web
from datetime import datetime

urls = (
    '/(.*)', 'Visitas'
)
app = web.application(urls, globals())
render = web.template.render('templates')

class Visitas:
    def GET(self, nombre):
        try:
            cookie = web.cookies()
            visitas = "0"
            fecha=datetime.today().strftime('%Y-%m-%d')
            hora=datetime.today().strftime('%H:%M')
            print(cookie)


            if fecha:
                web.setcookie("Fecha",fecha,expires="", domain=None)
            else:
                
                web.setcookie("Fecha",fecha,expires="", domain=None)
            
            if hora:
                web.setcookie("Hora",hora,expires="", domain=None)
            else:
                
                web.setcookie("Hora",hora,expires="", domain=None)


            if nombre:
                web.setcookie("nombre",nombre,expires="", domain=None)
            else:
                nombre = "Anonimo"
                web.setcookie("nombre",nombre,expires="", domain=None)

            if cookie.get("visitas"):
                visitas = int(cookie.get("visitas"))
                visitas += 1
                web.setcookie("visitas", str(visitas), expires="", domain=None)
            else:
                web.setcookie("visitas", str(1), expires="", domain=None)
                visitas = "1"
            return render.cookies({'visitas':str(visitas), 'nombre':nombre, "fecha":str(fecha), "hora":str(hora)})
            # return "Visitas " + str(visitas) + "\nNombre " + nombre + " \nFecha " + str(fecha) + " \nHora " + str(hora)
        except Exception as e:
            return "Error " + str(e.args)





if __name__ == "__main__":
    app.run()