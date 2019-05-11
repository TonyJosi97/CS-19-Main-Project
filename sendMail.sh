#!/bin/bash
python newAES_ENC.py embedlog.log embedlog.logAES && python sendMail.py $1 $2 && rm temp__asciicompressed && rm temp__compressed && rm temp__encrypted && rm embedlog.log && rm embedlog.logAES && rm protest.png && rm subject && rm to
