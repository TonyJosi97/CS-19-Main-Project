#!/bin/bash
python newAES_DEC.py $1 embedlog.log && python pvdExtract.py $2 temp__extracted