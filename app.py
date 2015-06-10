#!/usr/bin/env python

import os
import time
from flask import Flask, render_template
from flask.ext.versioned import Versioned, Driver

class Config(object):
    DEBUG = True
    STATIC_VERSION = str(int(os.path.getmtime(__file__)))


class StaticVersionDriver(Driver):

    def __init__(self, app):
        self.app = app

    def version(self, filename):
        return "%s?v=%s" %(filename, app.config["STATIC_VERSION"])


app = Flask(__name__)
app.config.from_object(Config)
versioned = Versioned(app, driver_cls=StaticVersionDriver)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
