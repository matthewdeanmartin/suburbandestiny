---
date: '2014-10-01'
recovered_from: wayback
slug: post-766
source_file: data\normalized\tech.wakayos.com\root\__query__\paged\2\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=766
title: C# Basics– Classes and basic behavior
---


What upfront work is necessary to create fully defined classes? By fully defined, I mean, there is enough features implemented so that it play well with the Visual Studio debugger, WCF/WebAPI, Javascript and XML, and so on. 


Ideally, this boilerplate would always be available to consume on your custom classes. In practices, it is uncommon to see any of the following implemented. Why is that?


So lets simplify reality and imagine that code is of only a few types:


(I’m suffixing all of these with \-like to remind you that I’m talking about things that look like these, not necessarily the class or data structure with the same name in the .NET or C\# spec or BCL)


* **Primative\-like**. Single value, appear in many domains, often formatted different in different countries. Sometimes simple, like Int32, sometimes crazy complicated like DateTime, sometimes missing, like “Money”.
* **Struct\-like**. Really small values, appear in some domains, like Latitude/Longitude pairs.
* **Datarow\-like**. Many properties,need to be persisted, probably stored in a relational or document database, often exchanged across machine, OS and organizational boundaries.
* **Service\-like**. These are classes that may or may not have state depending on the programming pradigm. They are classes with methods that do something, where as all the above classes, mainly just hold data and incidentally do something. It might be domain\-anemic, like create, read, update and delete or it might be domain\-driven, like issue insurance policy, or cancel vacation.
* **Collection\-like**. These used to be implemented as custom types, but with Generics, there isn’t as much motivation to implement these on a \*per type\* basis.
* **Tree or Graph\-like**. These are reference values that contain complex values and collection\-like values and those turn also might contain complex values and collections.


**All classes may need the following features**


* **Equality**\- By value, by reference and by domain specific. The out of the box behavior is usually good enough and for reference types shouldn’t be modified. Typically if you do need to modify equality, it is to get by\-value or by\-primary\-key behavior, which is best done in a separate class.
* **Ranking**\- A type of sorting. This may not be as valuable as it seems now that linq exists and supports .Sort(x\=\>…)
* **String representation**\- A way to represent this for usually human consumption, with features overlapping Serialization
* **Serialization**\- A usually two way means of converting the class into string, JSON, XML for persistence or communicating off machine
* **Factories, Cloning and Conversion**\- This covers creation (often made moot by IOC containers, which sometimes have requirements about what a class looks like), cloning, which is a mapping problem (made moot by things like automapper), and finally conversion, which is mapping similar types, such as Int to Decimal, or more like “Legacy Customer” to “Customer”
* **Validation**\- Asking an object what is wrong, usually for human consumption
* **Persistence**\- A way to save an object to a datastore. At the moment, this is nhibernate, EF, and maybe others.
* **Metadata**\- For example, the .NET Type class, an XSD for the serialized format, and so on.
* **Versioning**\- Many of the above features are affected by version, such as seralization and type conversion, where one may want to convert between types that are the same but separated by time where properties may have been added or removed. Round trip conversion without data loss is a type of a versioning feature.


**How implemented**


* **Ad hoc**. Just make stuff up. Software should be hard, unpredictable and unmanageable. The real problem is too many people don’t want to read the non\-existent documentation of your one\-off API.
* **Framework driven**. Make best efforts to find existing patterns and copy them. This improves your ability to communicate how your API works to your future self and maybe to other developers.
* **Interface driven**. A bit old fashioned, but rampant. For example these:  

 `//Forms of ToString(), may need additional for WebAPI  

 IFormattable, IFormatProvider, ICustomFormatter,  

 //Sort of an alternate constructor/factory pattern  

 ICloneable,  

 IDisposable, //End of life clean up  

 IComparable, IComparable, //Sorting  

 //Competing ways to validate an object  

 IValidatableObject, IDataErrorInfo,  

 //Binary (de)serialization  

 ISerializable, IObjectReference`
* **Attribute driven**. This is now popular for seralization APIS, e.g. DataContract/DataMember and for certain Validations.
* **Base Class**\- A universal class that all other classes derive from and implement some of the above concerns. In practice, this isn’t very practical, as most of these code snippets vary with the number of properties you have.
* **In\-Class**\- For example, just implement IFormat\* on your class. If you need to support 2 or more ways of implementing an interface, you might be better off implementing several classes that depending on the class you are creating features for.
* **Universal Utility Class**\- You can only pick one base class in C\#. If you waste it on a utility class, you might preclude creating a more useful design heirarchy. A universal utility class has the same problem as a universal base class.
* **Code generation**. Generate source code using reflection.
* **Reflection**. Provide certain features by reflecting over the fields and properties.


**Gotchas.**  

All of these patterns entail gotchas. Someday when I’m smarter and have lots of free time, I’ll write about it.