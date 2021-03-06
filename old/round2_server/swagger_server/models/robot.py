# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.coordinate import Coordinate
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Robot(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, coordinates: Coordinate=None, id: int=None):
        """
        Robot - a model defined in Swagger

        :param coordinates: The coordinates of this Robot.
        :type coordinates: Coordinate
        :param id: The id of this Robot.
        :type id: int
        """
        self.swagger_types = {
            'coordinates': Coordinate,
            'id': int
        }

        self.attribute_map = {
            'coordinates': 'coordinates',
            'id': 'id'
        }

        self._coordinates = coordinates
        self._id = id

    @classmethod
    def from_dict(cls, dikt) -> 'Robot':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Robot of this Robot.
        :rtype: Robot
        """
        return deserialize_model(dikt, cls)

    @property
    def coordinates(self) -> Coordinate:
        """
        Gets the coordinates of this Robot.

        :return: The coordinates of this Robot.
        :rtype: Coordinate
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates: Coordinate):
        """
        Sets the coordinates of this Robot.

        :param coordinates: The coordinates of this Robot.
        :type coordinates: Coordinate
        """

        self._coordinates = coordinates

    @property
    def id(self) -> int:
        """
        Gets the id of this Robot.

        :return: The id of this Robot.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """
        Sets the id of this Robot.

        :param id: The id of this Robot.
        :type id: int
        """

        self._id = id

