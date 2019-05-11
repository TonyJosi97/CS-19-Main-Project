#!/bin/bash
python comp.py $1 temp__compressed && python make_ascii.py && python newAES_ENC.py temp__asciicompressed temp__encrypted && python pvdEmbed.py temp__encrypted test.png