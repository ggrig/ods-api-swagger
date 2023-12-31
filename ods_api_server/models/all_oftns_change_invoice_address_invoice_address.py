# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.q2_invoice import Q2Invoice  # noqa: F401,E501
from ods_api_server.models.q2_invoices import Q2Invoices  # noqa: F401,E501
from ods_api_server import util


class AllOftnsChangeInvoiceAddressInvoiceAddress(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, invoice: List[Q2Invoice]=None):  # noqa: E501
        """AllOftnsChangeInvoiceAddressInvoiceAddress - a model defined in Swagger

        :param invoice: The invoice of this AllOftnsChangeInvoiceAddressInvoiceAddress.  # noqa: E501
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
    def from_dict(cls, dikt) -> 'AllOftnsChangeInvoiceAddressInvoiceAddress':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AllOftns_ChangeInvoiceAddressInvoiceAddress of this AllOftnsChangeInvoiceAddressInvoiceAddress.  # noqa: E501
        :rtype: AllOftnsChangeInvoiceAddressInvoiceAddress
        """
        return util.deserialize_model(dikt, cls)

    @property
    def invoice(self) -> List[Q2Invoice]:
        """Gets the invoice of this AllOftnsChangeInvoiceAddressInvoiceAddress.


        :return: The invoice of this AllOftnsChangeInvoiceAddressInvoiceAddress.
        :rtype: List[Q2Invoice]
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice: List[Q2Invoice]):
        """Sets the invoice of this AllOftnsChangeInvoiceAddressInvoiceAddress.


        :param invoice: The invoice of this AllOftnsChangeInvoiceAddressInvoiceAddress.
        :type invoice: List[Q2Invoice]
        """
        if invoice is None:
            raise ValueError("Invalid value for `invoice`, must not be `None`")  # noqa: E501

        self._invoice = invoice
