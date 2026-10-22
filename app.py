from flask import flask, render_templace

app = flask(__name__)

@app.route('/')
def index():
    return render_templace('index.html')

if __name__ == '__main__':
    app.run()