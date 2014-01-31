#!/usr/local/bin/ruby
# Name      : Marat_Pernabekov
# CRN       : 73157
# Assignment: Lab 4
# File      : lab4.cgi

# Add the absolute path of current directory to Ruby search path
$:.unshift(File.dirname(__FILE__))

require 'cgi_helper'
include CGI_Helper
require 'cgi'
cgi = CGI.new

@crn=true

# Print the Content-type
http_header

# Add the relative path of current directory to Ruby search path
$:.unshift('.')

# Add two methods to the String class
class String
  # Capitalize the first word in the sentence
  def ucwords 
    # Set encoding to UTF-8
    out = self.force_encoding('UTF-8').gsub(/\W/,' ')
    
    # Split on word boundaries then capitalize
    out.split(/\b\s+\b/).collect {|w| w.capitalize }.join(' ') 
  end 
  
  def alternating_case 
    # Alternate upper and lower case characters
    count = 0 
    out = ''

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

    @crn1 = cgi.params['crn1'][0].to_s
    @crn2 = cgi.params['crn2'][1].to_s

    @sort_by = cgi.params['sort_by'][0].to_s
    @sort_by = 'user_name' if @sort_by.nil?

    start = Time.now

    # A handy array of field @names for printing the HTML <th> tags in the ERB template
    @fields = [:number,:user_name,:password,:uid,:gid,:gcos_field,:home_directory,:shell]

    # The Student class
    class Student
      # A class variable to count the number of students
      @@count = 0;

      # Create the accessors all at once.
      attr_accessor :number,:user_name,:password,:uid,:gid,:gcos_field,:home_directory,:shell

      def initialize(data)
        @number = @@count + 1;
        @@count = @number;

        # Provided data is an array containing the 7 pieces of password data
        @user_name,@password,@uid,@gid,@gcos_field,@home_directory,@shell = data
      end
    end

    # Get the line containing student names.
    students = File.readlines('/etc/group').detect {|line1, line2| line1 =~ /^c#{@crn1}:/ 
                line2 =~ /^c#{crn2}:/}
    students = students.split(':')[3].chomp.split(',').sort!

    # Use a hash to store student data.
    big_hash = {}

    # Go through the password file, collecting student records along the way.
    File.new('/etc/passwd').collect { |x| student_name = x.split(':')[0];big_hash[x.split(':')[0]] = x.chomp if students.include? student_name}

    # @for_template will be printed in the ERB template.
    @for_template = ''

    # Some arrays for collecting 
    uids = []
    @students_array = []

    # Now that we have all the student data (line 115), we can create Student objects
    students.each do |s|
      # If there are any empty elements, skip them
      next if big_hash[s].nil?

      # Create a new Student object to hold each student's data
      # The constructor requires an array of data
      o = Student.new(big_hash[s].split(':'))

      # Save the User Id into the collector array
      uids << o.uid

      # Add the student instance to the collector array
      @students_array << o
    end

     # Sort the objects by attribute.
    begin
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
      # If this fails for some reason, we'll find out why.
      puts @sort_by
      # puts e.message
      puts '<ol><li>'
      puts e.backtrace.join('</li><li>')
      puts '</li></ol>'
      puts '<pre>'
      puts #{@students_array.to_s.gsub('>',">\n\n")}
      puts '</pre>'
    end

    finish = Time.now
    @for_template +=  'Elapsed time: ' + (finish.to_f - start.to_f).to_s + '</pre>'
    html = []
    html << '<table border = "1">'
    html << '<tr>'
    @fields.each do |f|
       html << '<td>' + s1.send(f) + '</td>' + "\n"
    end
    html << '</tr>'
    html << '</table>'
    html1 = File.read('~/public_html/lab4.html')

    # Call the render_erb method from cgi_helper.rb
    puts render_erb(html1)
