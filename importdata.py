import csv
import json

from elasticsearch import Elasticsearch

es = Elasticsearch(['http://localhost:9200/'])
csv.register_dialect('iislog', delimiter=' ')

with open('/Users/sgourley/Projects/elastic-stack/u_ex180326.log') as log_csv:
    reader = csv.DictReader(log_csv, dialect='iislog')
    i = 0
    for line in reader:
        j = json.dumps(line)
        es.index(index='iis-log-index', doc_type='iislog', id=i, body=j)
        i = i + 1
        print(i)
