#!/usr/local/bin/ruby
# Name: Marat Pernabekov
# CRN: 73157
# Assignment: Lab 5
# File: bluecloth.cgi
# encoding: utf-8

# Boilerplate
$:.unshift(File.dirname(__FILE__))
require 'cgi_helper'
include CGI_Helper
ENV['GEM_HOME']='/students/mpernabe/mygems'
require 'bluecloth'
http_header
# End of boilerplate

# Read the input from a text file if it exists
oliver = File.readlines('../../oliver.markdown.txt').
         join if File.exist?('../../oliver.markdown.txt')

# Display the text in html
unless oliver.nil?
   puts BlueCloth::new(oliver).to_html
else
   puts 'Error, could not open file.'
   raise Exception, 'Could not open file: oliver.markdown.txt'
end