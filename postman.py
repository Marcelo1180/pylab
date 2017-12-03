 #!/usr/bin/python
 # -*- coding: utf-8 -*-
import sys
import json
import requests
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import Terminal256Formatter
from dracula import DraculaStyle


# url = 'http://127.0.0.1:9200/fundempresa2/empresa/_search'
url = 'http://127.0.0.1:9200/test/test/_search'
data = {
    "query":{
    	"bool":{
    	   "must":[
    	      {
    	         "query_string":{
    	            "fields":[
    	               "nombre",
    	               "nombre.sinonimo"
    	            ],
    	            "query": "hotel"
    	         }

    	      },
    	    #   {
    	    #      "match":{
    	    #         "estado":"MA"
    	    #      }
    	    #   }
    	   ],
    	   "must_not":[
    	      {
    	         "match":{
    	            "nombre":""
    	         }
    	      }
    	   ],
    	   "should":[
    	      {
    	         "match":{
    	            "nombre": "itati"
    	         }
    	      }
    	   ]
    	}
    }
}
if __name__ == "__main__":
    uinput = " ".join(sys.argv[1:])
    data["query"]["bool"]["must"][0]["query_string"]["query"] = uinput
    # print(data["query"]["bool"]["must"][0]["query_string"]["query"])
    data_json = json.dumps(data)
    response = requests.get(url, data=data_json)

    xheader = "HTTP/1.1 %s\n%s"%(response.status_code, response.headers['content-type'])
    # code=json.loads(response.text)
    xcode=json.dumps(response.json(), sort_keys=True, indent=4, ensure_ascii=False, encoding="utf-8")
    print(highlight(xheader+"\n\n"+xcode, JsonLexer(), Terminal256Formatter(style=DraculaStyle)))
