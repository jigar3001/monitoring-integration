

Monitoring-Integration
=======================

Usage Details
--------------

1. Install Grafana. 
   Follow the steps provided in below mentioned doc to install grafana.

    http://docs.grafana.org/installation/rpm/

**Note :**

  All the commands mentioned below are run as a regular user that has ``sudo``
  privileges.


* **Installing Monitoring-Integration**

    ::
    
        $ yum install tendrl-monitoring-integration
	
   **Note**
        Make sure tendrl repositories are enabled.
	https://github.com/Tendrl/documentation/wiki/Tendrl-Package-Installation-Reference


* **Restart server to load new configurations**

  * Start grafana server
  
    ::

        $ service grafana-server start  
  
  * Restart httpd

    ::

        $ service httpd restart  
* **Configuring Monitoring-Integration**

  * Provide host ip-address of datasource to be created in grafana under "datasource_host" in
    /etc/tendrl/monitoring-integration/monitoring-integration.conf.yaml file
    
    NOTE: Do not provide localost or 127.0.0.1.


* **Running Monitoring-Integration**


  * Run monitoring-integration

    ::

        $ tendrl-monitoring-integration
