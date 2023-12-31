# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.insert_payment_v2_result import InsertPaymentV2Result  # noqa: F401,E501
from ods_api_server import util


class InlineResponse2005(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, insert_payment_v2_result: object=None):  # noqa: E501
        """InlineResponse2005 - a model defined in Swagger

        :param insert_payment_v2_result: The insert_payment_v2_result of this InlineResponse2005.  # noqa: E501
        :type insert_payment_v2_result: object
        """
        self.swagger_types = {
            'insert_payment_v2_result': object
        }

        self.attribute_map = {
            'insert_payment_v2_result': 'InsertPaymentV2_Result'
        }
        self._insert_payment_v2_result = insert_payment_v2_result

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2005':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_5 of this InlineResponse2005.  # noqa: E501
        :rtype: InlineResponse2005
        """
        return util.deserialize_model(dikt, cls)

    @property
    def insert_payment_v2_result(self) -> object:
        """Gets the insert_payment_v2_result of this InlineResponse2005.


        :return: The insert_payment_v2_result of this InlineResponse2005.
        :rtype: object
        """
        return self._insert_payment_v2_result

    @insert_payment_v2_result.setter
    def insert_payment_v2_result(self, insert_payment_v2_result: object):
        """Sets the insert_payment_v2_result of this InlineResponse2005.


        :param insert_payment_v2_result: The insert_payment_v2_result of this InlineResponse2005.
        :type insert_payment_v2_result: object
        """
        if insert_payment_v2_result is None:
            raise ValueError("Invalid value for `insert_payment_v2_result`, must not be `None`")  # noqa: E501

        self._insert_payment_v2_result = insert_payment_v2_result
