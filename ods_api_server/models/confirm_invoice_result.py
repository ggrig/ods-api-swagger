# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.all_of_confirm_invoice_result_confirm_invoice_result import AllOfConfirmInvoiceResultConfirmInvoiceResult  # noqa: F401,E501
from ods_api_server import util


class ConfirmInvoiceResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, confirm_invoice_result: AllOfConfirmInvoiceResultConfirmInvoiceResult=None):  # noqa: E501
        """ConfirmInvoiceResult - a model defined in Swagger

        :param confirm_invoice_result: The confirm_invoice_result of this ConfirmInvoiceResult.  # noqa: E501
        :type confirm_invoice_result: AllOfConfirmInvoiceResultConfirmInvoiceResult
        """
        self.swagger_types = {
            'confirm_invoice_result': AllOfConfirmInvoiceResultConfirmInvoiceResult
        }

        self.attribute_map = {
            'confirm_invoice_result': 'ConfirmInvoice_Result'
        }
        self._confirm_invoice_result = confirm_invoice_result

    @classmethod
    def from_dict(cls, dikt) -> 'ConfirmInvoiceResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ConfirmInvoice_Result of this ConfirmInvoiceResult.  # noqa: E501
        :rtype: ConfirmInvoiceResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def confirm_invoice_result(self) -> AllOfConfirmInvoiceResultConfirmInvoiceResult:
        """Gets the confirm_invoice_result of this ConfirmInvoiceResult.


        :return: The confirm_invoice_result of this ConfirmInvoiceResult.
        :rtype: AllOfConfirmInvoiceResultConfirmInvoiceResult
        """
        return self._confirm_invoice_result

    @confirm_invoice_result.setter
    def confirm_invoice_result(self, confirm_invoice_result: AllOfConfirmInvoiceResultConfirmInvoiceResult):
        """Sets the confirm_invoice_result of this ConfirmInvoiceResult.


        :param confirm_invoice_result: The confirm_invoice_result of this ConfirmInvoiceResult.
        :type confirm_invoice_result: AllOfConfirmInvoiceResultConfirmInvoiceResult
        """
        if confirm_invoice_result is None:
            raise ValueError("Invalid value for `confirm_invoice_result`, must not be `None`")  # noqa: E501

        self._confirm_invoice_result = confirm_invoice_result
