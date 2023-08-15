# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.all_oftns_confirm_invoice_result_confirm_invoice import AllOftnsConfirmInvoiceResultConfirmInvoice  # noqa: F401,E501
from ods_api_server import util


class TnsConfirmInvoiceResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, confirm_invoice: AllOftnsConfirmInvoiceResultConfirmInvoice=None):  # noqa: E501
        """TnsConfirmInvoiceResult - a model defined in Swagger

        :param confirm_invoice: The confirm_invoice of this TnsConfirmInvoiceResult.  # noqa: E501
        :type confirm_invoice: AllOftnsConfirmInvoiceResultConfirmInvoice
        """
        self.swagger_types = {
            'confirm_invoice': AllOftnsConfirmInvoiceResultConfirmInvoice
        }

        self.attribute_map = {
            'confirm_invoice': 'confirmInvoice'
        }
        self._confirm_invoice = confirm_invoice

    @classmethod
    def from_dict(cls, dikt) -> 'TnsConfirmInvoiceResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tns_ConfirmInvoice_Result of this TnsConfirmInvoiceResult.  # noqa: E501
        :rtype: TnsConfirmInvoiceResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def confirm_invoice(self) -> AllOftnsConfirmInvoiceResultConfirmInvoice:
        """Gets the confirm_invoice of this TnsConfirmInvoiceResult.


        :return: The confirm_invoice of this TnsConfirmInvoiceResult.
        :rtype: AllOftnsConfirmInvoiceResultConfirmInvoice
        """
        return self._confirm_invoice

    @confirm_invoice.setter
    def confirm_invoice(self, confirm_invoice: AllOftnsConfirmInvoiceResultConfirmInvoice):
        """Sets the confirm_invoice of this TnsConfirmInvoiceResult.


        :param confirm_invoice: The confirm_invoice of this TnsConfirmInvoiceResult.
        :type confirm_invoice: AllOftnsConfirmInvoiceResultConfirmInvoice
        """
        if confirm_invoice is None:
            raise ValueError("Invalid value for `confirm_invoice`, must not be `None`")  # noqa: E501

        self._confirm_invoice = confirm_invoice
