# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.all_of_change_customer_address_result_change_customer_address_result import AllOfChangeCustomerAddressResultChangeCustomerAddressResult  # noqa: F401,E501
from ods_api_server import util


class ChangeCustomerAddressResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, change_customer_address_result: AllOfChangeCustomerAddressResultChangeCustomerAddressResult=None):  # noqa: E501
        """ChangeCustomerAddressResult - a model defined in Swagger

        :param change_customer_address_result: The change_customer_address_result of this ChangeCustomerAddressResult.  # noqa: E501
        :type change_customer_address_result: AllOfChangeCustomerAddressResultChangeCustomerAddressResult
        """
        self.swagger_types = {
            'change_customer_address_result': AllOfChangeCustomerAddressResultChangeCustomerAddressResult
        }

        self.attribute_map = {
            'change_customer_address_result': 'ChangeCustomerAddress_Result'
        }
        self._change_customer_address_result = change_customer_address_result

    @classmethod
    def from_dict(cls, dikt) -> 'ChangeCustomerAddressResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ChangeCustomerAddress_Result of this ChangeCustomerAddressResult.  # noqa: E501
        :rtype: ChangeCustomerAddressResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def change_customer_address_result(self) -> AllOfChangeCustomerAddressResultChangeCustomerAddressResult:
        """Gets the change_customer_address_result of this ChangeCustomerAddressResult.


        :return: The change_customer_address_result of this ChangeCustomerAddressResult.
        :rtype: AllOfChangeCustomerAddressResultChangeCustomerAddressResult
        """
        return self._change_customer_address_result

    @change_customer_address_result.setter
    def change_customer_address_result(self, change_customer_address_result: AllOfChangeCustomerAddressResultChangeCustomerAddressResult):
        """Sets the change_customer_address_result of this ChangeCustomerAddressResult.


        :param change_customer_address_result: The change_customer_address_result of this ChangeCustomerAddressResult.
        :type change_customer_address_result: AllOfChangeCustomerAddressResultChangeCustomerAddressResult
        """
        if change_customer_address_result is None:
            raise ValueError("Invalid value for `change_customer_address_result`, must not be `None`")  # noqa: E501

        self._change_customer_address_result = change_customer_address_result
