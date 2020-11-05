
from flask import Flask
from flask import request

app= Flask (__name__)  #mi objeto 

@app.route('/') #grap o decorador 
def index(): #funcion
    return 'Hola Mundo'

@app.route('/method1')
def method1():
    param =request.args.get('param1', 'without data')
    return 'the param is: ' + str (param)

if __name__=='__main__':
    app.run(debug=True , port=9090)