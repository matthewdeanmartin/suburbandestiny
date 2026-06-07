---
date: '2009-07-26'
recovered_from: wayback
slug: post-568
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200907\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=568
title: Troubleshooting “Service ‘Astoria’ implements multiple ServiceContract types,
  and no endpoints are defined in the configuration file.”
---


This is a misleading error that means you forgot to put the connection string into web.config.


So if you get:



> `WebHost failed to process a request.  
> 
>  Sender Information: System.ServiceModel.Activation.HostedHttpRequestAsyncResult/63432468  
> 
>  Exception: System.ServiceModel.ServiceActivationException: The service '/Services/Astoria.svc' cannot be activated due to an exception during compilation. The exception message is: Service 'Astoria' implements multiple ServiceContract types, and no endpoints are defined in the configuration file. WebServiceHost can set up default endpoints, but only if the service implements only a single ServiceContract. Either change the service to only implement a single ServiceContract, or else define endpoints for the service explicitly in the configuration file.. ---> System.InvalidOperationException: Service 'Astoria' implements multiple ServiceContract types, and no endpoints are defined in the configuration file. WebServiceHost can set up default endpoints, but only if the service implements only a single ServiceContract. Either change the service to only implement a single ServiceContract, or else define endpoints for the service explicitly in the configuration file.  
> 
>  at System.ServiceModel.Web.WebServiceHost.AddAutomaticWebHttpBindingEndpoints(ServiceHost host, IDictionary`2 implementedContracts, String multipleContractsErrorMessage)  
> 
>  at System.ServiceModel.Web.WebServiceHost.OnOpening()  
> 
>  at System.ServiceModel.Channels.CommunicationObject.Open(TimeSpan timeout)  
> 
>  at System.ServiceModel.ServiceHostingEnvironment.HostingManager.ActivateService(String normalizedVirtualPath)  
> 
>  at System.ServiceModel.ServiceHostingEnvironment.HostingManager.EnsureServiceAvailable(String normalizedVirtualPath)  
> 
>  --- End of inner exception stack trace ---  
> 
>  at System.ServiceModel.AsyncResult.End[TAsyncResult](IAsyncResult result)  
> 
>  at System.ServiceModel.Activation.HostedHttpRequestAsyncResult.End(IAsyncResult result)  
> 
>  Process Name: WebDev.WebServer  
> 
>  Process ID: 8168`


This is what a connection string for an entity data model looks like. If you created your edmx file in a different project from your .svc file, you will need to manually copy the connection string. In this case I’m using Sqlite (which can’t be design using Visual Studio Express, in case you were wondering)


 `<connectionStrings>  

 <add name="calendarEm" connectionString="metadata=res://*/CalendarV1.csdl|res://*/CalendarV1.ssdl|res://*/CalendarV1.msl;provider=System.Data.SQLite;provider connection string="data source=C:\code\CommunityCalendar\Calendar\App_Data\calendar.db3;useutf16encoding=True"" providerName="System.Data.EntityClient" />  

 </connectionStrings>`