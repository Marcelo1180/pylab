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
                                  "nombre.fonetico",
                                #   "nombre.numero"
                               ],
                            #    "query":"(((universidad~) OR (universidad~)) AND ((10) OR (diez) OR (x))) OR (((universidad~)))",
                            #    "query":"(((universidad100~)))",
                            #    "query":"(((universidad) OR (universidad~)) AND ((siglo) OR (siglo~)) AND ((10) OR (diez) OR (x)))",
                                # OR (((universidadsiglo)) AND ((10) OR (diez) OR (x))) OR (((universidad) OR (universidad~)) AND ((siglox)))\
                            #    "query":"(((universidadsiglo10)))",
                            #    "query":"(((universidadsiglox)))",
                               "query":"nombre.numero:universidadsiglox",
                               "boost":3
                            }
                         },
                        #  {
                        #     "match":{
                        #        "estado":"MA"
                        #     }
                        #  }
                      ],
                    #   "filter":[
                    #      {
                    #         "terms":{
                    #            "ciiu":[]
                    #         }
                    #      }
                    #   ]
                   }
                },
                # {
                #    "bool":{
                #       "must":[
                #         {
                #             "query_string":{
                #                "fields":[
                #                   "nombre",
                #                   "nombre.fonetico"
                #                ],
                #                "query":"",
                #                "boost":2
                #             }
                #         },{
                #             "query_string":{
                #                "fields":[
                #                   "objeto_principal",
                #                   "objeto_principal.sinonimo"
                #                ],
                #                "query":"",
                #                "boost":1
                #             }
                #         },
                #          {
                #             "match":{
                #                "estado":"MA"
                #             }
                #          }
                #       ]
                #    }
                # }
             ],
             "minimum_should_match":1
          }
       }
    }

    @staticmethod
    def search(uinput="", uciiu=[], upobjeto=""):
        bsearch = BooleanSearch.query(uinput)
        # Buscar._data["query"]["bool"]["should"][0]["bool"]["must"][0]["query_string"]["query"] = bsearch
        # Buscar._data["query"]["bool"]["should"][0]["bool"]["filter"][0]["terms"]["ciiu"] = uciiu
        # Buscar._data["query"]["bool"]["should"][1]["bool"]["must"][0]["query_string"]["query"] = bsearch
        # Buscar._data["query"]["bool"]["should"][1]["bool"]["must"][1]["query_string"]["query"] = upobjeto
        data_json = json.dumps(Buscar._data)
        response = requests.get(Buscar._url, data=data_json)
        return json.dumps(response.json())
