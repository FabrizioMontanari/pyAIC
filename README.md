# pyAIC

This package define a series of function to manipulate, convert and (syntactically) validate AIC codes as described in the italian "Gazzetta Ufficiale della Repubblica Italiana" [Serie Generale n.165 del 18-07-2014](https://www.gazzettaufficiale.it/atto/serie_generale/caricaDettaglioAtto/originario?atto.dataPubblicazioneGazzetta=2014-07-18&atto.codiceRedazionale=14A05668&elenco30giorni=true), [attachment A](https://www.gazzettaufficiale.it/do/atto/serie_generale/caricaPdf?cdimg=14A0566800100010110001&dgu=2014-07-18&art.dataPubblicazioneGazzetta=2014-07-18&art.codiceRedazionale=14A05668&art.num=1&art.tiposerie=SG).
The document describes two valid representation of an AIC code.

## Functions

The functions to validate a code are **is_base32_AIC** and **is_base32_AIC**. Using strict=True will validate only real AIC codes (they must start with "0"), while strict=False will validate PARAF codes.


The functions to convert between base32 and base10 representation are **from10to32** and **from32to10**.


The last char of a base10 code is a checksum, to check it use **check_AIC_base10_checksum**, to compute it use **calc_AIC_base10_checksum**.

