#!/bin/bash
python newAES_DEC.py embedlog.logAES embedlog.log && python pvdExtract.py $1 temp__extracted