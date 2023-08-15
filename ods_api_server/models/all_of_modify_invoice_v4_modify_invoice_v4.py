# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.tns_modify_invoice_v4 import TnsModifyInvoiceV4  # noqa: F401,E501
from ods_api_server import util


class AllOfModifyInvoiceV4ModifyInvoiceV4(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, modify_invoice: object=None):  # noqa: E501
        """AllOfModifyInvoiceV4ModifyInvoiceV4 - a model defined in Swagger

        :param modify_invoice: The modify_invoice of this AllOfModifyInvoiceV4ModifyInvoiceV4.  # noqa: E501
        :type modify_invoice: object
        """
        self.swagger_types = {
            'modify_invoice': object
        }

        self.attribute_map = {
            'modify_invoice': 'modifyInvoice'
        }
        self._modify_invoice = modify_invoice

    @classmethod
    def from_dict(cls, dikt) -> 'AllOfModifyInvoiceV4ModifyInvoiceV4':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AllOfModifyInvoiceV4ModifyInvoiceV4 of this AllOfModifyInvoiceV4ModifyInvoiceV4.  # noqa: E501
        :rtype: AllOfModifyInvoiceV4ModifyInvoiceV4
        """
        return util.deserialize_model(dikt, cls)

    @property
    def modify_invoice(self) -> object:
        """Gets the modify_invoice of this AllOfModifyInvoiceV4ModifyInvoiceV4.


        :return: The modify_invoice of this AllOfModifyInvoiceV4ModifyInvoiceV4.
        :rtype: object
        """
        return self._modify_invoice

    @modify_invoice.setter
    def modify_invoice(self, modify_invoice: object):
        """Sets the modify_invoice of this AllOfModifyInvoiceV4ModifyInvoiceV4.


        :param modify_invoice: The modify_invoice of this AllOfModifyInvoiceV4ModifyInvoiceV4.
        :type modify_invoice: object
        """
        if modify_invoice is None:
            raise ValueError("Invalid value for `modify_invoice`, must not be `None`")  # noqa: E501

        self._modify_invoice = modify_invoice
