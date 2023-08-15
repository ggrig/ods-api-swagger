# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.all_of_change_contact_information_result_change_contact_information_result import AllOfChangeContactInformationResultChangeContactInformationResult  # noqa: F401,E501
from ods_api_server import util


class ChangeContactInformationResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, change_contact_information_result: AllOfChangeContactInformationResultChangeContactInformationResult=None):  # noqa: E501
        """ChangeContactInformationResult - a model defined in Swagger

        :param change_contact_information_result: The change_contact_information_result of this ChangeContactInformationResult.  # noqa: E501
        :type change_contact_information_result: AllOfChangeContactInformationResultChangeContactInformationResult
        """
        self.swagger_types = {
            'change_contact_information_result': AllOfChangeContactInformationResultChangeContactInformationResult
        }

        self.attribute_map = {
            'change_contact_information_result': 'ChangeContactInformation_Result'
        }
        self._change_contact_information_result = change_contact_information_result

    @classmethod
    def from_dict(cls, dikt) -> 'ChangeContactInformationResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ChangeContactInformation_Result of this ChangeContactInformationResult.  # noqa: E501
        :rtype: ChangeContactInformationResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def change_contact_information_result(self) -> AllOfChangeContactInformationResultChangeContactInformationResult:
        """Gets the change_contact_information_result of this ChangeContactInformationResult.


        :return: The change_contact_information_result of this ChangeContactInformationResult.
        :rtype: AllOfChangeContactInformationResultChangeContactInformationResult
        """
        return self._change_contact_information_result

    @change_contact_information_result.setter
    def change_contact_information_result(self, change_contact_information_result: AllOfChangeContactInformationResultChangeContactInformationResult):
        """Sets the change_contact_information_result of this ChangeContactInformationResult.


        :param change_contact_information_result: The change_contact_information_result of this ChangeContactInformationResult.
        :type change_contact_information_result: AllOfChangeContactInformationResultChangeContactInformationResult
        """
        if change_contact_information_result is None:
            raise ValueError("Invalid value for `change_contact_information_result`, must not be `None`")  # noqa: E501

        self._change_contact_information_result = change_contact_information_result
