# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.all_oftns_modify_invoice_v4_modify_invoice import AllOftnsModifyInvoiceV4ModifyInvoice  # noqa: F401,E501
from ods_api_server import util


class TnsModifyInvoiceV4(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, modify_invoice: AllOftnsModifyInvoiceV4ModifyInvoice=None):  # noqa: E501
        """TnsModifyInvoiceV4 - a model defined in Swagger

        :param modify_invoice: The modify_invoice of this TnsModifyInvoiceV4.  # noqa: E501
        :type modify_invoice: AllOftnsModifyInvoiceV4ModifyInvoice
        """
        self.swagger_types = {
            'modify_invoice': AllOftnsModifyInvoiceV4ModifyInvoice
        }

        self.attribute_map = {
            'modify_invoice': 'modifyInvoice'
        }
        self._modify_invoice = modify_invoice

    @classmethod
    def from_dict(cls, dikt) -> 'TnsModifyInvoiceV4':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tns_ModifyInvoiceV4 of this TnsModifyInvoiceV4.  # noqa: E501
        :rtype: TnsModifyInvoiceV4
        """
        return util.deserialize_model(dikt, cls)

    @property
    def modify_invoice(self) -> AllOftnsModifyInvoiceV4ModifyInvoice:
        """Gets the modify_invoice of this TnsModifyInvoiceV4.


        :return: The modify_invoice of this TnsModifyInvoiceV4.
        :rtype: AllOftnsModifyInvoiceV4ModifyInvoice
        """
        return self._modify_invoice

    @modify_invoice.setter
    def modify_invoice(self, modify_invoice: AllOftnsModifyInvoiceV4ModifyInvoice):
        """Sets the modify_invoice of this TnsModifyInvoiceV4.


        :param modify_invoice: The modify_invoice of this TnsModifyInvoiceV4.
        :type modify_invoice: AllOftnsModifyInvoiceV4ModifyInvoice
        """
        if modify_invoice is None:
            raise ValueError("Invalid value for `modify_invoice`, must not be `None`")  # noqa: E501

        self._modify_invoice = modify_invoice
