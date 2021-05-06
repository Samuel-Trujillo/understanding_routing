from flask import Flask  
app = Flask(__name__)    
@app.route('/')          
def hello_world():
    return 'Hello World!'
@app.route("/dojo")
def dojo():
    return "Dojo!"
@app.route('/say/<ninput>')
def say(ninput):
    return "Hi " + str(ninput) +"!"
@app.route('/repeat/<times>/<text>')
def repeat(times,text):
    return str((text + "  ") * int(times))
if __name__=="__main__":
    app.run(debug=True)    
