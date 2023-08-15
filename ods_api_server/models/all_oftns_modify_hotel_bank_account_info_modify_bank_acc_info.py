# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.q28_hotel_bank_account_info import Q28HotelBankAccountInfo  # noqa: F401,E501
from ods_api_server.models.q28_hotel_bank_account_info_list import Q28HotelBankAccountInfoList  # noqa: F401,E501
from ods_api_server import util


class AllOftnsModifyHotelBankAccountInfoModifyBankAccInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, hotel_bank_account_info: List[Q28HotelBankAccountInfo]=None):  # noqa: E501
        """AllOftnsModifyHotelBankAccountInfoModifyBankAccInfo - a model defined in Swagger

        :param hotel_bank_account_info: The hotel_bank_account_info of this AllOftnsModifyHotelBankAccountInfoModifyBankAccInfo.  # noqa: E501
        :type hotel_bank_account_info: List[Q28HotelBankAccountInfo]
        """
        self.swagger_types = {
            'hotel_bank_account_info': List[Q28HotelBankAccountInfo]
        }

        self.attribute_map = {
            'hotel_bank_account_info': 'HotelBankAccountInfo'
        }
        self._hotel_bank_account_info = hotel_bank_account_info

    @classmethod
    def from_dict(cls, dikt) -> 'AllOftnsModifyHotelBankAccountInfoModifyBankAccInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AllOftns_ModifyHotelBankAccountInfoModifyBankAccInfo of this AllOftnsModifyHotelBankAccountInfoModifyBankAccInfo.  # noqa: E501
        :rtype: AllOftnsModifyHotelBankAccountInfoModifyBankAccInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def hotel_bank_account_info(self) -> List[Q28HotelBankAccountInfo]:
        """Gets the hotel_bank_account_info of this AllOftnsModifyHotelBankAccountInfoModifyBankAccInfo.


        :return: The hotel_bank_account_info of this AllOftnsModifyHotelBankAccountInfoModifyBankAccInfo.
        :rtype: List[Q28HotelBankAccountInfo]
        """
        return self._hotel_bank_account_info

    @hotel_bank_account_info.setter
    def hotel_bank_account_info(self, hotel_bank_account_info: List[Q28HotelBankAccountInfo]):
        """Sets the hotel_bank_account_info of this AllOftnsModifyHotelBankAccountInfoModifyBankAccInfo.


        :param hotel_bank_account_info: The hotel_bank_account_info of this AllOftnsModifyHotelBankAccountInfoModifyBankAccInfo.
        :type hotel_bank_account_info: List[Q28HotelBankAccountInfo]
        """
        if hotel_bank_account_info is None:
            raise ValueError("Invalid value for `hotel_bank_account_info`, must not be `None`")  # noqa: E501

        self._hotel_bank_account_info = hotel_bank_account_info
