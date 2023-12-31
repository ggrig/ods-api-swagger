# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.all_oftns_modify_invoice_result_modify_invoice import AllOftnsModifyInvoiceResultModifyInvoice  # noqa: F401,E501
from ods_api_server import util


class TnsModifyInvoiceResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, modify_invoice: AllOftnsModifyInvoiceResultModifyInvoice=None):  # noqa: E501
        """TnsModifyInvoiceResult - a model defined in Swagger

        :param modify_invoice: The modify_invoice of this TnsModifyInvoiceResult.  # noqa: E501
        :type modify_invoice: AllOftnsModifyInvoiceResultModifyInvoice
        """
        self.swagger_types = {
            'modify_invoice': AllOftnsModifyInvoiceResultModifyInvoice
        }

        self.attribute_map = {
            'modify_invoice': 'modifyInvoice'
        }
        self._modify_invoice = modify_invoice

    @classmethod
    def from_dict(cls, dikt) -> 'TnsModifyInvoiceResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tns_ModifyInvoice_Result of this TnsModifyInvoiceResult.  # noqa: E501
        :rtype: TnsModifyInvoiceResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def modify_invoice(self) -> AllOftnsModifyInvoiceResultModifyInvoice:
        """Gets the modify_invoice of this TnsModifyInvoiceResult.


        :return: The modify_invoice of this TnsModifyInvoiceResult.
        :rtype: AllOftnsModifyInvoiceResultModifyInvoice
        """
        return self._modify_invoice

    @modify_invoice.setter
    def modify_invoice(self, modify_invoice: AllOftnsModifyInvoiceResultModifyInvoice):
        """Sets the modify_invoice of this TnsModifyInvoiceResult.


        :param modify_invoice: The modify_invoice of this TnsModifyInvoiceResult.
        :type modify_invoice: AllOftnsModifyInvoiceResultModifyInvoice
        """
        if modify_invoice is None:
            raise ValueError("Invalid value for `modify_invoice`, must not be `None`")  # noqa: E501

        self._modify_invoice = modify_invoice
