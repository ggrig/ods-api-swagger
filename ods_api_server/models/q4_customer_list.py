# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.q4_customer import Q4Customer  # noqa: F401,E501
from ods_api_server import util


class Q4CustomerList(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, customer: List[Q4Customer]=None):  # noqa: E501
        """Q4CustomerList - a model defined in Swagger

        :param customer: The customer of this Q4CustomerList.  # noqa: E501
        :type customer: List[Q4Customer]
        """
        self.swagger_types = {
            'customer': List[Q4Customer]
        }

        self.attribute_map = {
            'customer': 'Customer'
        }
        self._customer = customer

    @classmethod
    def from_dict(cls, dikt) -> 'Q4CustomerList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The q4_CustomerList of this Q4CustomerList.  # noqa: E501
        :rtype: Q4CustomerList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def customer(self) -> List[Q4Customer]:
        """Gets the customer of this Q4CustomerList.


        :return: The customer of this Q4CustomerList.
        :rtype: List[Q4Customer]
        """
        return self._customer

    @customer.setter
    def customer(self, customer: List[Q4Customer]):
        """Sets the customer of this Q4CustomerList.


        :param customer: The customer of this Q4CustomerList.
        :type customer: List[Q4Customer]
        """
        if customer is None:
            raise ValueError("Invalid value for `customer`, must not be `None`")  # noqa: E501

        self._customer = customer
