#!/usr/local/bin/ruby       
# Name: Marat Pernabekov    
# CRN : 73157               
# Assignment: Lab 5         
# File: dangerous.cgi       
# encoding: utf-8           

require 'cgi'

cgi = CGI.new('html4')
@message = ''

# Accept input and determine the message to be displayed.
# If the text is dangerous, mark text as tainted.
if cgi.params['get_text']
   @text = cgi.params['get_text'].join
   if @text =~ /[\*'"`;-]/
     @message = 'Beware: Dangerous!'
     @text.taint
   else
     @message = 'Harmless'
     @text.untaint
   end
end

# Use CGI to create an html form, which will check if
# the user input is dangerous. Dangerous input has any or
# all of the following characters (*'"`;-).
cgi.out(content_type_string='text/html') do
  cgi.html('DOCTYPE' => '<!DOCTYPE html>') do
    cgi.head{"\n" + CGI::unescape_html('<link rel = "stylesheet" type =
       "text/css" href="../css/form.css" />') + cgi.
       title{'Dangerous or Harmless - Marat Pernabekov'} } +
     cgi.body() do
       cgi.multipart_form() do
         cgi.h1 { "Dangerous or Harmless?" } + "\n" +
         cgi.br + 
         cgi.h3 { "Please enter some text: "} + "\n" +
         cgi.textarea("get_text", 50, 9) + "\n" +
         cgi.br + 
         cgi.submit('Check it out =>')
       end +
       cgi.pre() do
          "\n" +
          if @text.tainted?
             cgi.div('id' => 'tainted'){
             '%s' % @message + "\n" +
             '%s' % @text.gsub(/\[*\\*\]*/ ,'') }
          else
             cgi.div('id' => 'untainted'){
             '%s' % @message + "\n" +
             '%s' % @text.gsub(/\[*\\*\]*/ ,'') }
          end
       end
    end
  end
end
