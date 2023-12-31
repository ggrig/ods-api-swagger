# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.insert_payment_pc_result import InsertPaymentPCResult  # noqa: F401,E501
from ods_api_server import util


class InlineResponse20014(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, insert_payment_pc_result: object=None):  # noqa: E501
        """InlineResponse20014 - a model defined in Swagger

        :param insert_payment_pc_result: The insert_payment_pc_result of this InlineResponse20014.  # noqa: E501
        :type insert_payment_pc_result: object
        """
        self.swagger_types = {
            'insert_payment_pc_result': object
        }

        self.attribute_map = {
            'insert_payment_pc_result': 'InsertPaymentPC_Result'
        }
        self._insert_payment_pc_result = insert_payment_pc_result

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse20014':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_14 of this InlineResponse20014.  # noqa: E501
        :rtype: InlineResponse20014
        """
        return util.deserialize_model(dikt, cls)

    @property
    def insert_payment_pc_result(self) -> object:
        """Gets the insert_payment_pc_result of this InlineResponse20014.


        :return: The insert_payment_pc_result of this InlineResponse20014.
        :rtype: object
        """
        return self._insert_payment_pc_result

    @insert_payment_pc_result.setter
    def insert_payment_pc_result(self, insert_payment_pc_result: object):
        """Sets the insert_payment_pc_result of this InlineResponse20014.


        :param insert_payment_pc_result: The insert_payment_pc_result of this InlineResponse20014.
        :type insert_payment_pc_result: object
        """
        if insert_payment_pc_result is None:
            raise ValueError("Invalid value for `insert_payment_pc_result`, must not be `None`")  # noqa: E501

        self._insert_payment_pc_result = insert_payment_pc_result
