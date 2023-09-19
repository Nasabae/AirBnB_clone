#!/usr/bin/python3
# from uuid import uuid4
# from datetime import datetime
# import models

from models.base_model import BaseModel

"""
User Module
Defines a user class with attributes which includes email,
password, first_name, and last_name
"""


class User(BaseModel):
    """
    Class user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
