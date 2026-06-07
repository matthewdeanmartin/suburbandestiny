---
date: '2012-09-16'
recovered_from: wayback
slug: post-676
source_file: data\normalized\tech.wakayos.com\root\__query__\m\201209\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=676
title: Getting WCF to talk ordinary HTTP to a browser
---


This is an exercise in driving nails into the coffee table with your shoe. The goal isn’t really all that obviously beneficial and the tool isn’t the expected tool for the job. WCF wants to speak SOAP to SOAP aware clients. With the expansion to support a REST API with System.ServiceModel.Web, you can get a WCF service to talk to a browser. HOWEVER


\* The browser doesn’t serialize complex objects to a C\# like data type system on Request or Response. Instead you deal primarily in a raw Stream.  

\* Some browsers don’t speak XHTML (they will render it if you call it text/html, but MSIE will render xhtml/application as XML), so you can’t just return an X(HT)ML payload.  

\* WCF used this way is a “bring your own view engine” framework. I chose SharpDom for this exercise. It seems like it should be possible to support returning a SharpDom return value that serializes to XHTML with a type of text/html, but I don’t know how to do that.  

\* MVC already solves a lot of similar problems.


BUT with WCF you get some of those WCF features, like umm, well, when you have a browser client a lot of features aren’t avail (e.g. fancy transaction support, callbacks, etc), but you can still do fancy thinks like instancing, and supporting a HTML browser, JSON and WCF interface all on top of mostly the same code.


Just serving a page is fairly easy. Turn on web support in the config (same as any REST enabling, see end of post),  





```

[WebGet]
public Stream HomePage(){ 
            //Return a stream with HTML
            //... I have skipped the view engine, I used SharpDom
            MemoryStream stream = new MemoryStream();
            TextWriter writer = new StreamWriter(stream, Encoding.UTF8);
            new PageBuilder().Render(model, writer);
            writer.Flush();
            stream.Position = 0;
            return stream;
}

```

  

What will the URL look like? Well in devepment in Win 7, if you don’t have admin rights, it will be something like:


http://localhost:8732/Design\_Time\_Addresses/HelloWorld/web/HomePage


The http://localhost:8732/Design\_Time\_Addresses/ is the address that a non\-admin can register. It looks like you can’t register 8080\.


The /web/ part is because in my endpoints in config (below), the endpoint is “web”


Also notice you have to set an encoding (and I suppose you’ll want that to match what the HTML meta tag says)


`[WebInvoke(Method = "POST")]  

public Stream AnotherPostBack(Stream streamOfData)  

{  

 StreamReader reader = new StreamReader(streamOfData);  

 String res = reader.ReadToEnd();  

 NameValueCollection coll = HttpUtility.ParseQueryString(res);  

 //Return a stream of HTML  

}`  

To invoke the above, use an METHOD of POST and an action of 


http://localhost:8732/Design\_Time\_Addresses/HelloWorld/web/AnotherPostBack


And finally, use a web friendly host in your console app


`using (WebServiceHost host = new WebServiceHost(typeof(HelloService)))  

 {  

 host.Open();  

 Console.ReadLine();  

 }`


http://stackoverflow.com/questions/1850293/wcf\-rest\-where\-is\-the\-request\-data


Also, you can post back to this kind of operator… but for the life of me I can’t figure out how to get the Content. I can see the headers, I can see the content length, but I can’t get at the stream that holds the post’s content.


(This [StackOverflow Q \& A implies that to get the raw content,](http://stackoverflow.com/questions/1287802/access-request-body-in-a-wcf-restful-service) you have to use reflection to inspect private variables: )  

````
[OperationContract(Action = "POST", ReplyAction = "*")]
[WebInvoke(Method = "POST")]
public Stream PostBack(Message request)
{
}
````


Obviously, cookies and URL params are just a matter of inspecting the IncomingRequest.


And the config:  





```

<system.serviceModel>
    <services>
      <service name="WcfForHtml.HelloService" behaviorConfiguration="TestServiceBehavior">
        <host>
          <baseAddresses>
            <add baseAddress="http://localhost:8732/Design_Time_Addresses/HelloWorld"/>
          </baseAddresses>
        </host>
        <endpoint address="web"
                  binding="webHttpBinding"
                  contract="WcfForHtml.HelloService"
                  behaviorConfiguration="webBehavior">
        </endpoint>
      </service>
    </services>
      <behaviors>
        <!--SERVICE behavior-->
        <serviceBehaviors>
          <behavior name="TestServiceBehavior">
            <serviceMetadata httpGetEnabled="true" />
            <serviceDebug includeExceptionDetailInFaults="true"/>
          </behavior>
        </serviceBehaviors>
        <!--END POINT behavior-->
        <endpointBehaviors>
          <behavior name="webBehavior">
            <webHttp/>    
          </behavior>
        </endpointBehaviors>
      </behaviors>
  </system.serviceModel>

```