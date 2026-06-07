---
date: '2009-08-06'
recovered_from: wayback
slug: post-576
source_file: data\normalized\tech.wakayos.com\root\__query__\p\576\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=576
title: You think you’re doing tier architecture or business objects, but its just
  super pipelines and ziggurats.
---


**Superpiplining. Methods that call methods that call methods do not magically add value along the way.**


If one tier is bad, two tiers is better, why not n tiers (or layers), I mean, literally an infinite number of tiers, each adding zero value along the way. I call this patter “Super Pipelining” Super pipelining makes dependency tracing a pain. A typial super\-pipelined application will still put all authorization, validation, calculations in the UI and pass System.Data or SqlClient objects back and forth the super pipeline.


 `class Customer() {  

 public void AddCustomer(Dto customer){ (new CustomerBusinessObject()).AddCustomer(); }  

}`


class CustomerBusinessObject() {  

 public void AddCustomer(Dto customer){ (new CustomerBusinessLogicObject()).AddCustomer(); }  

}


class CustomerBusinessLogicObject() {  

 public void AddCustomer(Dto customer){ (new CustomerBusinessLogicDomainObject()).AddCustomer(); }  

}


class CustomerBusinessLogicDomainObject() {  

 public void AddCustomer(Dto customer){ (new CustomerBusinessLogicDomainScenarioDatabasePersistenceObject()).AddCustomer(); }  

}


class CustomerBusinessLogicDomainScenarioDatabasePersistenceObject() {  

 public void AddCustomer(Dto customer){ (new CustomerBusinessObject()).AddCustomer(); }  

}  




**Ziggurat.**  A class that inherits from a class that inherits from a class that inherits from a class where the middle classes and the base don’t do anything. The classes in the middle do not magically make your code better.


 `class BusinessObject: BaseObject {}  

class BaseObject: BasementObject{}  

class BasementObject: UndergroundObject{}  

class UndergroundObject: UbberBasementObject{}  

class UbberBasementObject: SuperDuperBasementObject{}  

class SuperDuperBasementObject: AceOfBaseObject{}  

class AceOfBaseObject: China{}`