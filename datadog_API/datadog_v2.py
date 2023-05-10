import csv
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.list_monitors()

    # make new list by selecting values from 'name'
    monitor_names = [monitor['name'] for monitor in response]

    # Writing monitors to CSV files
    with open('monitor_names.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name'])
        writer.writerows([[name] for name in monitor_names])
