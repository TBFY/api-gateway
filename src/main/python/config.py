# Step one for every Python app that talks over the web
#pip install requests

import requests
import json

endpoint = "localhost:8001"

reconciliationAPI = {
    "name":"reconciliation-api",
    "uris":"/brands",
    "methods":"GET",
    "upstream_url":"https://opencorporates.com/reconcile",
    "strip_uri":True,
    "preserve_host":False,
    "retries":5,
    "upstream_connect_timeout":60000,
    "upstream_send_timeout":60000,
    "upstream_read_timeout":60000,
    "https_only":False,
    "http_if_terminated":True
}

sparQLEndpoint = {
    "name":"sparql-endpoint",
    "uris":"/sparql",
    "methods":"GET",
    "upstream_url":"http://data.tbfy.eu/repositories/TBFY",
    "strip_uri":True,
    "preserve_host":False,
    "retries":5,
    "upstream_connect_timeout":60000,
    "upstream_send_timeout":60000,
    "upstream_read_timeout":60000,
    "https_only":False,
    "http_if_terminated":True
}

searchAPI = {
    "name":"search-documents",
    "uris":"/documents",
    "methods":"GET",
    "upstream_url":"http://tbfy.librairy.linkeddata.es/search-api/documents",
    "strip_uri":True,
    "preserve_host":False,
    "retries":5,
    "upstream_connect_timeout":60000,
    "upstream_send_timeout":60000,
    "upstream_read_timeout":60000,
    "https_only":False,
    "http_if_terminated":True
}

kgAPI_organisation = {
    "name":"kg-organizations",
    "uris":"/organizations",
    "methods":"GET",
    "upstream_url":"http://tbfy.librairy.linkeddata.es/kg-api/organisation",
    "strip_uri":True,
    "preserve_host":False,
    "retries":5,
    "upstream_connect_timeout":60000,
    "upstream_send_timeout":60000,
    "upstream_read_timeout":60000,
    "https_only":False,
    "http_if_terminated":True
}

kgAPI_company = {
    "name":"kg-companies",
    "uris":"/companies",
    "methods":"GET",
    "upstream_url":"http://tbfy.librairy.linkeddata.es/kg-api/company",
    "strip_uri":True,
    "preserve_host":False,
    "retries":5,
    "upstream_connect_timeout":60000,
    "upstream_send_timeout":60000,
    "upstream_read_timeout":60000,
    "https_only":False,
    "http_if_terminated":True
}

kgAPI_contract = {
    "name":"kg-contract",
    "uris":"/contracts",
    "methods":"GET",
    "upstream_url":"http://tbfy.librairy.linkeddata.es/kg-api/contract",
    "strip_uri":True,
    "preserve_host":False,
    "retries":5,
    "upstream_connect_timeout":60000,
    "upstream_send_timeout":60000,
    "upstream_read_timeout":60000,
    "https_only":False,
    "http_if_terminated":True
}

kgAPI_award = {
    "name":"kg-award",
    "uris":"/awards",
    "methods":"GET",
    "upstream_url":"http://tbfy.librairy.linkeddata.es/kg-api/award",
    "strip_uri":True,
    "preserve_host":False,
    "retries":5,
    "upstream_connect_timeout":60000,
    "upstream_send_timeout":60000,
    "upstream_read_timeout":60000,
    "https_only":False,
    "http_if_terminated":True
}

kgAPI_tender = {
    "name":"kg-tender",
    "uris":"/tenders",
    "methods":"GET",
    "upstream_url":"http://tbfy.librairy.linkeddata.es/kg-api/tender",
    "strip_uri":True,
    "preserve_host":False,
    "retries":5,
    "upstream_connect_timeout":60000,
    "upstream_send_timeout":60000,
    "upstream_read_timeout":60000,
    "https_only":False,
    "http_if_terminated":True
}

kgAPI_contractingProcesses = {
    "name":"kg-contractingProcesses",
    "uris":"/contractingProcesses",
    "methods":"GET",
    "upstream_url":"http://tbfy.librairy.linkeddata.es/kg-api/contractingProcess",
    "strip_uri":True,
    "preserve_host":False,
    "retries":5,
    "upstream_connect_timeout":60000,
    "upstream_send_timeout":60000,
    "upstream_read_timeout":60000,
    "https_only":False,
    "http_if_terminated":True
}




configs = [searchAPI, kgAPI_organisation, kgAPI_company,  kgAPI_award, kgAPI_contract, kgAPI_contractingProcesses, kgAPI_tender, reconciliationAPI, sparQLEndpoint]


for config in configs:
    resp = requests.post('http://'+endpoint+'/apis', json=config)
    if resp.status_code == 409:
        print('{} already exists'.format(config["name"]))
    elif resp.status_code == 201:
        print('Added {} endpoint as route-service: {}'.format(config["name"],resp.json()["id"]))
    else:
        raise Exception('error','Error adding {} by POST /apis/ {}'.format(config["name"], resp.status_code))