# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.confirm_invoice import ConfirmInvoice  # noqa: F401,E501
from ods_api_server import util


class ConfirmInvoiceBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, confirm_invoice: object=None):  # noqa: E501
        """ConfirmInvoiceBody - a model defined in Swagger

        :param confirm_invoice: The confirm_invoice of this ConfirmInvoiceBody.  # noqa: E501
        :type confirm_invoice: object
        """
        self.swagger_types = {
            'confirm_invoice': object
        }

        self.attribute_map = {
            'confirm_invoice': 'ConfirmInvoice'
        }
        self._confirm_invoice = confirm_invoice

    @classmethod
    def from_dict(cls, dikt) -> 'ConfirmInvoiceBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ConfirmInvoice_body of this ConfirmInvoiceBody.  # noqa: E501
        :rtype: ConfirmInvoiceBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def confirm_invoice(self) -> object:
        """Gets the confirm_invoice of this ConfirmInvoiceBody.


        :return: The confirm_invoice of this ConfirmInvoiceBody.
        :rtype: object
        """
        return self._confirm_invoice

    @confirm_invoice.setter
    def confirm_invoice(self, confirm_invoice: object):
        """Sets the confirm_invoice of this ConfirmInvoiceBody.


        :param confirm_invoice: The confirm_invoice of this ConfirmInvoiceBody.
        :type confirm_invoice: object
        """
        if confirm_invoice is None:
            raise ValueError("Invalid value for `confirm_invoice`, must not be `None`")  # noqa: E501

        self._confirm_invoice = confirm_invoice
