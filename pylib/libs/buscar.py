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
        	   "must":[
        	      {
        	         "query_string":{
        	            "fields":[
        	               "nombre",
        	               "nombre.fonetico"
        	            ],
        	            "query": ""
        	         }

        	      },
        	      {
        	         "match":{
        	            "estado": "MA"
        	         }
        	      }
        	   ],
        	   "must_not":[
        	      {
        	         "match":{
        	            "nombre": ""
        	         }
        	      }
        	   ],
               "filter":[
        	      {
        	         "term":{
        	            "ciiu": "1013"
        	         }
        	      }
        	   ],
        	   "should":[
        	      {
        	         "match":{
        	            "nombre": ""
        	         }
        	      }
        	   ]
        	}
        }
    }

    @staticmethod
    def search(uinput=""):
        bsearch = BooleanSearch.query(uinput)
        Buscar._data["query"]["bool"]["must"][0]["query_string"]["query"] = bsearch
        data_json = json.dumps(Buscar._data)
        # return requests.get(Buscar._url, data=data_json)
        response = requests.get(Buscar._url, data=data_json)
        return response
