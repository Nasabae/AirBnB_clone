#!/usr/bin/python3

from models.base_model import BaseModel

"""
Review Module
Defines the Place class with public attributes
'place_id', 'user_id', and 'text'
"""


class Review(BaseModel):
    """
    Review class
    """
    place_id = ""
    user_id = ""
    text = ""
