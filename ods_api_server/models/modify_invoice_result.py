# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.all_of_modify_invoice_result_modify_invoice_result import AllOfModifyInvoiceResultModifyInvoiceResult  # noqa: F401,E501
from ods_api_server import util


class ModifyInvoiceResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, modify_invoice_result: AllOfModifyInvoiceResultModifyInvoiceResult=None):  # noqa: E501
        """ModifyInvoiceResult - a model defined in Swagger

        :param modify_invoice_result: The modify_invoice_result of this ModifyInvoiceResult.  # noqa: E501
        :type modify_invoice_result: AllOfModifyInvoiceResultModifyInvoiceResult
        """
        self.swagger_types = {
            'modify_invoice_result': AllOfModifyInvoiceResultModifyInvoiceResult
        }

        self.attribute_map = {
            'modify_invoice_result': 'ModifyInvoice_Result'
        }
        self._modify_invoice_result = modify_invoice_result

    @classmethod
    def from_dict(cls, dikt) -> 'ModifyInvoiceResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ModifyInvoice_Result of this ModifyInvoiceResult.  # noqa: E501
        :rtype: ModifyInvoiceResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def modify_invoice_result(self) -> AllOfModifyInvoiceResultModifyInvoiceResult:
        """Gets the modify_invoice_result of this ModifyInvoiceResult.


        :return: The modify_invoice_result of this ModifyInvoiceResult.
        :rtype: AllOfModifyInvoiceResultModifyInvoiceResult
        """
        return self._modify_invoice_result

    @modify_invoice_result.setter
    def modify_invoice_result(self, modify_invoice_result: AllOfModifyInvoiceResultModifyInvoiceResult):
        """Sets the modify_invoice_result of this ModifyInvoiceResult.


        :param modify_invoice_result: The modify_invoice_result of this ModifyInvoiceResult.
        :type modify_invoice_result: AllOfModifyInvoiceResultModifyInvoiceResult
        """
        if modify_invoice_result is None:
            raise ValueError("Invalid value for `modify_invoice_result`, must not be `None`")  # noqa: E501

        self._modify_invoice_result = modify_invoice_result
