#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Hello API"""

import flask_restful

class Hello(flask_restful.Resource):
    """Represents a greeting"""

    def get(self, user_name=None):
        """
        Get method, can accept an optional `user_name`
        """
        if user_name:
            return {"greeting": "Hello {0}".format(user_name)}
        return {"greeting": "Hello {0}".format("anon")}
