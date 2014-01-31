#!/usr/local/bin/ruby
# Name      : Marat_Pernabekov
# CRN       : 73157
# Assignment: Week 7 Exercise
# File      : week7.cgi

##
# Add the absolute path of current directory to Ruby search path
$:.unshift(File.dirname(__FILE__))

require 'cgi_helper'
include CGI_Helper
require 'cgi'
cgi = CGI.new

if not cgi.params['profile'][0].nil?
    require 'profile'
end

@crn=true

##
# Print the Content-type
http_header

class MissingCRNError < StandardError; end

##
# Add the relative path of current directory to Ruby search path
$:.unshift('.')

##
# Add two methods to the String class
class String
  #
  # 
  def ucwords
    #
    # Encoding to UTF-8
    out = self.force_encoding('UTF-8').gsub(/\W/,' ')
    #
    # split on word boundaries then capitalize
    out.split(/\b\s+\b/).collect {|w| w.capitalize }.join(' ') 
  end 

  def alternating_case 
    # alternate upper and lower case characters
    count = 0 
    out = ''

    #
    # Find every character
    self.scan(/./m) do |b| 
        if count == 0 
          out << b.upcase && count = 1 
        else
          out << b.downcase && count = 0 
        end  
    end 
    
    # return the empty string if necessary
    out 
  end 
end

begin
    @@n = 0

    def bgcolor(n)
      @@n += 15
      red   = "%02x" %  ((@@n + n) % 200).abs
      green = "%02x" % ((127 -  n) % 200).abs
      blue  = "%02x" %  ((127 + n) % 200).abs
      "#{red}#{green}#{blue}"
    end

    @crn = nil

    crns = ['73157','74686']

    @crn = cgi.params['crn'][0].to_s

    if @crn.nil?
       raise MissingCRNError.new('CRN is nil')
    elsif
       unless crns.include?(@crn)
        raise MissingCRNError.new()
       end
    end

    @sort_by = cgi.params['sort_by'][0].to_s
    @sort_by = 'user_name' if @sort_by.nil?


    start = Time.now

    ## 
    # A handy array of field @names for printing the HTML <th> tags in the ERB template
    @fields = [ :number, :user_name, :password, :uid, :gid, :gcos_field,:home_directory, :login_shell]

    ##
    # The Student class
    class Student
      ##
      # A class variable to count the number of students
      @@count = 0;

      ##
      # Create the accessors all at once.
      attr_accessor :number,:user_name, :password, :uid, :gid, :gcos_field,:home_directory, :login_shell

      def initialize(data)
        @number = @@count + 1;
        @@count = @number;

        ##
        # Use parallel assignment to an array to a list to initialize each object
        @user_name,@password,@uid,@gid,@gcos_field,@home_directory,@login_shell  = data
      end
    end

    # Get the group line from /etc/passwd. There are many ways to do this, but
    # some methods are more efficient than others. Ideally  you want to go through
    # the file one time only. The Ruby Enumberable::detect method will stop when
    # it detects a match.
    #
    #line = File.readlines('/etc/group').scan {|line| line =~ /77734/ }

    # Get the line containing student @names,
    # We can do this in a ridiculously long single line of code that chains methods together. You
    # can also break this single line into multiple lines if you wish.
    #               read all lines          detect line                         split it on ":", chomp,splt,sort!
    students = File.readlines('/etc/group').detect {|line| line =~ /^c#{@crn}:/ }.split(':')[3].chomp.split(',').sort!

    ##
    # Use a hash to store student data. Hashes are the most efficient way to store and retrieve
    # data.  O(1)
    big_hash = {}

    ##
    # Again, we want to go through the password file one time only, collecting student 
    # records along the way.
    File.new('/etc/passwd').collect { |x| student_name = x.split(':')[0];big_hash[x.split(':')[0]] = x.chomp if students.include? student_name}

    ##
    # @for_template will be printed in the ERB template.
    @for_template = ''

    ##
    # Some arrays for collecting 
    uids = []
    @students_array = []

    ##
    # Now that we have all the student data (line 115), we can create Student objects
    students.each do |s|

      ##
      # If there are any empty elements, skip them
      next if big_hash[s].nil?

      ##
      # Create a new Student object with each student's data)
      # The constructor requires an array of data
      o = Student.new(big_hash[s].split(':'))

      ##
      # Save the User Id into the collector array
      uids << o.uid

      ##
      # Add the student instance to the collector array
      @students_array << o
    end


    ##
    # If we're feeling ambitious we can sort the objects by attribute.
    # I use @sort_by to do this, and use the "send" method to set
    # the value we are sorting on. If you're really ambitious, you can
    # create a toggle sort. 
    begin

      ##
      # Set a default sort
      if @sort_by.nil? or @sort_by.empty?
        @sort_by = 'user_name'
      end
      
      if @sort_by == 'uid' || @sort_by == 'gid'
        @students_array =  @students_array.sort_by {|o| o.send(@sort_by.to_sym) }
      else
        @students_array =  @students_array.sort_by {|o| o.send(@sort_by.downcase) }
      end

    rescue Exception => e
      ##
      # If this fails for some reason, we'll find out why.
      puts @sort_by
      # puts e.message
      puts '<ol><li>'
      puts e.backtrace.join('</li><li>')
      puts '</li></ol>'
      puts '<pre>'
      puts (@students_array.to_s.gsub('>',">\n\n"))
      puts '</pre>'
    end

    finish = Time.now
    @for_template +=  'Elapsed time: ' + (finish.to_f - start.to_f).to_s + '</pre>'
    html = File.read('sorting.lab5_template.html.erb')


    # Collect the source code for printing in the ERB template
    @source_code = '<div id="source-code" style="display:none;">'
    @source_code += <<END
    <div style="background-color:transparent;color:#efe;">

END
    @source_code += '<div style="padding:2em;width:94%;background-color:lightyellow"><h1>week7.cgi Source Code</h1>'
    @source_code += '<pre>'
    @source_code += CGI.escapeHTML(File.read('week7.cgi'))
    @source_code += '</pre>'
    @source_code += '<h1>cgi_helper.rb Source Code</h1>'
    @source_code += '<pre>'
    @source_code += CGI.escapeHTML(File.read('cgi_helper.rb'))
    @source_code += '</pre>'
    @source_code += '</div>'

    # The render method is in cgi_helper.rb
    puts render(html)

rescue MissingCRNError => e
     #puts e.message
     puts <<HTML
     <h4>Select a CRN to view the demo for your class.</h4>
     <ul>
     <h5>Fall</h5>
     <li><a href="?crn=73157">73157</a></li>
     <li><a href="?crn=74686">74686</a></li>
     </ul>
HTML
rescue Exception =>e
    puts '<hr>'
    puts '<h1>Error</h1>'
    puts '<pre>'
    puts e.message

    e.backtrace.each do |l|
        puts l
    end
    puts '</pre>'
end
