import connexion
import six

from ods_api_server.models.change_contact_information_body import ChangeContactInformationBody  # noqa: E501
from ods_api_server.models.change_contact_information_result import ChangeContactInformationResult
from ods_api_server.models.change_customer_address_body import ChangeCustomerAddressBody  # noqa: E501
from ods_api_server.models.change_customer_address_v2_body import ChangeCustomerAddressV2Body  # noqa: E501
from ods_api_server.models.change_customer_address_v2_result import ChangeCustomerAddressV2Result
from ods_api_server.models.change_invoice_address_body import ChangeInvoiceAddressBody  # noqa: E501
from ods_api_server.models.change_invoice_address_result import ChangeInvoiceAddressResult
from ods_api_server.models.confirm_invoice_body import ConfirmInvoiceBody  # noqa: E501
from ods_api_server.models.confirm_invoice_result import ConfirmInvoiceResult
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
from ods_api_server.models.insert_payment_v3_result import InsertPaymentV3Result
from ods_api_server.models.modify_hotel_bank_account_info_body import ModifyHotelBankAccountInfoBody  # noqa: E501
from ods_api_server.models.modify_hotel_bank_account_info_result import ModifyHotelBankAccountInfoResult
from ods_api_server.models.modify_hotel_credit_card_info_body import ModifyHotelCreditCardInfoBody  # noqa: E501
from ods_api_server.models.modify_hotel_credit_card_info_result import ModifyHotelCreditCardInfoResult
from ods_api_server.models.modify_invoice_body import ModifyInvoiceBody  # noqa: E501
from ods_api_server.models.modify_invoice_v2_body import ModifyInvoiceV2Body  # noqa: E501
from ods_api_server.models.modify_invoice_v3_body import ModifyInvoiceV3Body  # noqa: E501
from ods_api_server.models.modify_invoice_v4_body import ModifyInvoiceV4Body  # noqa: E501
from ods_api_server.models.modify_invoice_v4_result import ModifyInvoiceV4Result
from ods_api_server import util

import logging
logger = logging.getLogger(__name__)

def change_contact_information(body):  # noqa: E501
    logger.info('>> ChangeContactInformation')

    """ChangeContactInformation

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2002
    """
    # if connexion.request.is_json:
    #     body = ChangeContactInformationBody.from_dict(connexion.request.get_json())  # noqa: E501
    # return 'do some magic!'

    try:
        if connexion.request.is_json:
            body = ChangeContactInformationBody.from_dict(connexion.request.get_json())  # noqa: E501
            result = ChangeContactInformationResult(body.change_contact_information)
            return result
        else:
            logger.info(f'Not JSON {connexion.request}')
    except Exception as ex:
        logger.error(f'ChangeContactInformationBody exception: {str(ex)}')

    return '<< ChangeContactInformationBody wrong processing path'

def change_customer_address(body):  # noqa: E501
    logger.info('>> ChangeCustomerAddress')

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
    logger.info('>> ChangeCustomerAddressV2')

    """ChangeCustomerAddressV2

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2006
    """
    try:
        if connexion.request.is_json:
            body = ChangeCustomerAddressV2Body.from_dict(connexion.request.get_json())  # noqa: E501
            result = ChangeCustomerAddressV2Result(body.change_customer_address_v2)
            return result 
        else:
            logger.info(f'Not JSON {connexion.request}')
    except Exception as ex:
        logger.error(f'ChangeCustomerAddressV2 exception: {str(ex)}')

    return '<< ChangeCustomerAddressV2 wrong processing path'

def change_invoice_address(body):  # noqa: E501
    logger.info('>> ChangeInvoiceAddress')

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
            logger.info(f'Not JSON {connexion.request}')
    except Exception as ex:
        logger.error(f'ChangeInvoiceAddress exception: {str(ex)}')

    return '<< ChangeInvoiceAddress wrong processing path'


def confirm_invoice(body):  # noqa: E501
    logger.info('>> ConfirmInvoice')

    """ConfirmInvoice

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse20011
    """
    try:
        if connexion.request.is_json:
            body = ConfirmInvoiceBody.from_dict(connexion.request.get_json())  # noqa: E501
            result = ConfirmInvoiceResult(body.confirm_invoice)
            return result
        else:
            logger.info(f'Not JSON {connexion.request}')
    except Exception as ex:
        logger.error(f'ConfirmInvoiceBody exception: {str(ex)}')

    return '<< ConfirmInvoiceBody wrong processing path'

def insert_payment(body):  # noqa: E501
    logger.info('>> InsertPayment')

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
    logger.info('>> InsertPaymentV2')

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
    logger.info('>> InsertPaymentV3')

    """InsertPaymentV3

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2009
    """
    try:
        if connexion.request.is_json:
            body = InsertPaymentV3Body.from_dict(connexion.request.get_json())  # noqa: E501
            result = InsertPaymentV3Result(body.insert_payment_v3)
            return result
        else:
            logger.info(f'Not JSON {connexion.request}')
    except Exception as ex:
        logger.error(f'InsertPaymentV3Body exception: {str(ex)}')

    return '<< InsertPaymentV3Body wrong processing path'

def modify_hotel_bank_account_info(body):  # noqa: E501
    logger.info('>> ModifyHotelBankAccountInfo')

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
    logger.info('>> ModifyHotelCreditCardInfo')

    """ModifyHotelCreditCardInfo

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse20012
    """
    try:
        if connexion.request.is_json:
            body = ModifyHotelCreditCardInfoBody.from_dict(connexion.request.get_json())  # noqa: E501
            result = ModifyHotelCreditCardInfoResult(body.modify_hotel_credit_card_info)
            return result
        else:
            logger.info(f'Not JSON {connexion.request}')
    except Exception as ex:
        logger.error(f'ModifyHotelCreditCardInfoBody exception: {str(ex)}')

    return '<< ModifyHotelCreditCardInfoBody wrong processing path'

def modify_invoice(body):  # noqa: E501
    logger.info('>> ModifyInvoice')

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
    logger.info('>> ModifyInvoiceV2')

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
    logger.info('>> ModifyInvoiceV3')

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
    logger.info('>> ModifyInvoiceV4')

    """ModifyInvoiceV4

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse20010
    """
    try:
        if connexion.request.is_json:
            body = ModifyInvoiceV4Body.from_dict(connexion.request.get_json())  # noqa: E501
            result = ModifyInvoiceV4Result(body.modify_invoice_v4)
            return result
        else:
            logger.info(f'Not JSON {connexion.request}')
    except Exception as ex:
        logger.error(f'ModifyInvoiceV4Body exception: {str(ex)}')

    return '<< ModifyInvoiceV4Body wrong processing path'
