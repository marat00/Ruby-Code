#!/usr/local/bin/ruby
# SCRIPT: lab2.cgi
# CREATOR: Marat_Pernabekov
require 'cgi'
puts "Content-type: text/html"
puts # This blank line is mandatory

# display the original string
the_string = <<-HERE
               this string has leading space and too    MANY tabs and sPaCes betweenX
   the indiVidual Words in each Line.X
  each Line ends with a accidentally  aDDED  X.X
            in this lab you wilL WRITE code that "sAnITizES" this string by normalizingX
   ("normalizing" means   capitalizing sentences   and setting otherX
  characters to lower case)     and removes in       the extra spaces between WOrds.X
HERE

puts the_string

# display the initial array
puts "\nThe Initial Array"
array = the_string.scan(/\s|\S/)
print array

# display Part 1
puts "\n\n#3 Contents of Part 1"
array1 = array.slice(0..138)
print array1

# display Part 2
puts "\n\n#4 Contents of Part 2"
array2 = array.slice(139..the_string.length)
print array2

# display common elements
puts "\n\n#5 Set of Common Elements"
print array1 & array2

# display the differences between arrays
puts "\n\n#6 Differences Between Parts One and Two"
print array1 - array2
puts
puts "\n\n#7 Differences Between Parts Two and One"
print array2 - array1
puts

# display elements at end of each array
puts "\n\n#8 Elements At End of Parts One and Two"
puts 'One: ' + array1.at(-1).inspect
puts 'Two: ' + array2.at(-1).inspect
puts

# display elements at front of each array
puts "\n\n#9 Elements At Front of Parts One and Two"
puts 'One: ' + array1.first.inspect
puts 'Two: ' + array2.first.inspect
puts

# upcasing the characters in Part Two and remove whitespace
# append the result to Part One and then flatten the new Part One
puts "\n\n#10 Part Two, Upcased With White Space Removed, Inserted Into One At Index 100, And Flattened"
array2.delete_if{|w| w == "\n"|| w == " "}.map!(&:upcase)
array1.insert(99, array2)
print array1.flatten!

# remove whitespace from the New Part One
puts "\n\n#11 The New Array With Spaces Removed"
print array1.delete_if{|x| x == " " || x == "\n"}

# add "!" to all characters in Part One
puts "\n\n#12 After Adding A '!' To Each Element"
print array1.collect!{|x| x + "!"}

# remove the last element and show the modified array
puts "\n\n#13 #13 Popped The Last Element"
puts pop = array1.pop
print "The remainder:" 
print array1

puts "\n\n"
print array1.unshift(pop)

puts "\n\n"
print array1.delete_if{|x| x != %r(A-Z)}