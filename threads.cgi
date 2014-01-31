#!/usr/local/bin/ruby
# Name: Marat Pernabekov
# CRN: 73157
# Assignment: Lab 5
# File: threads.cgi
# encoding: utf-8

$:.unshift(File.dirname(__FILE__))

# Boilerplate
require 'cgi_helper.rb'
include CGI_Helper
require 'cgi'
cgi = CGI.new('html4')
http_header
# End of boilerplate

# Create an array of alphabetical characters
letters = ("a".."z").to_a + ("A".."Z").to_a

puts <<HTML
<!doctype html>
<html>
<head>
<meta name=charset value=utf-8>
<link rel='stylesheet' type='text/css' href='../css/threads.css'
<body>
HTML

# Create an array of threads
threads = []

# Create 10 threads and let them individually go through each
# letter of the alphabet, displaying the result on the screen
10.times do |count|
  thread = Thread.new do 
     letters.each do |char|
        print '<span class=thread' + count.to_s + '>' + char +
           '<sub class=thread' + count.to_s+ '>' + count.inspect +
           '</sub></span>'; $stdout.flush; sleep rand(6)
     end
  end
  threads << thread   # pass the result into the threads array
end

# Join the threads
threads.each {|thread| thread.join}

# End html
puts '</body><html>'
