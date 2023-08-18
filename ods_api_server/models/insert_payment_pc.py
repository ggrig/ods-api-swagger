# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.all_of_insert_payment_pc_insert_payment_pc import AllOfInsertPaymentPCInsertPaymentPc  # noqa: F401,E501
from ods_api_server import util


class InsertPaymentPC(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, insert_payment_pc: AllOfInsertPaymentPCInsertPaymentPc=None):  # noqa: E501
        """InsertPaymentPC - a model defined in Swagger

        :param insert_payment_pc: The insert_payment_pc of this InsertPaymentPC.  # noqa: E501
        :type insert_payment_pc: AllOfInsertPaymentPCInsertPaymentPc
        """
        self.swagger_types = {
            'insert_payment_pc': AllOfInsertPaymentPCInsertPaymentPc
        }

        self.attribute_map = {
            'insert_payment_pc': 'InsertPaymentPC'
        }
        self._insert_payment_pc = insert_payment_pc

    @classmethod
    def from_dict(cls, dikt) -> 'InsertPaymentPC':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InsertPaymentPC of this InsertPaymentPC.  # noqa: E501
        :rtype: InsertPaymentPC
        """
        return util.deserialize_model(dikt, cls)

    @property
    def insert_payment_pc(self) -> AllOfInsertPaymentPCInsertPaymentPc:
        """Gets the insert_payment_pc of this InsertPaymentPC.


        :return: The insert_payment_pc of this InsertPaymentPC.
        :rtype: AllOfInsertPaymentPCInsertPaymentPc
        """
        return self._insert_payment_pc

    @insert_payment_pc.setter
    def insert_payment_pc(self, insert_payment_pc: AllOfInsertPaymentPCInsertPaymentPc):
        """Sets the insert_payment_pc of this InsertPaymentPC.


        :param insert_payment_pc: The insert_payment_pc of this InsertPaymentPC.
        :type insert_payment_pc: AllOfInsertPaymentPCInsertPaymentPc
        """
        if insert_payment_pc is None:
            raise ValueError("Invalid value for `insert_payment_pc`, must not be `None`")  # noqa: E501

        self._insert_payment_pc = insert_payment_pc
