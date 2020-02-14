from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, world!"


if __name__ == '__main__':
    app.run()
