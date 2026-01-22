##import pytest
##from test_credit_card_validator import credit_card_validator

class TestCredCardValidator:
    # ------ Overall Tests Invalid ------
    def test_empty_input(self):
        '''Testing if the input is blank'''
        assert credit_card_validator("") == False

    def test_no_input(self):
        '''Testing if the input is nothing/none'''
        assert credit_card_validator(None) == False

    def test_unsupported_prefix(self):
        '''Testing if this is a supported card type/incorrect prefix'''
        assert credit_card_validator("9911111111111117") == False
    
    def test_non_digit_characters(self):
        '''Testing an input containing non-digit characters'''
        assert credit_card_validator("4111-1111-1111-1111") == False

    def test_alpha_input(self):
        '''Testing alphabetic input'''
        assert credit_card_validator("abcd1234") == False
    
    # ------ VISA Tests Invaild Cases ------
    def test_visa_too_short(self):
        '''Testing if the required # of digits is short'''
        assert credit_card_validator("41111111111111") == False # only short by 1
    
    def test_visa_too_long(self):
        '''Testing if the digits go past the max #'''
        assert credit_card_validator("41111111111111111") == False # only one over
    
    def test_visa_fails_luhn(self):
        '''Testing if the Visa fails Luhn check'''
        assert credit_card_validator("4111111111111121") == False
    
    # Valid Test Cases (VISA)
    def test_vaild_visa(self):
        '''Testing a vaild VISA card #'''
        assert credit_card_validator("4111111111111111") == True

    
    # ------ AMEX Test Invaild Cases ------
    def test_amex_too_short(self):
        '''Testing if there are less than require # of digits'''
        assert credit_card_validator("37144963539843") == False # only one less
    
    def test_amex_too_long(self):
        '''Testing if there are too many # of digits'''
        assert credit_card_validator("3714496353984312") == False # only one over
    
    def test_amex_fails_luhn(self):
        '''Testing if the AMEX fails the Luhn check'''
        assert credit_card_validator("378282246310006") == False

    # Vaild Test Cases (AMEX)
    def test_vaild_amex_34(self):
        '''Testing a vaild AMEX card that starts with 34'''
        assert credit_card_validator("348282246310005") == True

    def test_vaild_amex_37(self):
        '''Testing a vaild AMEX card that starts with 37'''
        assert credit_card_validator("378282246310005") == True

    # ------ MasterCard Test Invaild Cases ------
    def test_mastercard_fails(self):
        '''Testing a MasterCard that fails the Luhn check'''
        assert credit_card_validator("5555555555554445") == False
    
    # Vaild Cases (Mastercard)
    def test_valid_mastercard_51(self):
        '''Testing a valid MasterCard with prefix 51'''
        assert credit_card_validator("5555555555554444") == True

    def test_valid_mastercard_lower_boundary(self):
        '''Testing MasterCard lower boundary prefix 2221'''
        assert credit_card_validator("2221000000000009") == True

    def test_valid_mastercard_upper_boundary(self):
        '''Testing MasterCard upper boundary prefix 2720'''
        assert credit_card_validator("2720999999999993") == True