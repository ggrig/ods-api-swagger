# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from ods_api_server.models.change_contact_information_body import ChangeContactInformationBody  # noqa: E501
from ods_api_server.models.change_customer_address_body import ChangeCustomerAddressBody  # noqa: E501
from ods_api_server.models.change_customer_address_v2_body import ChangeCustomerAddressV2Body  # noqa: E501
from ods_api_server.models.change_invoice_address_body import ChangeInvoiceAddressBody  # noqa: E501
from ods_api_server.models.confirm_invoice_body import ConfirmInvoiceBody  # noqa: E501
from ods_api_server.models.inline_response200 import InlineResponse200  # noqa: E501
from ods_api_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from ods_api_server.models.inline_response20010 import InlineResponse20010  # noqa: E501
from ods_api_server.models.inline_response20011 import InlineResponse20011  # noqa: E501
from ods_api_server.models.inline_response20012 import InlineResponse20012  # noqa: E501
from ods_api_server.models.inline_response20013 import InlineResponse20013  # noqa: E501
from ods_api_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from ods_api_server.models.inline_response2003 import InlineResponse2003  # noqa: E501
from ods_api_server.models.inline_response2004 import InlineResponse2004  # noqa: E501
from ods_api_server.models.inline_response2005 import InlineResponse2005  # noqa: E501
from ods_api_server.models.inline_response2006 import InlineResponse2006  # noqa: E501
from ods_api_server.models.inline_response2007 import InlineResponse2007  # noqa: E501
from ods_api_server.models.inline_response2008 import InlineResponse2008  # noqa: E501
from ods_api_server.models.inline_response2009 import InlineResponse2009  # noqa: E501
from ods_api_server.models.insert_payment_body import InsertPaymentBody  # noqa: E501
from ods_api_server.models.insert_payment_v2_body import InsertPaymentV2Body  # noqa: E501
from ods_api_server.models.insert_payment_v3_body import InsertPaymentV3Body  # noqa: E501
from ods_api_server.models.modify_hotel_bank_account_info_body import ModifyHotelBankAccountInfoBody  # noqa: E501
from ods_api_server.models.modify_hotel_credit_card_info_body import ModifyHotelCreditCardInfoBody  # noqa: E501
from ods_api_server.models.modify_invoice_body import ModifyInvoiceBody  # noqa: E501
from ods_api_server.models.modify_invoice_v2_body import ModifyInvoiceV2Body  # noqa: E501
from ods_api_server.models.modify_invoice_v3_body import ModifyInvoiceV3Body  # noqa: E501
from ods_api_server.models.modify_invoice_v4_body import ModifyInvoiceV4Body  # noqa: E501
from ods_api_server.test import BaseTestCase


class TestHPPBindingController(BaseTestCase):
    """HPPBindingController integration test stubs"""

    def test_change_contact_information(self):
        """Test case for change_contact_information

        ChangeContactInformation
        """
        body = ChangeContactInformationBody()
        response = self.client.open(
            '/Marquardt-Informatik/HPP/1.0.0.0/ChangeContactInformation',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_change_customer_address(self):
        """Test case for change_customer_address

        ChangeCustomerAddress
        """
        body = ChangeCustomerAddressBody()
        response = self.client.open(
            '/Marquardt-Informatik/HPP/1.0.0.0/ChangeCustomerAddress',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_change_customer_address_v2(self):
        """Test case for change_customer_address_v2

        ChangeCustomerAddressV2
        """
        body = ChangeCustomerAddressV2Body()
        response = self.client.open(
            '/Marquardt-Informatik/HPP/1.0.0.0/ChangeCustomerAddressV2',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_change_invoice_address(self):
        """Test case for change_invoice_address

        ChangeInvoiceAddress
        """
        body = ChangeInvoiceAddressBody()
        response = self.client.open(
            '/Marquardt-Informatik/HPP/1.0.0.0/ChangeInvoiceAddress',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_confirm_invoice(self):
        """Test case for confirm_invoice

        ConfirmInvoice
        """
        body = ConfirmInvoiceBody()
        response = self.client.open(
            '/Marquardt-Informatik/HPP/1.0.0.0/ConfirmInvoice',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_insert_payment(self):
        """Test case for insert_payment

        InsertPayment
        """
        body = InsertPaymentBody()
        response = self.client.open(
            '/Marquardt-Informatik/HPP/1.0.0.0/InsertPayment',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_insert_payment_v2(self):
        """Test case for insert_payment_v2

        InsertPaymentV2
        """
        body = InsertPaymentV2Body()
        response = self.client.open(
            '/Marquardt-Informatik/HPP/1.0.0.0/InsertPaymentV2',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_insert_payment_v3(self):
        """Test case for insert_payment_v3

        InsertPaymentV3
        """
        body = InsertPaymentV3Body()
        response = self.client.open(
            '/Marquardt-Informatik/HPP/1.0.0.0/InsertPaymentV3',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modify_hotel_bank_account_info(self):
        """Test case for modify_hotel_bank_account_info

        ModifyHotelBankAccountInfo
        """
        body = ModifyHotelBankAccountInfoBody()
        response = self.client.open(
            '/Marquardt-Informatik/HPP/1.0.0.0/ModifyHotelBankAccountInfo',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modify_hotel_credit_card_info(self):
        """Test case for modify_hotel_credit_card_info

        ModifyHotelCreditCardInfo
        """
        body = ModifyHotelCreditCardInfoBody()
        response = self.client.open(
            '/Marquardt-Informatik/HPP/1.0.0.0/ModifyHotelCreditCardInfo',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modify_invoice(self):
        """Test case for modify_invoice

        ModifyInvoice
        """
        body = ModifyInvoiceBody()
        response = self.client.open(
            '/Marquardt-Informatik/HPP/1.0.0.0/ModifyInvoice',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modify_invoice_v2(self):
        """Test case for modify_invoice_v2

        ModifyInvoiceV2
        """
        body = ModifyInvoiceV2Body()
        response = self.client.open(
            '/Marquardt-Informatik/HPP/1.0.0.0/ModifyInvoiceV2',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modify_invoice_v3(self):
        """Test case for modify_invoice_v3

        ModifyInvoiceV3
        """
        body = ModifyInvoiceV3Body()
        response = self.client.open(
            '/Marquardt-Informatik/HPP/1.0.0.0/ModifyInvoiceV3',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modify_invoice_v4(self):
        """Test case for modify_invoice_v4

        ModifyInvoiceV4
        """
        body = ModifyInvoiceV4Body()
        response = self.client.open(
            '/Marquardt-Informatik/HPP/1.0.0.0/ModifyInvoiceV4',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
