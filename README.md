# pyAIC

This package define a series of function to manipulate, convert and (syntactically) validate AIC codes as described in the italian "Gazzetta Ufficiale della Repubblica Italiana" Serie Generale n.165 del 18-07-2014, attachment A.
The document describes two valid representation of an AIC code.

## Functions

The functions to validate a code are **is_base32_AIC** and **is_base32_AIC**.


The functions to convert between base32 and base10 representation are **from10to32** and **from32to10**.


The last char of a base10 code is a checksum, to check it use **check_AIC_base10_checksum**.
