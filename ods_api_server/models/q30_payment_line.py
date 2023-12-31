# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.all_ofq30_payment_line_reservation import AllOfq30PaymentLineReservation  # noqa: F401,E501
from ods_api_server import util


class Q30PaymentLine(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, posting_date: str=None, payment_method_code: str=None, ext_document_no: str=None, reservation: AllOfq30PaymentLineReservation=None, currency_code: str=None):  # noqa: E501
        """Q30PaymentLine - a model defined in Swagger

        :param posting_date: The posting_date of this Q30PaymentLine.  # noqa: E501
        :type posting_date: str
        :param payment_method_code: The payment_method_code of this Q30PaymentLine.  # noqa: E501
        :type payment_method_code: str
        :param ext_document_no: The ext_document_no of this Q30PaymentLine.  # noqa: E501
        :type ext_document_no: str
        :param reservation: The reservation of this Q30PaymentLine.  # noqa: E501
        :type reservation: AllOfq30PaymentLineReservation
        :param currency_code: The currency_code of this Q30PaymentLine.  # noqa: E501
        :type currency_code: str
        """
        self.swagger_types = {
            'posting_date': str,
            'payment_method_code': str,
            'ext_document_no': str,
            'reservation': AllOfq30PaymentLineReservation,
            'currency_code': str
        }

        self.attribute_map = {
            'posting_date': 'PostingDate',
            'payment_method_code': 'PaymentMethodCode',
            'ext_document_no': 'ExtDocumentNo',
            'reservation': 'Reservation',
            'currency_code': 'CurrencyCode'
        }
        self._posting_date = posting_date
        self._payment_method_code = payment_method_code
        self._ext_document_no = ext_document_no
        self._reservation = reservation
        self._currency_code = currency_code

    @classmethod
    def from_dict(cls, dikt) -> 'Q30PaymentLine':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The q30_PaymentLine of this Q30PaymentLine.  # noqa: E501
        :rtype: Q30PaymentLine
        """
        return util.deserialize_model(dikt, cls)

    @property
    def posting_date(self) -> str:
        """Gets the posting_date of this Q30PaymentLine.


        :return: The posting_date of this Q30PaymentLine.
        :rtype: str
        """
        return self._posting_date

    @posting_date.setter
    def posting_date(self, posting_date: str):
        """Sets the posting_date of this Q30PaymentLine.


        :param posting_date: The posting_date of this Q30PaymentLine.
        :type posting_date: str
        """
        if posting_date is None:
            raise ValueError("Invalid value for `posting_date`, must not be `None`")  # noqa: E501

        self._posting_date = posting_date

    @property
    def payment_method_code(self) -> str:
        """Gets the payment_method_code of this Q30PaymentLine.


        :return: The payment_method_code of this Q30PaymentLine.
        :rtype: str
        """
        return self._payment_method_code

    @payment_method_code.setter
    def payment_method_code(self, payment_method_code: str):
        """Sets the payment_method_code of this Q30PaymentLine.


        :param payment_method_code: The payment_method_code of this Q30PaymentLine.
        :type payment_method_code: str
        """
        if payment_method_code is None:
            raise ValueError("Invalid value for `payment_method_code`, must not be `None`")  # noqa: E501

        self._payment_method_code = payment_method_code

    @property
    def ext_document_no(self) -> str:
        """Gets the ext_document_no of this Q30PaymentLine.


        :return: The ext_document_no of this Q30PaymentLine.
        :rtype: str
        """
        return self._ext_document_no

    @ext_document_no.setter
    def ext_document_no(self, ext_document_no: str):
        """Sets the ext_document_no of this Q30PaymentLine.


        :param ext_document_no: The ext_document_no of this Q30PaymentLine.
        :type ext_document_no: str
        """
        if ext_document_no is None:
            raise ValueError("Invalid value for `ext_document_no`, must not be `None`")  # noqa: E501

        self._ext_document_no = ext_document_no

    @property
    def reservation(self) -> AllOfq30PaymentLineReservation:
        """Gets the reservation of this Q30PaymentLine.


        :return: The reservation of this Q30PaymentLine.
        :rtype: AllOfq30PaymentLineReservation
        """
        return self._reservation

    @reservation.setter
    def reservation(self, reservation: AllOfq30PaymentLineReservation):
        """Sets the reservation of this Q30PaymentLine.


        :param reservation: The reservation of this Q30PaymentLine.
        :type reservation: AllOfq30PaymentLineReservation
        """
        if reservation is None:
            raise ValueError("Invalid value for `reservation`, must not be `None`")  # noqa: E501

        self._reservation = reservation

    @property
    def currency_code(self) -> str:
        """Gets the currency_code of this Q30PaymentLine.


        :return: The currency_code of this Q30PaymentLine.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code: str):
        """Sets the currency_code of this Q30PaymentLine.


        :param currency_code: The currency_code of this Q30PaymentLine.
        :type currency_code: str
        """
        if currency_code is None:
            raise ValueError("Invalid value for `currency_code`, must not be `None`")  # noqa: E501

        self._currency_code = currency_code
