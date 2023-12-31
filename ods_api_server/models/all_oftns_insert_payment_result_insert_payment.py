# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.q8_payment_line import Q8PaymentLine  # noqa: F401,E501
from ods_api_server.models.q8_payment_lines import Q8PaymentLines  # noqa: F401,E501
from ods_api_server import util


class AllOftnsInsertPaymentResultInsertPayment(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, payment_line: List[Q8PaymentLine]=None):  # noqa: E501
        """AllOftnsInsertPaymentResultInsertPayment - a model defined in Swagger

        :param payment_line: The payment_line of this AllOftnsInsertPaymentResultInsertPayment.  # noqa: E501
        :type payment_line: List[Q8PaymentLine]
        """
        self.swagger_types = {
            'payment_line': List[Q8PaymentLine]
        }

        self.attribute_map = {
            'payment_line': 'PaymentLine'
        }
        self._payment_line = payment_line

    @classmethod
    def from_dict(cls, dikt) -> 'AllOftnsInsertPaymentResultInsertPayment':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AllOftns_InsertPayment_ResultInsertPayment of this AllOftnsInsertPaymentResultInsertPayment.  # noqa: E501
        :rtype: AllOftnsInsertPaymentResultInsertPayment
        """
        return util.deserialize_model(dikt, cls)

    @property
    def payment_line(self) -> List[Q8PaymentLine]:
        """Gets the payment_line of this AllOftnsInsertPaymentResultInsertPayment.


        :return: The payment_line of this AllOftnsInsertPaymentResultInsertPayment.
        :rtype: List[Q8PaymentLine]
        """
        return self._payment_line

    @payment_line.setter
    def payment_line(self, payment_line: List[Q8PaymentLine]):
        """Sets the payment_line of this AllOftnsInsertPaymentResultInsertPayment.


        :param payment_line: The payment_line of this AllOftnsInsertPaymentResultInsertPayment.
        :type payment_line: List[Q8PaymentLine]
        """
        if payment_line is None:
            raise ValueError("Invalid value for `payment_line`, must not be `None`")  # noqa: E501

        self._payment_line = payment_line
