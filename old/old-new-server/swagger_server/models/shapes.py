# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.polygon import Polygon
from swagger_server.models.rectangle import Rectangle
from swagger_server.models.triangle import Triangle
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Shapes(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, rectangle: Rectangle=None, triangle: Triangle=None, polygon: Polygon=None):
        """
        Shapes - a model defined in Swagger

        :param rectangle: The rectangle of this Shapes.
        :type rectangle: Rectangle
        :param triangle: The triangle of this Shapes.
        :type triangle: Triangle
        :param polygon: The polygon of this Shapes.
        :type polygon: Polygon
        """
        self.swagger_types = {
            'rectangle': Rectangle,
            'triangle': Triangle,
            'polygon': Polygon
        }

        self.attribute_map = {
            'rectangle': 'rectangle',
            'triangle': 'triangle',
            'polygon': 'polygon'
        }

        self._rectangle = rectangle
        self._triangle = triangle
        self._polygon = polygon

    @classmethod
    def from_dict(cls, dikt) -> 'Shapes':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Shapes of this Shapes.
        :rtype: Shapes
        """
        return deserialize_model(dikt, cls)

    @property
    def rectangle(self) -> Rectangle:
        """
        Gets the rectangle of this Shapes.

        :return: The rectangle of this Shapes.
        :rtype: Rectangle
        """
        return self._rectangle

    @rectangle.setter
    def rectangle(self, rectangle: Rectangle):
        """
        Sets the rectangle of this Shapes.

        :param rectangle: The rectangle of this Shapes.
        :type rectangle: Rectangle
        """

        self._rectangle = rectangle

    @property
    def triangle(self) -> Triangle:
        """
        Gets the triangle of this Shapes.

        :return: The triangle of this Shapes.
        :rtype: Triangle
        """
        return self._triangle

    @triangle.setter
    def triangle(self, triangle: Triangle):
        """
        Sets the triangle of this Shapes.

        :param triangle: The triangle of this Shapes.
        :type triangle: Triangle
        """

        self._triangle = triangle

    @property
    def polygon(self) -> Polygon:
        """
        Gets the polygon of this Shapes.

        :return: The polygon of this Shapes.
        :rtype: Polygon
        """
        return self._polygon

    @polygon.setter
    def polygon(self, polygon: Polygon):
        """
        Sets the polygon of this Shapes.

        :param polygon: The polygon of this Shapes.
        :type polygon: Polygon
        """

        self._polygon = polygon

