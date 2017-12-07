 #!/usr/bin/python
 # -*- coding: utf-8 -*-
import sys
import json
from libs.consulta import BooleanSearch


if __name__ == "__main__":
    xinput = " ".join(sys.argv[1:])
    print(BooleanSearch.query(xinput))
