#!/usr/bin/env python
"""
Copyright 2014-2015 Taxamo, Ltd.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
class Us_tax_exemption_certificate_details_schema:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'single_purchase_order_identifier': 'str',
            'purchaser_business_type': 'str',
            'purchaser_exemption_reason_value': 'str',
            'purchaser_state': 'str',
            'purchaser_zip': 'str',
            'purchaser_city': 'str',
            'purchaser_last_name': 'str',
            'purchaser_exemption_reason': 'str',
            'single_purchase': 'bool',
            'purchaser_tax_id': 'us_tax_id',
            'purchaser_address2': 'str',
            'purchaser_address1': 'str',
            'purchaser_business_type_other_value': 'str',
            'purchaser_first_name': 'str',
            'exempt_states': 'list[us_tax_exempt_state]',
            'purchaser_title': 'str'

        }


        #Purchase/order identifier for single purchase.
        self.single_purchase_order_identifier = None # str
        #Purchaser business type.
        self.purchaser_business_type = None # str
        #The value of exemption reason.
        self.purchaser_exemption_reason_value = None # str
        #Purchaser's state.
        self.purchaser_state = None # str
        #Purchaser's zip code.
        self.purchaser_zip = None # str
        #Purchaser's city.
        self.purchaser_city = None # str
        #Purchaser's last name.
        self.purchaser_last_name = None # str
        #The reason for exemption reason.
        self.purchaser_exemption_reason = None # str
        #Set to true if this certificate is valid for single purchase only.
        self.single_purchase = None # bool
        #Purchaser's TAX ID.
        self.purchaser_tax_id = None # us_tax_id
        #Purchaser's second address line.
        self.purchaser_address2 = None # str
        #Purchaser's first address line.
        self.purchaser_address1 = None # str
        #If business type is other, a short description must be provided.
        self.purchaser_business_type_other_value = None # str
        #Purchaser's first name.
        self.purchaser_first_name = None # str
        #List of states where the certificate is valid.
        self.exempt_states = None # list[us_tax_exempt_state]
        #Purchaser's title.
        self.purchaser_title = None # str
        