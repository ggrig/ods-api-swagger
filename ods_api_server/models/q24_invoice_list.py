# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.q24_invoice import Q24Invoice  # noqa: F401,E501
from ods_api_server import util


class Q24InvoiceList(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, invoice: List[Q24Invoice]=None):  # noqa: E501
        """Q24InvoiceList - a model defined in Swagger

        :param invoice: The invoice of this Q24InvoiceList.  # noqa: E501
        :type invoice: List[Q24Invoice]
        """
        self.swagger_types = {
            'invoice': List[Q24Invoice]
        }

        self.attribute_map = {
            'invoice': 'Invoice'
        }
        self._invoice = invoice

    @classmethod
    def from_dict(cls, dikt) -> 'Q24InvoiceList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The q24_InvoiceList of this Q24InvoiceList.  # noqa: E501
        :rtype: Q24InvoiceList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def invoice(self) -> List[Q24Invoice]:
        """Gets the invoice of this Q24InvoiceList.


        :return: The invoice of this Q24InvoiceList.
        :rtype: List[Q24Invoice]
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice: List[Q24Invoice]):
        """Sets the invoice of this Q24InvoiceList.


        :param invoice: The invoice of this Q24InvoiceList.
        :type invoice: List[Q24Invoice]
        """
        if invoice is None:
            raise ValueError("Invalid value for `invoice`, must not be `None`")  # noqa: E501

        self._invoice = invoice
