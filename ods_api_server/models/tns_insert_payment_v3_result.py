# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.all_oftns_insert_payment_v3_result_insert_payment import AllOftnsInsertPaymentV3ResultInsertPayment  # noqa: F401,E501
from ods_api_server import util


class TnsInsertPaymentV3Result(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, insert_payment: AllOftnsInsertPaymentV3ResultInsertPayment=None):  # noqa: E501
        """TnsInsertPaymentV3Result - a model defined in Swagger

        :param insert_payment: The insert_payment of this TnsInsertPaymentV3Result.  # noqa: E501
        :type insert_payment: AllOftnsInsertPaymentV3ResultInsertPayment
        """
        self.swagger_types = {
            'insert_payment': AllOftnsInsertPaymentV3ResultInsertPayment
        }

        self.attribute_map = {
            'insert_payment': 'insertPayment'
        }
        self._insert_payment = insert_payment

    @classmethod
    def from_dict(cls, dikt) -> 'TnsInsertPaymentV3Result':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tns_InsertPaymentV3_Result of this TnsInsertPaymentV3Result.  # noqa: E501
        :rtype: TnsInsertPaymentV3Result
        """
        return util.deserialize_model(dikt, cls)

    @property
    def insert_payment(self) -> AllOftnsInsertPaymentV3ResultInsertPayment:
        """Gets the insert_payment of this TnsInsertPaymentV3Result.


        :return: The insert_payment of this TnsInsertPaymentV3Result.
        :rtype: AllOftnsInsertPaymentV3ResultInsertPayment
        """
        return self._insert_payment

    @insert_payment.setter
    def insert_payment(self, insert_payment: AllOftnsInsertPaymentV3ResultInsertPayment):
        """Sets the insert_payment of this TnsInsertPaymentV3Result.


        :param insert_payment: The insert_payment of this TnsInsertPaymentV3Result.
        :type insert_payment: AllOftnsInsertPaymentV3ResultInsertPayment
        """
        if insert_payment is None:
            raise ValueError("Invalid value for `insert_payment`, must not be `None`")  # noqa: E501

        self._insert_payment = insert_payment
