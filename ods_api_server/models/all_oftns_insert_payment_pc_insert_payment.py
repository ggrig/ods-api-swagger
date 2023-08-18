# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.q30_payment_line import Q30PaymentLine  # noqa: F401,E501
from ods_api_server.models.q30_payment_lines import Q30PaymentLines  # noqa: F401,E501
from ods_api_server import util


class AllOftnsInsertPaymentPCInsertPayment(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, payment_line: List[Q30PaymentLine]=None):  # noqa: E501
        """AllOftnsInsertPaymentPCInsertPayment - a model defined in Swagger

        :param payment_line: The payment_line of this AllOftnsInsertPaymentPCInsertPayment.  # noqa: E501
        :type payment_line: List[Q30PaymentLine]
        """
        self.swagger_types = {
            'payment_line': List[Q30PaymentLine]
        }

        self.attribute_map = {
            'payment_line': 'PaymentLine'
        }
        self._payment_line = payment_line

    @classmethod
    def from_dict(cls, dikt) -> 'AllOftnsInsertPaymentPCInsertPayment':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AllOftns_InsertPaymentPCInsertPayment of this AllOftnsInsertPaymentPCInsertPayment.  # noqa: E501
        :rtype: AllOftnsInsertPaymentPCInsertPayment
        """
        return util.deserialize_model(dikt, cls)

    @property
    def payment_line(self) -> List[Q30PaymentLine]:
        """Gets the payment_line of this AllOftnsInsertPaymentPCInsertPayment.


        :return: The payment_line of this AllOftnsInsertPaymentPCInsertPayment.
        :rtype: List[Q30PaymentLine]
        """
        return self._payment_line

    @payment_line.setter
    def payment_line(self, payment_line: List[Q30PaymentLine]):
        """Sets the payment_line of this AllOftnsInsertPaymentPCInsertPayment.


        :param payment_line: The payment_line of this AllOftnsInsertPaymentPCInsertPayment.
        :type payment_line: List[Q30PaymentLine]
        """
        if payment_line is None:
            raise ValueError("Invalid value for `payment_line`, must not be `None`")  # noqa: E501

        self._payment_line = payment_line