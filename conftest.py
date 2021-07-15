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

@pytest.fixture()
def tc_param():
    common_var = {}
    common_var["uuid"] = ssid
    common_var["user"] = user
    common_var["start_time"] = int(time.time())
    common_var["cur_time"] = cur_time

    return common_var

@pytest.fixture()
def srv_hdl():
    hdl = general_lib.login_to_host("172.20.1.23","cbuser","c@ncunSys100")
    return hdl


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
