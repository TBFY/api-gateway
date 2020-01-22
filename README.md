<p align="center"><img width=50% src="https://github.com/TBFY/general/blob/master/figures/tbfy-logo.png"></p>
<p align="center"><img width=40% src="https://github.com/TBFY/api-gateway/blob/master/logo.png"></p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Docker](https://img.shields.io/badge/docker-v3+-blue.svg)
![Docker-Compose](https://img.shields.io/badge/docker_compose-v3.0+-blue.svg)
[![Release Status](https://jitci.com/gh/TBFY/api-gateway/svg)](https://jitci.com/gh/TBFY/api-gateway)
[![](https://jitpack.io/v/TBFY/api-gateway.svg)](https://jitpack.io/#TBFY/api-gateway)
[![GitHub Issues](https://img.shields.io/github/issues/TBFY/api-gateway.svg)](https://github.com/TBFY/api-gateway/issues)
[![License](https://img.shields.io/badge/license-Apache2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


## Basic Overview

Orchestration Microservice API Gateway. It provides a flexible abstraction layer and a single entry point that securely manages communication between TBFY clients and online tools via API.

## Quick Start

1. Install [Docker](https://docs.docker.com/install/) and [Docker-Compose](https://docs.docker.com/compose/install/)
1. Clone this repo

	```
	git clone https://github.com/TBFY/api-gateway.git
	```
1. Run the API-Gateway by:
    ```
    docker-compose up -d
	```
1. That's all! It should be listening at: [http://localhost:8000](http://localhost:8000)
    ```
    {
      message: "no route and no API found with those values"
    }
	```

## Current Services

Once the API-Gateway is up and running, all TBFY services are available from a single entry point:

industryCodesAPI, jurisdictionsAPI, placeholdersAPI, statementsAPI, filingsAPI, corporateGroupingsAPI, officersAPI

|               service                      |                                 as resource                                           |
|--------------------------------------------|------------------------------------------------------------------------------------|
|    companies info      	                   |    [/companies](https://tbfy.librairy.linkeddata.es/api/companies)      |
|    industry codes info      	                   |    [/companies](https://tbfy.librairy.linkeddata.es/api/industryCodes)      |
|    jurisdictions info      	                   |    [/companies](https://tbfy.librairy.linkeddata.es/api/jurisdictions)      |
|    placeholders info      	                   |    [/companies](https://tbfy.librairy.linkeddata.es/api/placeholders)      |
|    statements info      	                   |    [/companies](https://tbfy.librairy.linkeddata.es/api/statements)      |
|    filings info      	                   |    [/companies](https://tbfy.librairy.linkeddata.es/api/filings)      |
|    corporate groupings info      	                   |    [/companies](https://tbfy.librairy.linkeddata.es/api/corporateGroupings)      |
|    officers info      	                   |    [/companies](https://tbfy.librairy.linkeddata.es/api/officers)      |
|    OCDS info          	                   |    [/ocds](https://tbfy.librairy.linkeddata.es/api/ocds)      |
|    reconciliation: organization names      |    [/brands](https://tbfy.librairy.linkeddata.es/api/brands)      |
|    knowledge-graph: SparQL Queries         |    [/triples](https://tbfy.librairy.linkeddata.es/api/triples)      |
|    search-API: documents                   |    [/documents](https://tbfy.librairy.linkeddata.es/api/documents)      |
|    knowledge-graph-API: organizations      |    [/organisation](https://tbfy.librairy.linkeddata.es/api/organisation)      |
|    knowledge-graph-API: contracts          |    [/contract](https://tbfy.librairy.linkeddata.es/api/contract)      |
|    knowledge-graph-API: tenders            |    [/tender](https://tbfy.librairy.linkeddata.es/api/tender)      |
|    knowledge-graph-API: awards             |    [/award](https://tbfy.librairy.linkeddata.es/api/award)      |
|    knowledge-graph-API: contracting processes      |    [/contractingProcess](https://tbfy.librairy.linkeddata.es/api/contractingProcess)      |


## Contributing
Please take a look at our [contributing](https://github.com/TBFY/general/blob/master/guides/how-to-contribute.md) guidelines if you're interested in helping!
