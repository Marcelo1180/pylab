 #!/usr/bin/python
 # -*- coding: utf-8 -*-
import sys
import json
import requests
from libs.consulta import BooleanSearch

class Buscar:
    _url = 'http://127.0.0.1:9200/test/test/_search'
    _data = {
       "query":{
          "bool":{
             "should":[
                {
                   "bool":{
                      "must":[
                         {
                            "query_string":{
                               "fields":[
                                  "nombre",
                                  "nombre.fonetico"
                               ],
                               "query":"(((antie~)) AND ((metic~))) OR (((antiemetic~)))",
                               "boost":3
                            }
                         }
                      ],
                      "filter":[
                         {
                            "terms":{
                               "ciiu":["0124"]
                            }
                         }
                      ]
                   }
                },
                {
                   "bool":{
                      "must":[
                         {
                            "query_string":{
                               "fields":[
                                  "nombre",
                                  "nombre.fonetico"
                               ],
                               "query":"antiemetic",
                               "boost":2
                            }
                         }
                      ]
                   }
                }
             ],
             "minimum_should_match":1
          }
       }
    }

    @staticmethod
    def search(uinput="", uciiu=[], upobjeto=""):
        bsearch = BooleanSearch.query(uinput)
        # Buscar._data["query"]["bool"]["must"][0]["query_string"]["query"] = bsearch
        # Buscar._data["query"]["bool"]["filter"][0]["terms"]["ciiu"] = uciiu
        # Buscar._data["query"]["bool"]["must"][1]["query_string"]["query"] = upobjeto
        data_json = json.dumps(Buscar._data)
        response = requests.get(Buscar._url, data=data_json)
        return json.dumps(response.json())
