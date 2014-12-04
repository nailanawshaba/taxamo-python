#!/usr/bin/env python
"""
Copyright 2014 Taxamo, Ltd.

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
class Country_schema:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'ccn3': 'str',
            'name': 'str',
            'code': 'str',
            'code_long': 'str',
            'cca2': 'str',
            'callingCode': 'list[str]',
            'cca3': 'str',
            'tax_number_country_code': 'str',
            'codenum': 'str',
            'tax_supported': 'bool'

        }


        #Country ISO 3-digit code.
        self.ccn3 = None # str
        #Country name.
        self.name = None # str
        #Two letter ISO country code.
        self.code = None # str
        #Three letter ISO country code.
        self.code_long = None # str
        #Two letter ISO country code.
        self.cca2 = None # str
        #List of phone number calling codes.
        self.callingCode = None # list[str]
        #Three letter ISO country code.
        self.cca3 = None # str
        #VAT number country code. Important for Greece.
        self.tax_number_country_code = None # str
        #Country ISO 3-digit code.
        self.codenum = None # str
        #True if tax calculation supported for this country.
        self.tax_supported = None # bool
        
