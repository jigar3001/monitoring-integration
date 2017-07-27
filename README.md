

Monitoring-Integration
=======================


Functionalities
----------------

- Create a new dashboard in Grafana

Usage Details
--------------

#### Development setup ####


  * Install grafana : http://docs.grafana.org/installation/

  * Provide grafana host-addr and port in the grafana.conf.yml file.

  * Create a json file in grafana/dashboards and provide the json for the dashboard
     that is to be created.

  * Provide the file-name of the json file in the grafana.conf.yml under dashboards.

  * Make one of the dashboards listed under dashboards as home_dashboard. 

  * Create a graphite.conf.yml using the format provided in grapite.conf.sample.yml
     file and provide details of graphite's instance in the conf file.

  * Run __init__.py file. `$ python __init__.py `


