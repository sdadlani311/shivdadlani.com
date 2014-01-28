#!/usr/bin/env python
from werkzeug import script

from application import create_app


def make_shell():
    return dict(app=create_app('settings'))

if __name__ == "__main__":
    script.make_shell(make_shell, use_ipython=True)()
