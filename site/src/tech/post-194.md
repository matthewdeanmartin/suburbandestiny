---
date: '2007-02-02'
recovered_from: wayback
slug: post-194
source_file: C:\github\dead_blog\data\normalized\tech.wakayos.com\root\__query__\m\200702\index.html
source_site: suburbandestiny-tech
source_url: http://tech.wakayos.com/?p=194
title: Exporting Gridviews with ASP.NET
---


How to export a ASP.NET gridview to excel, plus how to deal with the occasional control not rendered in a form error.


Public Overrides Sub VerifyRenderingInServerForm(ByVal control As Control)  

‘Do nothing.  

End Sub


Protected Sub btnExport\_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles btnExport.Click  

Response.Clear()  

Response.AddHeader(“content\-disposition”, “attachment;filename\=FileName.xls”)  

Response.Charset \= “”


‘If you want the option to open the Excel file without saving than


‘comment out the line below


‘Response.Cache.SetCacheability(HttpCacheability.NoCache)


Response.ContentType \= “application/vnd.xls”  

Dim stringWrite As System.IO.StringWriter \= New System.IO.StringWriter()  

Dim htmlWrite As System.Web.UI.HtmlTextWriter \= New HtmlTextWriter(stringWrite)


Me.grdData.RenderControl(htmlWrite)  

Response.Write(stringWrite.ToString())  

Response.End()  

End Sub