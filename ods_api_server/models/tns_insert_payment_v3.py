# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.all_oftns_insert_payment_v3_insert_payment import AllOftnsInsertPaymentV3InsertPayment  # noqa: F401,E501
from ods_api_server import util


class TnsInsertPaymentV3(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, insert_payment: AllOftnsInsertPaymentV3InsertPayment=None):  # noqa: E501
        """TnsInsertPaymentV3 - a model defined in Swagger

        :param insert_payment: The insert_payment of this TnsInsertPaymentV3.  # noqa: E501
        :type insert_payment: AllOftnsInsertPaymentV3InsertPayment
        """
        self.swagger_types = {
            'insert_payment': AllOftnsInsertPaymentV3InsertPayment
        }

        self.attribute_map = {
            'insert_payment': 'insertPayment'
        }
        self._insert_payment = insert_payment

    @classmethod
    def from_dict(cls, dikt) -> 'TnsInsertPaymentV3':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tns_InsertPaymentV3 of this TnsInsertPaymentV3.  # noqa: E501
        :rtype: TnsInsertPaymentV3
        """
        return util.deserialize_model(dikt, cls)

    @property
    def insert_payment(self) -> AllOftnsInsertPaymentV3InsertPayment:
        """Gets the insert_payment of this TnsInsertPaymentV3.


        :return: The insert_payment of this TnsInsertPaymentV3.
        :rtype: AllOftnsInsertPaymentV3InsertPayment
        """
        return self._insert_payment

    @insert_payment.setter
    def insert_payment(self, insert_payment: AllOftnsInsertPaymentV3InsertPayment):
        """Sets the insert_payment of this TnsInsertPaymentV3.


        :param insert_payment: The insert_payment of this TnsInsertPaymentV3.
        :type insert_payment: AllOftnsInsertPaymentV3InsertPayment
        """
        if insert_payment is None:
            raise ValueError("Invalid value for `insert_payment`, must not be `None`")  # noqa: E501

        self._insert_payment = insert_payment
