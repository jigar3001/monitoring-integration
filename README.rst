

Monitoring-Integration
=======================

Usage Details
--------------

#. Grafana Installation. 
   Follow the steps provided in below mentioned doc to install grafana.

    http://docs.grafana.org/installation/rpm/

** Note :**

All the commands mentioned below are run as a regular user that has ``sudo``
privileges.
  
* **Installing Monitoring-Integration**

  ::
    
       $ yum install tendrl-monitoring-integration
	
       **Note**
   
          Make sure tendrl repositories are enabled.
          https://github.com/Tendrl/documentation/wiki/Tendrl-Package-Installation-Reference
    
  Configuration file monitoring-integration.conf.yaml needed by monitoring-integration
  is present under
 
  ' /etc/tendrl/monitoring-integration/'

  Default dashboards that are to be created in grafana are present under

  ' /etc/tendrl/monitoring-integration/grafana/dashboards/ '


* **Start/Restart server to load new configurations**

  1 Start grafana server
  
    ::

        $ service grafana-server start  
  
  2 Restart httpd

    ::

        $ service httpd restart  


* **Running Monitoring-Integration**

  1  Provide host ip-address of datasource to be created in grafana under "datasource_host" in
     monitoring-integration.conf.yaml file.
     [ Do not provide localhost or 127.0.0.1 ]

  2  Run monitoring-integration

     ::

         $ tendrl-monitoring-integration
