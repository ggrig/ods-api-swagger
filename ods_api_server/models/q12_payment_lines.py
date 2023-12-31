# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.q12_payment_line import Q12PaymentLine  # noqa: F401,E501
from ods_api_server import util


class Q12PaymentLines(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, payment_line: List[Q12PaymentLine]=None):  # noqa: E501
        """Q12PaymentLines - a model defined in Swagger

        :param payment_line: The payment_line of this Q12PaymentLines.  # noqa: E501
        :type payment_line: List[Q12PaymentLine]
        """
        self.swagger_types = {
            'payment_line': List[Q12PaymentLine]
        }

        self.attribute_map = {
            'payment_line': 'PaymentLine'
        }
        self._payment_line = payment_line

    @classmethod
    def from_dict(cls, dikt) -> 'Q12PaymentLines':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The q12_PaymentLines of this Q12PaymentLines.  # noqa: E501
        :rtype: Q12PaymentLines
        """
        return util.deserialize_model(dikt, cls)

    @property
    def payment_line(self) -> List[Q12PaymentLine]:
        """Gets the payment_line of this Q12PaymentLines.


        :return: The payment_line of this Q12PaymentLines.
        :rtype: List[Q12PaymentLine]
        """
        return self._payment_line

    @payment_line.setter
    def payment_line(self, payment_line: List[Q12PaymentLine]):
        """Sets the payment_line of this Q12PaymentLines.


        :param payment_line: The payment_line of this Q12PaymentLines.
        :type payment_line: List[Q12PaymentLine]
        """
        if payment_line is None:
            raise ValueError("Invalid value for `payment_line`, must not be `None`")  # noqa: E501

        self._payment_line = payment_line
