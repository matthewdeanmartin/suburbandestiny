---
date: '2010-07-22'
recovered_from: wayback
slug: post-601
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\201007\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=601
title: Using unit testing principles to write better integration tests
---


My application is a database application. There is some logic that is easy to move into an application server where it is easy to do dependency inversion and unit testing.  That leaves untested all that code in the database, the stored procedures, triggers, tables and so on.


**Compilation Tests.** Sql Server allows for SET NOEXEC ON, which compiles and checks many things for a batch of SQL commands, but doesn’t execute of it.  I have integration tests that run almost all my data layer code with NOEXEC ON and it reveals malformed parameter lists and other issues that would normally only show at runtime.  The tests run very fast, do not change the state of the system, and they don’t interfere with each other.  There isn’t anything to assert except that no exception was thrown.


**Indempotent Tests.** If your code has working transactions, then you create a root object (store), the child object (books in stock), etc as if the database was empty.  Then when you have enough objects to record a book sale, record the sale.  Assert something useful like numbers of rows affected, size of primary key etc.  Then roll it all back.


These tests can run fast, but might not depending on the particulars of the transaction.  For example, a stored procedure to calculate the payroll might be slow if the database has a 100,000 employees.  A good idempotent test will skip over any of these slow tests


Idempotent tests leave the database unchanged as long as your transaction code isn’t buggy.


**Additive Integration Tests.** Additive tests look a lot like the idempotent tests, except they don’t roll back.  Read world database code fails on account of how the data looks just as often as it fails for how the code works.  Not all code failures should be fixed by writing more code.  If common sense is violated by a column containing nulls 1% of the time, then it isn’t possible to write code to do something other than fail when that column is null.  But we can’t discover that our code and our data aren’t in harmony unless we run this test.


A good additive test is mostly inserts and driven by existing, real or highly realistic data.  An example would be taking the entire inventory of books and re\-adding them with slightly different names.  If a row that exists now can’t be inserted with existing code, then one of them is wrong.


Additive tests leave the database modified, but because the transactions are mostly inserts, tests aren’t likely to be competing for the same rows and tables.  If performance characteristics warrant it, consider running it in a transaction and rolling back.  Better databases can rollback large numbers of transactions rapidly, worse database will take huge amounts of time to rollback or hang the server.


**Destructive Integration Tests.** Destructive tests operate on the existing data in a way to make it unsuable for other tests.  Destructive tests primarily do deletes and updates.  For example, if we imagine a test that looped through all books in inventory and recorded a sale, we might be able to discover some books fail to be sold when run through the sales code.  Either we have a code problem or a data problem and that is something we’d like to know.


At the end of the test, the database may be logically correct given the transactions you’ve run, but all the books have been sold, all the employees have been fired, all the book descriptions overwritten with lorem ipsum.  Like additive tests, these can be rolled back if your database can do so without performance problems.  Otherwise,  you will want to let these transactions commit and then restore the database from a backup.


Destructive tests are the least like unit tests and the most like the integration tests your unit test text book warned you about.


All of these proposed tests are, except the destructive ones, in my opinion, safe for putting in a build server nightly build.  Obviously none of these tests are safe for running on production and better integration testing is no substitute to refactoring, dependency inversion and writing true unit tests that are independent of the peculiarities of the persistent data store.