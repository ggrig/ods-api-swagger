# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.q18_invoice import Q18Invoice  # noqa: F401,E501
from ods_api_server.models.q18_invoice_list import Q18InvoiceList  # noqa: F401,E501
from ods_api_server import util


class AllOftnsModifyInvoiceV3ModifyInvoice(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, invoice: List[Q18Invoice]=None):  # noqa: E501
        """AllOftnsModifyInvoiceV3ModifyInvoice - a model defined in Swagger

        :param invoice: The invoice of this AllOftnsModifyInvoiceV3ModifyInvoice.  # noqa: E501
        :type invoice: List[Q18Invoice]
        """
        self.swagger_types = {
            'invoice': List[Q18Invoice]
        }

        self.attribute_map = {
            'invoice': 'Invoice'
        }
        self._invoice = invoice

    @classmethod
    def from_dict(cls, dikt) -> 'AllOftnsModifyInvoiceV3ModifyInvoice':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AllOftns_ModifyInvoiceV3ModifyInvoice of this AllOftnsModifyInvoiceV3ModifyInvoice.  # noqa: E501
        :rtype: AllOftnsModifyInvoiceV3ModifyInvoice
        """
        return util.deserialize_model(dikt, cls)

    @property
    def invoice(self) -> List[Q18Invoice]:
        """Gets the invoice of this AllOftnsModifyInvoiceV3ModifyInvoice.


        :return: The invoice of this AllOftnsModifyInvoiceV3ModifyInvoice.
        :rtype: List[Q18Invoice]
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice: List[Q18Invoice]):
        """Sets the invoice of this AllOftnsModifyInvoiceV3ModifyInvoice.


        :param invoice: The invoice of this AllOftnsModifyInvoiceV3ModifyInvoice.
        :type invoice: List[Q18Invoice]
        """
        if invoice is None:
            raise ValueError("Invalid value for `invoice`, must not be `None`")  # noqa: E501

        self._invoice = invoice
