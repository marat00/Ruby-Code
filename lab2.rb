#!/usr/local/bin/ruby
# SCRIPT: lab2.cgi
# CREATOR: Marat_Pernabekov
puts "Content-type: text/html"
puts # This blank line is mandatory

puts <<HTML
<!DOCTYPE html>
<html>
<head>
<title>Lab 2 - Marat Pernabekov</title>
</head>
<body>
<% the_string = '            this string has leading space and too    MANY 
tabs and sPaCes betweenX
   the indiVidual Words in each Line.X
  each Line ends with a accidentally  aDDED  X.X
            in this lab you wilL WRITE code that "sAnITizES" this string by normalizingX
   ("normalizing" means   capitalizing sentences   and setting otherX
  characters to lower case)     and removes in       the extra spaces between WOrds.X' %>

puts the_string.scan(/\s\S/).join()


</body>
</html>
HTML