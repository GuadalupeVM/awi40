import web

urls = (
    '/', 'Suma'
)
app = web.application(urls, globals())

render = web.template.render('templates')


class Suma(object):
    def GET(self):
        
        return render.suma()

    def POST(self):

        
        form = dict(web.input())

        # opera=web.input()
        # return form["opera"]
        if form["opera"] == "suma":

            return ("La suma de "+form["numero1"]+" + "+form["numero2"]+" = "+str(int(form["numero1"])+int(form["numero2"])))
            
        elif form["opera"] == "resta":
            return ("La resta de "+form["numero1"]+" - "+form["numero2"]+" = "+str(int(form["numero1"])-int(form["numero2"])))

        elif form["opera"] == "multi":
            return ("La multiplicacion de "+form["numero1"]+" * "+form["numero2"]+" = "+str(int(form["numero1"])*int(form["numero2"])))

        elif form["opera"] == "divi":
            return ("La division de "+form["numero1"]+" / "+form["numero2"]+" = "+str(int(form["numero1"])/int(form["numero2"])))

    

if __name__ == "__main__":
    # web.confing.debug = False
    app.run()
