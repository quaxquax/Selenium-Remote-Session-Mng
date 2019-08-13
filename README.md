# SeleniumRemote-
An Instance Manager for Remote Selenium Sessions

Consider the followinng use case: 

You may have to test a globally availabe Web App, with complex session management. If you tear down and reestablish a new Selenium instance you will love the web apps user context, which may lead to unrealistic use cases. 

By working with a remote Selenium session that you can dis-connect from the browser after running a test and make it avilable for another test instance. 

Depending on geo-location or user profile the web app may present differently, which means you may want to have several different Selenium instances available, configured with different proxies for instance.

This project is at its infancy. At this point it only contains a example Python script that illustreates how to create a Selenium session for remote connections and an associated start-up shell script.
