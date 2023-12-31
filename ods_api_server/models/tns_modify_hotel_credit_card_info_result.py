# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.all_oftns_modify_hotel_credit_card_info_result_modify_credit_card_info import AllOftnsModifyHotelCreditCardInfoResultModifyCreditCardInfo  # noqa: F401,E501
from ods_api_server import util


class TnsModifyHotelCreditCardInfoResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, modify_credit_card_info: AllOftnsModifyHotelCreditCardInfoResultModifyCreditCardInfo=None):  # noqa: E501
        """TnsModifyHotelCreditCardInfoResult - a model defined in Swagger

        :param modify_credit_card_info: The modify_credit_card_info of this TnsModifyHotelCreditCardInfoResult.  # noqa: E501
        :type modify_credit_card_info: AllOftnsModifyHotelCreditCardInfoResultModifyCreditCardInfo
        """
        self.swagger_types = {
            'modify_credit_card_info': AllOftnsModifyHotelCreditCardInfoResultModifyCreditCardInfo
        }

        self.attribute_map = {
            'modify_credit_card_info': 'modifyCreditCardInfo'
        }
        self._modify_credit_card_info = modify_credit_card_info

    @classmethod
    def from_dict(cls, dikt) -> 'TnsModifyHotelCreditCardInfoResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tns_ModifyHotelCreditCardInfo_Result of this TnsModifyHotelCreditCardInfoResult.  # noqa: E501
        :rtype: TnsModifyHotelCreditCardInfoResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def modify_credit_card_info(self) -> AllOftnsModifyHotelCreditCardInfoResultModifyCreditCardInfo:
        """Gets the modify_credit_card_info of this TnsModifyHotelCreditCardInfoResult.


        :return: The modify_credit_card_info of this TnsModifyHotelCreditCardInfoResult.
        :rtype: AllOftnsModifyHotelCreditCardInfoResultModifyCreditCardInfo
        """
        return self._modify_credit_card_info

    @modify_credit_card_info.setter
    def modify_credit_card_info(self, modify_credit_card_info: AllOftnsModifyHotelCreditCardInfoResultModifyCreditCardInfo):
        """Sets the modify_credit_card_info of this TnsModifyHotelCreditCardInfoResult.


        :param modify_credit_card_info: The modify_credit_card_info of this TnsModifyHotelCreditCardInfoResult.
        :type modify_credit_card_info: AllOftnsModifyHotelCreditCardInfoResultModifyCreditCardInfo
        """
        if modify_credit_card_info is None:
            raise ValueError("Invalid value for `modify_credit_card_info`, must not be `None`")  # noqa: E501

        self._modify_credit_card_info = modify_credit_card_info
