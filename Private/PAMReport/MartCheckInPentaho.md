## Mart Check In Pentaho
There are 19 Marts in impala database, we should check them each time when they are updated.
And we plan to create automated test cases for regression test.
* All columns should be include in the report
  * There are too many columns in some marts, so we seperate them into several reports in one folder
* Trigger such reports and if the marts are ok, the reports should be generated successfully.
* Using SoapUI to request API Service by Pentaho BA Server.
### Sample Steps
1. Create Reports which include all of the columns for each mart
2. Prepare properteis files include the report information
3. Create config file for initing the SoapUI project, include property file information, related test steps...
4. Get Authorization.
5. Delete genereated reports last time.
6. Scheduler all the report.
7. Check the expected reports are generated successfully or not