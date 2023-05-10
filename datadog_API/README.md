# Datadog API Script and Apache Install

This is a Python script that extracts the names of all monitors existing for a Datadog account via Datadog API and exports them as a CSV file.


## Datadog API Script(datadog-api.sh)
It is an improved version of basic scripts for Datadog provided by official documentation:
https://docs.datadoghq.com/api/latest/monitors/

## Requirements

Python 3.6 or later
datadog_api_client module
pandas module
### Installation

1. Install the required modules:
```
pip install datadog_api_client pandas
```
2. Clone or download the script from this repository.

## Usage

Please use the API and APP keys from existed Datadog account 
```
DD_SITE="datadoghq.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "datadog_v2.py"
```
The script will generate a file named monitor_names.csv in the same directory with the list of monitor names.
