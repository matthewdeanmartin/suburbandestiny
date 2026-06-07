---
date: '2007-05-25'
recovered_from: wayback
slug: post-215
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200705\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=215
title: ASP.NET DropDownList and Unexpected Data
---


**The Problem**  

You are data binding to a table. One of the columns, say US state, should have a limited domain, but for various reasons, values outside of that range appear. For example, you might be importing the data from a second system that uses the state field for country and state.�  

You don’t want to throw away the invalid state, for example the value, “UK” You want the user to correct them as they find them. The user should be shown the invalid value, given the option to leave it alone, but not given the option to change it to anything other than one of the fifty US states.  

Plain HTML drop down controls can’t show a value that isn’t on the list of options.


`<select>  

<option value="OH">Ohio</option>  

<option value="VA" selected="selected">Virginia</option>  

</select>`


You can’t set the value to “UK” because there isn’t an option.


**Solutions.**  

**Ugly solution \#1\.** Use foreign keys. Make a foreign key between the state table and the address table. The data import package will blow up on invalid foreign keys. Make the data service group clean up the mess without the help of an ASP.NET application.


**Ugly solution \#2\.** Update the SqlDataSource to use a combination of valid and found values. So if the table was pubs, you would use


`SELECT state value, state + ' Bad' description  

FROM authors  

where state not in (select state from states)  

GROUP BY state  

union  

select state, state as v from states`  

This solution is ugly because what was an isolated component, a drop down that lists the states, now needs to know all the parameters necessary to run the same query that the datagrid is using.


**Promising solution \#3\.** Use a third party control that simulates a drop down through a series of divs. This would have worked, but the Telerik Rad ComboBox had the exact same behavior as the Microsoft DropDownList—it blows up on an unexpected value.  

More Elegant Solution. For the ASP.NET DropDownList, we can create a new user control project, add the following class. This class overrides the DataBinding event. If the OnDataBinding event raises the dread out of range error, we torture the naming container until we get the value. We add it to the list with a description showing that we don’t approve of selecting it and select it. \*Note, I didn’t invent this technique, I found variants on forums.


**`Imports System  

Imports System.Collections.Generic  

Imports System.ComponentModel  

Imports System.Text  

Imports System.Web  

Imports System.Web.UI  

Imports System.Web.UI.WebControls  

Imports Microsoft.VisualBasic  

<DefaultProperty("Text"), ToolboxData("<{0}:BetterDropDown runat=server></{0}:BetterDropDown>")> _  

Public Class BetterDropDown  

Inherits System.Web.UI.WebControls.DropDownList`**`Protected Overrides Sub OnDataBinding(ByVal e As System.EventArgs)  

Try  

MyBase.OnDataBinding(e)  

Catch OutOfRangeEx As System.ArgumentOutOfRangeException  

Dim gvr As GridViewRow = CType(Me.NamingContainer, GridViewRow)  

Dim drv As DataRowView = CType(gvr.DataItem, DataRowView)  

Dim v As String = drv.Item(Me.DataValueField).ToString()  

Me.ClearSelection()  

Dim li As ListItem = New ListItem("BAD:" & v, v)  

li.Selected = True  

Me.Items.Insert(0, li)  

Catch ex As Exception  

Throw ex  

End Try`


**End Sub**


**End Class**


The client code looks like this. Notice that the DropDownList’s data source doesn’t need to reference the author’s table anymore, we don’t get an ugly error when an author is recorded as living in the state of UK


**`<%@ Register Assembly="BetterDD" Namespace="BetterDD" TagPrefix="asp" %>  

<asp:GridView  

ID="GridView1"  

runat="server"  

AutoGenerateColumns="False"  

DataKeyNames="au_id"  

DataSourceID="SqlDataSource2">  

<Columns>  

<asp:BoundField DataField="au_lname" HeaderText="au_lname" SortExpression="au_lname" />  

<asp:BoundField DataField="au_fname" HeaderText="au_fname" SortExpression="au_fname" />  

<asp:TemplateField HeaderText="state" SortExpression="state">  

<ItemTemplate>  

<asp:BetterDropDown  

ID="DropDownList1"  

runat="server"  

SelectedValue='<%# Bind("State") %>'  

DataTextField="State"  

DataValueField="State"  

DataSourceID="SqlDataSource1">  

</asp:BetterDropDown>  

</ItemTemplate>  

</asp:TemplateField>  

</Columns>  

</asp:GridView>`**


 **\<asp:SqlDataSource  

ID\=”SqlDataSource1″  

runat\=”server”  

ConnectionString\=”\<%$ ConnectionStrings:pubsConnectionString %\>”  

SelectCommand\=”select state, ‘y’ as v from states”\>\</asp:SqlDataSource\>  

\<asp:SqlDataSource  

ID\=”SqlDataSource2″  

runat\=”server”  

ConnectionString\=”\<%$ ConnectionStrings:pubsConnectionString %\>”  

SelectCommand\=”SELECT \[au\_id], \[au\_lname], \[au\_fname], \[state] FROM \[authors]“\>  

\</asp:SqlDataSource\>**