from flask import Flask

app=Flask(__name__)
    
@app.route('/')
def index():   #Decorador ligada a la ruta inicial
    return "Soy el amo en flask - Suscribete - Dale un like pelotudo"


if __name__ =='__main__':   
    app.run(debug=True, port=5000)
