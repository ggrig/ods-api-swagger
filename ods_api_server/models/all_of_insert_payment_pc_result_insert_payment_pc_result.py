# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.tns_insert_payment_pc_result import TnsInsertPaymentPCResult  # noqa: F401,E501
from ods_api_server import util


class AllOfInsertPaymentPCResultInsertPaymentPcResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, insert_payment: object=None):  # noqa: E501
        """AllOfInsertPaymentPCResultInsertPaymentPcResult - a model defined in Swagger

        :param insert_payment: The insert_payment of this AllOfInsertPaymentPCResultInsertPaymentPcResult.  # noqa: E501
        :type insert_payment: object
        """
        self.swagger_types = {
            'insert_payment': object
        }

        self.attribute_map = {
            'insert_payment': 'insertPayment'
        }
        self._insert_payment = insert_payment

    @classmethod
    def from_dict(cls, dikt) -> 'AllOfInsertPaymentPCResultInsertPaymentPcResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AllOfInsertPaymentPC_ResultInsertPaymentPcResult of this AllOfInsertPaymentPCResultInsertPaymentPcResult.  # noqa: E501
        :rtype: AllOfInsertPaymentPCResultInsertPaymentPcResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def insert_payment(self) -> object:
        """Gets the insert_payment of this AllOfInsertPaymentPCResultInsertPaymentPcResult.


        :return: The insert_payment of this AllOfInsertPaymentPCResultInsertPaymentPcResult.
        :rtype: object
        """
        return self._insert_payment

    @insert_payment.setter
    def insert_payment(self, insert_payment: object):
        """Sets the insert_payment of this AllOfInsertPaymentPCResultInsertPaymentPcResult.


        :param insert_payment: The insert_payment of this AllOfInsertPaymentPCResultInsertPaymentPcResult.
        :type insert_payment: object
        """
        if insert_payment is None:
            raise ValueError("Invalid value for `insert_payment`, must not be `None`")  # noqa: E501

        self._insert_payment = insert_payment
