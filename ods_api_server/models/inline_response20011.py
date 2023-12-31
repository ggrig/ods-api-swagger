# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.confirm_invoice_result import ConfirmInvoiceResult  # noqa: F401,E501
from ods_api_server import util


class InlineResponse20011(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, confirm_invoice_result: object=None):  # noqa: E501
        """InlineResponse20011 - a model defined in Swagger

        :param confirm_invoice_result: The confirm_invoice_result of this InlineResponse20011.  # noqa: E501
        :type confirm_invoice_result: object
        """
        self.swagger_types = {
            'confirm_invoice_result': object
        }

        self.attribute_map = {
            'confirm_invoice_result': 'ConfirmInvoice_Result'
        }
        self._confirm_invoice_result = confirm_invoice_result

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse20011':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_11 of this InlineResponse20011.  # noqa: E501
        :rtype: InlineResponse20011
        """
        return util.deserialize_model(dikt, cls)

    @property
    def confirm_invoice_result(self) -> object:
        """Gets the confirm_invoice_result of this InlineResponse20011.


        :return: The confirm_invoice_result of this InlineResponse20011.
        :rtype: object
        """
        return self._confirm_invoice_result

    @confirm_invoice_result.setter
    def confirm_invoice_result(self, confirm_invoice_result: object):
        """Sets the confirm_invoice_result of this InlineResponse20011.


        :param confirm_invoice_result: The confirm_invoice_result of this InlineResponse20011.
        :type confirm_invoice_result: object
        """
        if confirm_invoice_result is None:
            raise ValueError("Invalid value for `confirm_invoice_result`, must not be `None`")  # noqa: E501

        self._confirm_invoice_result = confirm_invoice_result
