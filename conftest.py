import pytest
import time
import logging
import uuid
import getpass
ssid = uuid.uuid4().hex
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

@pytest.fixture()
def username(request):
    return getpass.getuser() #gets the running username 

@pytest.fixture()
def uuid_value():
    return  ssid#returns a random id

@pytest.fixture(scope="session")
def run_result():
    pass
    yield
    time.sleep(10)
    res= es.search(index='test_*',body={'query':{'match':{'uuid':"{0}".format(ssid)}}},size=1000)
    result = {}
    passed = []
    failed = []
    for hit in res['hits']['hits']:
        result[hit['_source']['testname']] = hit['_source']['result']
    for k,v in result.items():
        if v.lower() == "failed":
            failed.append(k)
        else:
            passed.append(k)
