

import os
from flask import Flask, render_template

from singltone import Config_Provider

# CONFIG_PROVIDER = Singltone()
# MODERATOR = Moderator()

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title_name='Home', config=Config_Provider.get_instance())

@app.route('/learn_italian')
def learn_italian():
    return render_template('learn_word.html', title_name='Learn Italian', config=Config_Provider.get_instance())

if __name__ == '__main__':
    # set_navbar_links()
    # chrome://net-internals/#sockets
    app.config['SECRET_KEY'] = Config_Provider.SECRET_KEY
    app.config.update(
        dict(DATABASE=os.path.join(app.root_path, Config_Provider.DATABASE_PATH))
    )
    app.run(port=8000, debug=Config_Provider.DEBUG)