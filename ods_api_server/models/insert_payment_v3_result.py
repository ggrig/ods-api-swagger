# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.all_of_insert_payment_v3_result_insert_payment_v3_result import AllOfInsertPaymentV3ResultInsertPaymentV3Result  # noqa: F401,E501
from ods_api_server import util


class InsertPaymentV3Result(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, insert_payment_v3_result: AllOfInsertPaymentV3ResultInsertPaymentV3Result=None):  # noqa: E501
        """InsertPaymentV3Result - a model defined in Swagger

        :param insert_payment_v3_result: The insert_payment_v3_result of this InsertPaymentV3Result.  # noqa: E501
        :type insert_payment_v3_result: AllOfInsertPaymentV3ResultInsertPaymentV3Result
        """
        self.swagger_types = {
            'insert_payment_v3_result': AllOfInsertPaymentV3ResultInsertPaymentV3Result
        }

        self.attribute_map = {
            'insert_payment_v3_result': 'InsertPaymentV3_Result'
        }
        self._insert_payment_v3_result = insert_payment_v3_result

    @classmethod
    def from_dict(cls, dikt) -> 'InsertPaymentV3Result':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InsertPaymentV3_Result of this InsertPaymentV3Result.  # noqa: E501
        :rtype: InsertPaymentV3Result
        """
        return util.deserialize_model(dikt, cls)

    @property
    def insert_payment_v3_result(self) -> AllOfInsertPaymentV3ResultInsertPaymentV3Result:
        """Gets the insert_payment_v3_result of this InsertPaymentV3Result.


        :return: The insert_payment_v3_result of this InsertPaymentV3Result.
        :rtype: AllOfInsertPaymentV3ResultInsertPaymentV3Result
        """
        return self._insert_payment_v3_result

    @insert_payment_v3_result.setter
    def insert_payment_v3_result(self, insert_payment_v3_result: AllOfInsertPaymentV3ResultInsertPaymentV3Result):
        """Sets the insert_payment_v3_result of this InsertPaymentV3Result.


        :param insert_payment_v3_result: The insert_payment_v3_result of this InsertPaymentV3Result.
        :type insert_payment_v3_result: AllOfInsertPaymentV3ResultInsertPaymentV3Result
        """
        if insert_payment_v3_result is None:
            raise ValueError("Invalid value for `insert_payment_v3_result`, must not be `None`")  # noqa: E501

        self._insert_payment_v3_result = insert_payment_v3_result
