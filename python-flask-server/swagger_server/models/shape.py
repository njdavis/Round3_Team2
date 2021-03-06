# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Shape(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, shape_type: str=None):
        """
        Shape - a model defined in Swagger

        :param shape_type: The shape_type of this Shape.
        :type shape_type: str
        """
        self.swagger_types = {
            'shape_type': str
        }

        self.attribute_map = {
            'shape_type': 'shapeType'
        }

        self._shape_type = shape_type

    @classmethod
    def from_dict(cls, dikt) -> 'Shape':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Shape of this Shape.
        :rtype: Shape
        """
        return deserialize_model(dikt, cls)

    @property
    def shape_type(self) -> str:
        """
        Gets the shape_type of this Shape.

        :return: The shape_type of this Shape.
        :rtype: str
        """
        return self._shape_type

    @shape_type.setter
    def shape_type(self, shape_type: str):
        """
        Sets the shape_type of this Shape.

        :param shape_type: The shape_type of this Shape.
        :type shape_type: str
        """
        if shape_type is None:
            raise ValueError("Invalid value for `shape_type`, must not be `None`")

        self._shape_type = shape_type

