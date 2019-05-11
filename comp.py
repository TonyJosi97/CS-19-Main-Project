import sys
import arcode

use_static_model = False
ar = arcode.ArithmeticCode(use_static_model)

ar.encode_file(sys.argv[1], sys.argv[2])
print("Compression Completed...")