# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.all_of_change_invoice_address_result_change_invoice_address_result import AllOfChangeInvoiceAddressResultChangeInvoiceAddressResult  # noqa: F401,E501
from ods_api_server import util


class ChangeInvoiceAddressResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, change_invoice_address_result: AllOfChangeInvoiceAddressResultChangeInvoiceAddressResult=None):  # noqa: E501
        """ChangeInvoiceAddressResult - a model defined in Swagger

        :param change_invoice_address_result: The change_invoice_address_result of this ChangeInvoiceAddressResult.  # noqa: E501
        :type change_invoice_address_result: AllOfChangeInvoiceAddressResultChangeInvoiceAddressResult
        """
        self.swagger_types = {
            'change_invoice_address_result': AllOfChangeInvoiceAddressResultChangeInvoiceAddressResult
        }

        self.attribute_map = {
            'change_invoice_address_result': 'ChangeInvoiceAddress_Result'
        }
        self._change_invoice_address_result = change_invoice_address_result

    @classmethod
    def from_dict(cls, dikt) -> 'ChangeInvoiceAddressResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ChangeInvoiceAddress_Result of this ChangeInvoiceAddressResult.  # noqa: E501
        :rtype: ChangeInvoiceAddressResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def change_invoice_address_result(self) -> AllOfChangeInvoiceAddressResultChangeInvoiceAddressResult:
        """Gets the change_invoice_address_result of this ChangeInvoiceAddressResult.


        :return: The change_invoice_address_result of this ChangeInvoiceAddressResult.
        :rtype: AllOfChangeInvoiceAddressResultChangeInvoiceAddressResult
        """
        return self._change_invoice_address_result

    @change_invoice_address_result.setter
    def change_invoice_address_result(self, change_invoice_address_result: AllOfChangeInvoiceAddressResultChangeInvoiceAddressResult):
        """Sets the change_invoice_address_result of this ChangeInvoiceAddressResult.


        :param change_invoice_address_result: The change_invoice_address_result of this ChangeInvoiceAddressResult.
        :type change_invoice_address_result: AllOfChangeInvoiceAddressResultChangeInvoiceAddressResult
        """
        if change_invoice_address_result is None:
            raise ValueError("Invalid value for `change_invoice_address_result`, must not be `None`")  # noqa: E501

        self._change_invoice_address_result = change_invoice_address_result
