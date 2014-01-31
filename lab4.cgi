#!/usr/local/bin/ruby
# Name      : Marat Pernabekov
# CRN       : 73157
# Assignment: Lab 4
# File      : lab4.cgi

# Add the absolute path of current directory to Ruby search path
$:.unshift(File.dirname(__FILE__))

require 'cgi_helper.rb'
include CGI_Helper
require 'cgi'
cgi = CGI.new

puts cgi.header('type' => 'text/html')
puts 

# Add the relative path of current directory to Ruby search path
$:.unshift('.')

 begin
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

    @crn1 = 73157.inspect
    @crn2 = 74686.inspect

    @sort_by = cgi.params['sort_by'][0].to_s
    @sort_by = 'user_name' if @sort_by.nil?

    start = Time.now

    # A handy array of field @names for printing the HTML <th> tags in the ERB template
    @fields = [:number, :user_name, :password, :uid, :gid, :gcos_field, :home_directory, :shell]

    # The Student class
    class Student
      # A class variable to count the number of students
      @@count = 0

      # Create the accessors all at once.
      attr_accessor :number, :user_name, :password, :uid, :gid, :gcos_field, :home_directory, :shell

      def initialize(data)
        @number = @@count + 1
        @@count = @number

        # Provided data is an array containing the 7 pieces of password data
        @user_name, @password, @uid, @gid, @gcos_field, @home_directory, @shell = data
      end
    end

    # Get the line containing student names.
    students1, students2 = File.readlines('/etc/group').select{|line| line =~ /^c#{@crn1}:/ || line =~ /^c#{@crn2}:/}
    students1 = students1.inspect.split(':')[3].chomp.gsub!('\n"', "").split(',')
    students2 = students2.inspect.split(':')[3].chomp.gsub!('\n"', "").split(',')
    students = students1 + students2
    # Use a hash to store student data. 
    big_hash = {}

    # Go through the password file, collecting student records along the way. 
    File.new('/etc/passwd').collect { |x| student_name = x.split(':')[0]; big_hash[x.split(':')[0]] =  x.chomp if students.include? student_name}

    # Create a collection array
    @students_array = []

    # Now that we have all the student data, we can create Student objects
    students.each do |s|
      # If there are any empty elements, skip them
      next if big_hash[s].nil?

      # Create a new Student object to hold each student's data
      # The constructor requires an array of data
      o = Student.new(big_hash[s].split(':'))

      # Add the student instance to the collector array
      @students_array << o
    end

    # Create a table
    @html = []
    
    # Populate the table with student data
    @students_array.each do |s|
       @html << '<tr><td>' + s.number.inspect + '</td>'
       @html << '<td>' + s.user_name + '</td>'
       @html << '<td>' + s.password + '</td>'
       @html << '<td>' + s.uid.inspect.gsub('"', '') + '</td>'
       @html << '<td>' + s.gid.inspect.gsub('"', '') + '</td>'
       @html << '<td>' + s.gcos_field + '</td>'
       @html << '<td>' + s.home_directory + '</td>'
       @html << '<td>' + s.shell + '</td>' + '</tr>'
    end

    # Finish the table
    rhtml = File.read('../../lab4.html')

    # Call the render_erb method from cgi_helper.rb
    puts render_erb(rhtml)

    # Display time taken for the script to run
    finish = Time.now
    print 'Elapsed time: ' + (finish.to_f - start.to_f).to_s

 rescue Exception => e
   puts '<h1>Error</h1>'
   puts '<pre>'
   #puts e.message

    e.backtrace.each do |l|
      puts l
    end
   puts '</pre>'
 end
