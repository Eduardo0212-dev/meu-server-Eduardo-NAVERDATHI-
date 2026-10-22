from Flask import Flask, render_templace

app = Flask(__name__)

@app.route('/')
def index():
    return render_templace('index.html')

if __name__ == '__main__':
    app.run()