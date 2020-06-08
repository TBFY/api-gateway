# Step one for every Python app that talks over the web
#pip install requests

import requests
import json

endpoint = "localhost:8001"

# OpenOpps APIs

ocdsAPI = {
    "name":"ocds-api",
    "uris":"/ocds",
    "methods":"GET,POST,PUT,DELETE",
    "upstream_url":"https://openopps.com/api/tbfy/ocds",
    "strip_uri":True,
    "preserve_host":False,
    "retries":5,
    "upstream_connect_timeout":60000,
    "upstream_send_timeout":60000,
    "upstream_read_timeout":60000,
    "https_only":False,
    "http_if_terminated":True
}

# OpenCorporates APIs

companiesAPI = {
    "name":"companies-api",
    "uris":"/companies",
    "methods":"GET,POST,PUT,DELETE",
    "upstream_url":"https://api.opencorporates.com/v0.4/companies",
    "strip_uri":True,
    "preserve_host":False,
    "retries":5,
    "upstream_connect_timeout":60000,
    "upstream_send_timeout":60000,
    "upstream_read_timeout":60000,
    "https_only":False,
    "http_if_terminated":True
}

officersAPI = {
    "name":"officers-api",
    "uris":"/officers",
    "methods":"GET,POST,PUT,DELETE",
    "upstream_url":"https://api.opencorporates.com/v0.4/officers",
    "strip_uri":True,
    "preserve_host":False,
    "retries":5,
    "upstream_connect_timeout":60000,
    "upstream_send_timeout":60000,
    "upstream_read_timeout":60000,
    "https_only":False,
    "http_if_terminated":True
}

corporateGroupingsAPI = {
    "name":"corporateGroupings-api",
    "uris":"/corporateGroupings",
    "methods":"GET,POST,PUT,DELETE",
    "upstream_url":"https://api.opencorporates.com/v0.4/corporate_groupings",
    "strip_uri":True,
    "preserve_host":False,
    "retries":5,
    "upstream_connect_timeout":60000,
    "upstream_send_timeout":60000,
    "upstream_read_timeout":60000,
    "https_only":False,
    "http_if_terminated":True
}

filingsAPI = {
    "name":"filings-api",
    "uris":"/filings",
    "methods":"GET,POST,PUT,DELETE",
    "upstream_url":"https://api.opencorporates.com/v0.4/filings",
    "strip_uri":True,
    "preserve_host":False,
    "retries":5,
    "upstream_connect_timeout":60000,
    "upstream_send_timeout":60000,
    "upstream_read_timeout":60000,
    "https_only":False,
    "http_if_terminated":True
}

statementsAPI = {
    "name":"statements-api",
    "uris":"/statements",
    "methods":"GET,POST,PUT,DELETE",
    "upstream_url":"https://api.opencorporates.com/v0.4/statements",
    "strip_uri":True,
    "preserve_host":False,
    "retries":5,
    "upstream_connect_timeout":60000,
    "upstream_send_timeout":60000,
    "upstream_read_timeout":60000,
    "https_only":False,
    "http_if_terminated":True
}

placeholdersAPI = {
    "name":"placeholders-api",
    "uris":"/placeholders",
    "methods":"GET,POST,PUT,DELETE",
    "upstream_url":"https://api.opencorporates.com/v0.4/placeholders",
    "strip_uri":True,
    "preserve_host":False,
    "retries":5,
    "upstream_connect_timeout":60000,
    "upstream_send_timeout":60000,
    "upstream_read_timeout":60000,
    "https_only":False,
    "http_if_terminated":True
}

jurisdictionsAPI = {
    "name":"jurisdictions-api",
    "uris":"/jurisdictions",
    "methods":"GET,POST,PUT,DELETE",
    "upstream_url":"https://api.opencorporates.com/v0.4/jurisdictions",
    "strip_uri":True,
    "preserve_host":False,
    "retries":5,
    "upstream_connect_timeout":60000,
    "upstream_send_timeout":60000,
    "upstream_read_timeout":60000,
    "https_only":False,
    "http_if_terminated":True
}

industryCodesAPI = {
    "name":"industryCodes-api",
    "uris":"/industryCodes",
    "methods":"GET,POST,PUT,DELETE",
    "upstream_url":"https://api.opencorporates.com/v0.4/industry_codes",
    "strip_uri":True,
    "preserve_host":False,
    "retries":5,
    "upstream_connect_timeout":60000,
    "upstream_send_timeout":60000,
    "upstream_read_timeout":60000,
    "https_only":False,
    "http_if_terminated":True
}

reconciliationAPI = {
    "name":"reconciliation-api",
    "uris":"/brands",
    "methods":"GET,POST,PUT,DELETE",
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

# Documents API

searchAPI = {
    "name":"search-documents",
    "uris":"/documents",
    "methods":"GET,POST,PUT,DELETE",
    "upstream_url":"http://search-api:7777/search-api/documents",
    "strip_uri":True,
    "preserve_host":False,
    "retries":5,
    "upstream_connect_timeout":60000,
    "upstream_send_timeout":60000,
    "upstream_read_timeout":60000,
    "https_only":False,
    "http_if_terminated":True
}

# Knowledge-Graph APIs

sparQLEndpoint = {
    "name":"sparql-endpoint",
    "uris":"/triples",
    "methods":"GET,POST,PUT,DELETE",
    "upstream_url":"http://fuseki:3030/tbfy/query",
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
    "uris":"/organisation",
    "methods":"GET,POST,PUT,DELETE",
    "upstream_url":"http://kg-api:7777/kg-api/organisation",
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
    "uris":"/contract",
    "methods":"GET,POST,PUT,DELETE",
    "upstream_url":"http://kg-api:7777/kg-api/contract",
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
    "uris":"/award",
    "methods":"GET,POST,PUT,DELETE",
    "upstream_url":"http://kg-api:7777/kg-api/award",
    "strip_uri":True,
    "preserve_host":False,
    "retries":5,
    "upstream_connect_timeout":60000,
    "upstream_send_timeout":60000,
    "upstream_read_timeout":60000,
    "https_only":False,
    "http_if_terminated":True
}

kgAPI_supplier = {
    "name":"kg-supplier",
    "uris":"/supplier",
    "methods":"GET,POST,PUT,DELETE",
    "upstream_url":"http://kg-api:7777/kg-api/supplier",
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
    "uris":"/tender",
    "methods":"GET,POST,PUT,DELETE",
    "upstream_url":"http://kg-api:7777/kg-api/tender",
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
    "uris":"/contractingProcess",
    "methods":"GET,POST,PUT,DELETE",
    "upstream_url":"http://kg-api:7777/kg-api/contractingProcess",
    "strip_uri":True,
    "preserve_host":False,
    "retries":5,
    "upstream_connect_timeout":60000,
    "upstream_send_timeout":60000,
    "upstream_read_timeout":60000,
    "https_only":False,
    "http_if_terminated":True
}




configs = [searchAPI, kgAPI_organisation,  kgAPI_award, kgAPI_supplier, kgAPI_contract, kgAPI_contractingProcesses, kgAPI_tender, reconciliationAPI, sparQLEndpoint, companiesAPI, ocdsAPI, industryCodesAPI, jurisdictionsAPI, placeholdersAPI, statementsAPI, filingsAPI, corporateGroupingsAPI, officersAPI]


for config in configs:
    resp = requests.post('http://'+endpoint+'/apis', json=config)
    if resp.status_code == 409:
        print('{} already exists'.format(config["name"]))
    elif resp.status_code == 201:
        print('Added {} endpoint as route-service: {}'.format(config["name"],resp.json()["id"]))
    else:
        raise Exception('error','Error adding {} by POST /apis/ {}'.format(config["name"], resp.status_code))
