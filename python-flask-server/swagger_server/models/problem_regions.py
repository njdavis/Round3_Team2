# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.problem_regions_unsearched import ProblemRegionsUnsearched
from swagger_server.models.searched_region_lidar import SearchedRegionLIDAR
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class ProblemRegions(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, searched: List[SearchedRegionLIDAR]=None, unsearched: ProblemRegionsUnsearched=None):
        """
        ProblemRegions - a model defined in Swagger

        :param searched: The searched of this ProblemRegions.
        :type searched: List[SearchedRegionLIDAR]
        :param unsearched: The unsearched of this ProblemRegions.
        :type unsearched: ProblemRegionsUnsearched
        """
        self.swagger_types = {
            'searched': List[SearchedRegionLIDAR],
            'unsearched': ProblemRegionsUnsearched
        }

        self.attribute_map = {
            'searched': 'searched',
            'unsearched': 'unsearched'
        }

        self._searched = searched
        self._unsearched = unsearched

    @classmethod
    def from_dict(cls, dikt) -> 'ProblemRegions':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Problem_regions of this ProblemRegions.
        :rtype: ProblemRegions
        """
        return deserialize_model(dikt, cls)

    @property
    def searched(self) -> List[SearchedRegionLIDAR]:
        """
        Gets the searched of this ProblemRegions.

        :return: The searched of this ProblemRegions.
        :rtype: List[SearchedRegionLIDAR]
        """
        return self._searched

    @searched.setter
    def searched(self, searched: List[SearchedRegionLIDAR]):
        """
        Sets the searched of this ProblemRegions.

        :param searched: The searched of this ProblemRegions.
        :type searched: List[SearchedRegionLIDAR]
        """

        self._searched = searched

    @property
    def unsearched(self) -> ProblemRegionsUnsearched:
        """
        Gets the unsearched of this ProblemRegions.

        :return: The unsearched of this ProblemRegions.
        :rtype: ProblemRegionsUnsearched
        """
        return self._unsearched

    @unsearched.setter
    def unsearched(self, unsearched: ProblemRegionsUnsearched):
        """
        Sets the unsearched of this ProblemRegions.

        :param unsearched: The unsearched of this ProblemRegions.
        :type unsearched: ProblemRegionsUnsearched
        """

        self._unsearched = unsearched

