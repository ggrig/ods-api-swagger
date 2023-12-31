# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.modify_hotel_credit_card_info import ModifyHotelCreditCardInfo  # noqa: F401,E501
from ods_api_server import util


class ModifyHotelCreditCardInfoBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, modify_hotel_credit_card_info: object=None):  # noqa: E501
        """ModifyHotelCreditCardInfoBody - a model defined in Swagger

        :param modify_hotel_credit_card_info: The modify_hotel_credit_card_info of this ModifyHotelCreditCardInfoBody.  # noqa: E501
        :type modify_hotel_credit_card_info: object
        """
        self.swagger_types = {
            'modify_hotel_credit_card_info': object
        }

        self.attribute_map = {
            'modify_hotel_credit_card_info': 'ModifyHotelCreditCardInfo'
        }
        self._modify_hotel_credit_card_info = modify_hotel_credit_card_info

    @classmethod
    def from_dict(cls, dikt) -> 'ModifyHotelCreditCardInfoBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ModifyHotelCreditCardInfo_body of this ModifyHotelCreditCardInfoBody.  # noqa: E501
        :rtype: ModifyHotelCreditCardInfoBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def modify_hotel_credit_card_info(self) -> object:
        """Gets the modify_hotel_credit_card_info of this ModifyHotelCreditCardInfoBody.


        :return: The modify_hotel_credit_card_info of this ModifyHotelCreditCardInfoBody.
        :rtype: object
        """
        return self._modify_hotel_credit_card_info

    @modify_hotel_credit_card_info.setter
    def modify_hotel_credit_card_info(self, modify_hotel_credit_card_info: object):
        """Sets the modify_hotel_credit_card_info of this ModifyHotelCreditCardInfoBody.


        :param modify_hotel_credit_card_info: The modify_hotel_credit_card_info of this ModifyHotelCreditCardInfoBody.
        :type modify_hotel_credit_card_info: object
        """
        if modify_hotel_credit_card_info is None:
            raise ValueError("Invalid value for `modify_hotel_credit_card_info`, must not be `None`")  # noqa: E501

        self._modify_hotel_credit_card_info = modify_hotel_credit_card_info
