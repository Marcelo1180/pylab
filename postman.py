 #!/usr/bin/python
 # -*- coding: utf-8 -*-
import sys
import json
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import Terminal256Formatter
from dracula import DraculaStyle
from libs.buscar import Buscar
from libs.consulta import BooleanSearch


if __name__ == "__main__":
    xinput = " ".join(sys.argv[1:])
    # uinput, uciiu, upobjeto = xinput.split(",")
    # uciiu = uciiu.split(":")
    # upobjeto = upobjeto.split(" ")
    # upobjeto = " OR ".join([w+"~" for w in upobjeto])
    uinput = xinput
    uciiu = ""
    upobjeto = ""
    response = Buscar.search(uinput, uciiu, upobjeto)
    xhead = "\n".join([
        "xsearch: %s" % uinput,
        "bsearch: %s" % BooleanSearch.query(uinput),
        "ciiu: %s" % str(uciiu),
        "pobjeto: %s" % str(upobjeto),
    ])
    xcode = json.dumps(json.loads(response), sort_keys=True, indent=4, ensure_ascii=False)
    print(highlight(xhead, JsonLexer(), Terminal256Formatter(style=DraculaStyle)))
    print(highlight(xcode, JsonLexer(), Terminal256Formatter(style=DraculaStyle)))
