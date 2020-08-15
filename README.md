# Payments Card Numbers

1. A payment card can be a debit card, a credit card, a store card etc. Basically any card that can be used for payments

2. The leading first digit of a card number indicates the industry of the issuing authority
    Refer to the file industry_identifier.csv to know what digit points to which industry

3. Including the leading digit, the first 6 digits are called as IIN or BIN.
    IIN = Issuer Identification Number
    BIN = Bank Identification Number
    
    A new standard for IIN/BIN being of 8 digits was published in Jan 2017 but it is yet to be implemented

4. The total digits in a payment card, like the debit or credit cards, can range between 13 digits to 19 digits. The most common VISA and Master Cards have 16 digits while AMEX has 15 digits
    Refer to the file iin_ranges.csv to know ranges for different credit card issuers (Source: https://www.freeformatter.com/credit-card-number-generator-validator.html)

5. The last digit in a card number is a checksum digit

# This Repository

* For a given IIN and Card Length, it will generate the card numbers which are valid as per the Lunh's Algorithm
* The generated card number are not usable without the valid owner name, expiration date and CVV
