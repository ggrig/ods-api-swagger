# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.q2_invoice import Q2Invoice  # noqa: F401,E501
from ods_api_server.models.q2_invoices import Q2Invoices  # noqa: F401,E501
from ods_api_server import util


class AllOftnsChangeInvoiceAddressResultInvoiceAddress(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, invoice: List[Q2Invoice]=None):  # noqa: E501
        """AllOftnsChangeInvoiceAddressResultInvoiceAddress - a model defined in Swagger

        :param invoice: The invoice of this AllOftnsChangeInvoiceAddressResultInvoiceAddress.  # noqa: E501
        :type invoice: List[Q2Invoice]
        """
        self.swagger_types = {
            'invoice': List[Q2Invoice]
        }

        self.attribute_map = {
            'invoice': 'Invoice'
        }
        self._invoice = invoice

    @classmethod
    def from_dict(cls, dikt) -> 'AllOftnsChangeInvoiceAddressResultInvoiceAddress':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AllOftns_ChangeInvoiceAddress_ResultInvoiceAddress of this AllOftnsChangeInvoiceAddressResultInvoiceAddress.  # noqa: E501
        :rtype: AllOftnsChangeInvoiceAddressResultInvoiceAddress
        """
        return util.deserialize_model(dikt, cls)

    @property
    def invoice(self) -> List[Q2Invoice]:
        """Gets the invoice of this AllOftnsChangeInvoiceAddressResultInvoiceAddress.


        :return: The invoice of this AllOftnsChangeInvoiceAddressResultInvoiceAddress.
        :rtype: List[Q2Invoice]
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice: List[Q2Invoice]):
        """Sets the invoice of this AllOftnsChangeInvoiceAddressResultInvoiceAddress.


        :param invoice: The invoice of this AllOftnsChangeInvoiceAddressResultInvoiceAddress.
        :type invoice: List[Q2Invoice]
        """
        if invoice is None:
            raise ValueError("Invalid value for `invoice`, must not be `None`")  # noqa: E501

        self._invoice = invoice
