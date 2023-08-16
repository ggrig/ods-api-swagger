import connexion
import six

from ods_api_server.models.change_contact_information_body import ChangeContactInformationBody  # noqa: E501
from ods_api_server.models.change_customer_address_body import ChangeCustomerAddressBody  # noqa: E501
from ods_api_server.models.change_customer_address_v2_body import ChangeCustomerAddressV2Body  # noqa: E501
from ods_api_server.models.change_invoice_address_body import ChangeInvoiceAddressBody  # noqa: E501
from ods_api_server.models.change_invoice_address_result import ChangeInvoiceAddressResult
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
from ods_api_server import util

import pprint

def change_contact_information(body):  # noqa: E501
    print('>> ChangeContactInformation')

    """ChangeContactInformation

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2002
    """
    if connexion.request.is_json:
        body = ChangeContactInformationBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def change_customer_address(body):  # noqa: E501
    print('>> ChangeCustomerAddress')

    """ChangeCustomerAddress

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2001
    """
    if connexion.request.is_json:
        body = ChangeCustomerAddressBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def change_customer_address_v2(body):  # noqa: E501
    print('>> ChangeCustomerAddressV2')

    """ChangeCustomerAddressV2

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2006
    """
    if connexion.request.is_json:
        body = ChangeCustomerAddressV2Body.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def change_invoice_address(body):  # noqa: E501
    print('>> ChangeInvoiceAddress')

    """ChangeInvoiceAddress

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    try:
        if connexion.request.is_json:
            body = ChangeInvoiceAddressBody.from_dict(connexion.request.get_json())  # noqa: E501
            result = ChangeInvoiceAddressResult(body.change_invoice_address)
            return result
        else:
            print(f'Not JSON {connexion.request}')
    except Exception as ex:
        print(f'ChangeInvoiceAddress exception: {str(ex)}')

    return '<< ChangeInvoiceAddress wrong processing path'


def confirm_invoice(body):  # noqa: E501
    print('>> ConfirmInvoice')

    """ConfirmInvoice

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse20011
    """
    if connexion.request.is_json:
        body = ConfirmInvoiceBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def insert_payment(body):  # noqa: E501
    print('>> InsertPayment')

    """InsertPayment

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2003
    """
    if connexion.request.is_json:
        body = InsertPaymentBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def insert_payment_v2(body):  # noqa: E501
    print('>> InsertPaymentV2')

    """InsertPaymentV2

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2005
    """
    if connexion.request.is_json:
        body = InsertPaymentV2Body.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def insert_payment_v3(body):  # noqa: E501
    print('>> InsertPaymentV3')

    """InsertPaymentV3

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2009
    """
    if connexion.request.is_json:
        body = InsertPaymentV3Body.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def modify_hotel_bank_account_info(body):  # noqa: E501
    print('>> ModifyHotelBankAccountInfo')

    """ModifyHotelBankAccountInfo

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse20013
    """
    if connexion.request.is_json:
        body = ModifyHotelBankAccountInfoBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def modify_hotel_credit_card_info(body):  # noqa: E501
    print('>> ModifyHotelCreditCardInfo')

    """ModifyHotelCreditCardInfo

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse20012
    """
    if connexion.request.is_json:
        body = ModifyHotelCreditCardInfoBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def modify_invoice(body):  # noqa: E501
    print('>> ModifyInvoice')

    """ModifyInvoice

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2004
    """
    if connexion.request.is_json:
        body = ModifyInvoiceBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def modify_invoice_v2(body):  # noqa: E501
    print('>> ModifyInvoiceV2')

    """ModifyInvoiceV2

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2007
    """
    if connexion.request.is_json:
        body = ModifyInvoiceV2Body.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def modify_invoice_v3(body):  # noqa: E501
    print('>> ModifyInvoiceV3')

    """ModifyInvoiceV3

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2008
    """
    if connexion.request.is_json:
        body = ModifyInvoiceV3Body.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def modify_invoice_v4(body):  # noqa: E501
    print('>> ModifyInvoiceV4')

    """ModifyInvoiceV4

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse20010
    """
    if connexion.request.is_json:
        body = ModifyInvoiceV4Body.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
