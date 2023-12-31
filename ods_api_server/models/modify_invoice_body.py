# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.modify_invoice import ModifyInvoice  # noqa: F401,E501
from ods_api_server import util


class ModifyInvoiceBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, modify_invoice: object=None):  # noqa: E501
        """ModifyInvoiceBody - a model defined in Swagger

        :param modify_invoice: The modify_invoice of this ModifyInvoiceBody.  # noqa: E501
        :type modify_invoice: object
        """
        self.swagger_types = {
            'modify_invoice': object
        }

        self.attribute_map = {
            'modify_invoice': 'ModifyInvoice'
        }
        self._modify_invoice = modify_invoice

    @classmethod
    def from_dict(cls, dikt) -> 'ModifyInvoiceBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ModifyInvoice_body of this ModifyInvoiceBody.  # noqa: E501
        :rtype: ModifyInvoiceBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def modify_invoice(self) -> object:
        """Gets the modify_invoice of this ModifyInvoiceBody.


        :return: The modify_invoice of this ModifyInvoiceBody.
        :rtype: object
        """
        return self._modify_invoice

    @modify_invoice.setter
    def modify_invoice(self, modify_invoice: object):
        """Sets the modify_invoice of this ModifyInvoiceBody.


        :param modify_invoice: The modify_invoice of this ModifyInvoiceBody.
        :type modify_invoice: object
        """
        if modify_invoice is None:
            raise ValueError("Invalid value for `modify_invoice`, must not be `None`")  # noqa: E501

        self._modify_invoice = modify_invoice
