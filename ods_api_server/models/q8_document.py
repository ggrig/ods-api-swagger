# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server import util


class Q8Document(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, document_no: str=None):  # noqa: E501
        """Q8Document - a model defined in Swagger

        :param document_no: The document_no of this Q8Document.  # noqa: E501
        :type document_no: str
        """
        self.swagger_types = {
            'document_no': str
        }

        self.attribute_map = {
            'document_no': 'DocumentNo'
        }
        self._document_no = document_no

    @classmethod
    def from_dict(cls, dikt) -> 'Q8Document':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The q8_Document of this Q8Document.  # noqa: E501
        :rtype: Q8Document
        """
        return util.deserialize_model(dikt, cls)

    @property
    def document_no(self) -> str:
        """Gets the document_no of this Q8Document.


        :return: The document_no of this Q8Document.
        :rtype: str
        """
        return self._document_no

    @document_no.setter
    def document_no(self, document_no: str):
        """Sets the document_no of this Q8Document.


        :param document_no: The document_no of this Q8Document.
        :type document_no: str
        """
        if document_no is None:
            raise ValueError("Invalid value for `document_no`, must not be `None`")  # noqa: E501

        self._document_no = document_no
