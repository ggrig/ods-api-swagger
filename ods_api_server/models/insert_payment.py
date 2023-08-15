# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.all_of_insert_payment_insert_payment import AllOfInsertPaymentInsertPayment  # noqa: F401,E501
from ods_api_server import util


class InsertPayment(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, insert_payment: AllOfInsertPaymentInsertPayment=None):  # noqa: E501
        """InsertPayment - a model defined in Swagger

        :param insert_payment: The insert_payment of this InsertPayment.  # noqa: E501
        :type insert_payment: AllOfInsertPaymentInsertPayment
        """
        self.swagger_types = {
            'insert_payment': AllOfInsertPaymentInsertPayment
        }

        self.attribute_map = {
            'insert_payment': 'InsertPayment'
        }
        self._insert_payment = insert_payment

    @classmethod
    def from_dict(cls, dikt) -> 'InsertPayment':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InsertPayment of this InsertPayment.  # noqa: E501
        :rtype: InsertPayment
        """
        return util.deserialize_model(dikt, cls)

    @property
    def insert_payment(self) -> AllOfInsertPaymentInsertPayment:
        """Gets the insert_payment of this InsertPayment.


        :return: The insert_payment of this InsertPayment.
        :rtype: AllOfInsertPaymentInsertPayment
        """
        return self._insert_payment

    @insert_payment.setter
    def insert_payment(self, insert_payment: AllOfInsertPaymentInsertPayment):
        """Sets the insert_payment of this InsertPayment.


        :param insert_payment: The insert_payment of this InsertPayment.
        :type insert_payment: AllOfInsertPaymentInsertPayment
        """
        if insert_payment is None:
            raise ValueError("Invalid value for `insert_payment`, must not be `None`")  # noqa: E501

        self._insert_payment = insert_payment
