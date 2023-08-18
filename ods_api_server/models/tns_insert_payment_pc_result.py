# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.all_oftns_insert_payment_pc_result_insert_payment import AllOftnsInsertPaymentPCResultInsertPayment  # noqa: F401,E501
from ods_api_server import util


class TnsInsertPaymentPCResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, insert_payment: AllOftnsInsertPaymentPCResultInsertPayment=None):  # noqa: E501
        """TnsInsertPaymentPCResult - a model defined in Swagger

        :param insert_payment: The insert_payment of this TnsInsertPaymentPCResult.  # noqa: E501
        :type insert_payment: AllOftnsInsertPaymentPCResultInsertPayment
        """
        self.swagger_types = {
            'insert_payment': AllOftnsInsertPaymentPCResultInsertPayment
        }

        self.attribute_map = {
            'insert_payment': 'insertPayment'
        }
        self._insert_payment = insert_payment

    @classmethod
    def from_dict(cls, dikt) -> 'TnsInsertPaymentPCResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tns_InsertPaymentPC_Result of this TnsInsertPaymentPCResult.  # noqa: E501
        :rtype: TnsInsertPaymentPCResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def insert_payment(self) -> AllOftnsInsertPaymentPCResultInsertPayment:
        """Gets the insert_payment of this TnsInsertPaymentPCResult.


        :return: The insert_payment of this TnsInsertPaymentPCResult.
        :rtype: AllOftnsInsertPaymentPCResultInsertPayment
        """
        return self._insert_payment

    @insert_payment.setter
    def insert_payment(self, insert_payment: AllOftnsInsertPaymentPCResultInsertPayment):
        """Sets the insert_payment of this TnsInsertPaymentPCResult.


        :param insert_payment: The insert_payment of this TnsInsertPaymentPCResult.
        :type insert_payment: AllOftnsInsertPaymentPCResultInsertPayment
        """
        if insert_payment is None:
            raise ValueError("Invalid value for `insert_payment`, must not be `None`")  # noqa: E501

        self._insert_payment = insert_payment
