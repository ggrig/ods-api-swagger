# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ods_api_server.models.base_model_ import Model
from ods_api_server.models.q20_document import Q20Document  # noqa: F401,E501
from ods_api_server import util


class Q20Documents(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, document: List[Q20Document]=None):  # noqa: E501
        """Q20Documents - a model defined in Swagger

        :param document: The document of this Q20Documents.  # noqa: E501
        :type document: List[Q20Document]
        """
        self.swagger_types = {
            'document': List[Q20Document]
        }

        self.attribute_map = {
            'document': 'Document'
        }
        self._document = document

    @classmethod
    def from_dict(cls, dikt) -> 'Q20Documents':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The q20_Documents of this Q20Documents.  # noqa: E501
        :rtype: Q20Documents
        """
        return util.deserialize_model(dikt, cls)

    @property
    def document(self) -> List[Q20Document]:
        """Gets the document of this Q20Documents.


        :return: The document of this Q20Documents.
        :rtype: List[Q20Document]
        """
        return self._document

    @document.setter
    def document(self, document: List[Q20Document]):
        """Sets the document of this Q20Documents.


        :param document: The document of this Q20Documents.
        :type document: List[Q20Document]
        """
        if document is None:
            raise ValueError("Invalid value for `document`, must not be `None`")  # noqa: E501

        self._document = document
