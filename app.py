#!/usr/bin/env python
# -*- coding: utf-8 -*-
from application import create_app
app = create_app('settings')

if __name__ == '__main__':
    app.debug = True
    app.run()

