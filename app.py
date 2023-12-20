from flask import Flask
app= Flask(__name__)

@aap.rout('/')
def hello_world():
    return 'Helo Docker'