#!/usr/local/bin/ruby
# SCRIPT: hello_world.cgi
# CREATOR: Marat_Pernabekov
puts "Content-type: text/html"
puts # This blank line is mandatory

puts <<HTML
<!DOCTYPE html>
<html>
<head>
<title>A First Ruby CGI Script</title>
</head>
<body>
<h1>Hello, world!</h1>
<p> This is an example of a Ruby CGI script. It has the following 
features. </p>
<ol>
<li>A shebang line</li>
<li> A MIME type (<code>text/html</code>)</li>
<li>Some HTML to format the text</li>
</ol>
</body>
</html>
HTML

