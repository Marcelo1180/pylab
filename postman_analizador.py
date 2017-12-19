 #!/usr/bin/python
 # -*- coding: utf-8 -*-
import sys
import json
import requests
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import Terminal256Formatter
from dracula import DraculaStyle
from libs.buscar import Buscar
from libs.consulta import BooleanSearch


if __name__ == "__main__":
    # xinput = " ".join(sys.argv[1:])
    # # uinput, uciiu, upobjeto = xinput.split(",")
    # # uciiu = uciiu.split(":")
    # # upobjeto = upobjeto.split(" ")
    # # upobjeto = " OR ".join([w+"~" for w in upobjeto])
    # uinput = xinput
    # uciiu = ""
    # upobjeto = ""
    # response = Buscar.search(uinput, uciiu, upobjeto)
    # xhead = "\n".join([
    #     "xsearch: %s" % uinput,
    #     "bsearch: %s" % BooleanSearch.query(uinput),
    #     "ciiu: %s" % str(uciiu),
    #     "pobjeto: %s" % str(upobjeto),
    # ])

    url = 'http://127.0.0.1:4005/api/v2/reserva'
    data = {
        'id_reserva': 30,
        'division': 'venta de animales domesticos',
        'nombre': 'GATOS EL BUEN ARAÑAZO',
        'estado': 'activo'
    }
    data_json = json.dumps(data)
    response = requests.post(url, data=data_json)
    print("--------------------------------------------------------------")
    print(response.text)
    print("--------------------------------------------------------------")
    print(data_json)

    # url = 'http://127.0.0.1:9200/fundempresa2/empresa/00117460'

    # url = 'http://127.0.0.1:9200/fundempresa/reserva/_search?pretty=true&q=*:*'

    # url = 'http://127.0.0.1:9200/fundempresa/reserva/1'
    # response = requests.get(url)
    # print(response.text)

    # url = 'http://127.0.0.1:9200/fundempresa2/reserva'
    # data = {
    #     'id_reserva': 30,
    #     'division': 'venta de animales domesticos',
    #     'nombre': 'GATOS EL BUEN CARAÑAZO',
    #     'estado': 'activo'
    # }
    # data_json = json.dumps(data)
    # response = requests.post(url, data=data_json)
    # print(response.text)



    # xcode = json.dumps(json.loads(response.text), sort_keys=True, indent=4, ensure_ascii=False)
    # print(xcode)
    # print(highlight(xcode, JsonLexer(), Terminal256Formatter(style=DraculaStyle)))
