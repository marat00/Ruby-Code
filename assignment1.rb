#!/usr/local/bin/ruby
# SCRIPT:  lab1.rb
# CREATOR: Marat Pernabekov

# This script will showcase several String methods in Ruby.
the_string = '            this string has leading space and too    MANY 
tabs and sPaCes betweenX
   the indiVidual Words in each Line.X
  each Line ends with a accidentally  aDDED  X.X
            in this lab you wilL WRITE code that "sAnITizES" this string by normalizingX
   ("normalizing" means   capitalizing sentences   and setting otherX
  characters to lower case)     and removes in       the extra spaces between WOrds.X'

puts 'The string we will work with:'
puts the_string
puts '--------------------------------------------------------------------------------------------'

# Question 4.1 -- Squeeze the whitespaceputs '4.1 squeeze:'
puts '4.1 squeeze:'
puts the_string.squeeze(' ')
puts '---------------------------------------------------------------------------------------------'

# Question 4.2 -- Downcase
puts '4.2 downcase:'
puts the_string.downcase
puts '----------------------------------------------------------------------------------------------'

# Question 4.3 -- Upcase
puts '4.3 upcase:'
puts the_string.upcase
puts '-----------------------------------------------------------------------------------------------'

# Question 4.4 -- Capitalize
puts '4.4 capitalize first alphabetical character of each line:'
arr = the_string.split(/\n/).each { |x| print x.capitalize }
puts '-----------------------------------------------------------------------------------------------'

# Question 4.5 -- Remove the Ending X
puts '4.5 remove X:'
puts the_string.gsub('X','')
puts '-----------------------------------------------------------------------------------------------'

# Question 4.6 -- Display each byte
puts '4.6 each_byte:'
puts '---------','C|Dec|Hex', '---------'
str = the_string.split("")
str.each{|x| x.each_byte {|x| printf("%01s|%03d|0x%02x \n", x.chr, x.ord, x.to_s(16))}}
puts '-----------------------------------------------------------------------------------------------'

# Question 4.7 -- Split
puts '4.7 split:'
puts '', 'Splitting using the default delimiter (white space). The empty elements are not shown.'
print the_string.split()
puts '', ''
puts 'Splitting with an explicit \s parameter.'
print the_string.split(/\s/)
puts '------------------------------------------------------------------------------------------------'

# Question 4.8 -- Crypt
puts '4.8 crypt:'
puts the_string, ""
print 'Encrypted: ', the_string.crypt("GfgsAf5a")
puts '------------------------------------------------------------------------------------------------'

# Question 4.9 -- Replace
puts '4.9 replace:'
print 'Object ID Before:', the_string.object_id
puts
string1 = the_string.slice(0..97)
puts string1.replace(string1.strip.reverse.squeeze.upcase) + the_string.slice(98..400)
print 'Object ID After:', the_string.object_id
puts
puts '------------------------------------------------------------------------------------------------'

# Question 4.10 -- Inspect
puts '4.10 inspect:'
string1 = the_string.slice(0..97)
string2 = string1.replace(string1.strip.reverse.squeeze.upcase) + the_string.slice(98..400)
puts string2.inspect
puts '------------------------------------------------------------------------------------------------'
