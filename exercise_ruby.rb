#!/usr/local/bin/ruby
# SCRIPT: hello_world.cgi
# CREATOR: Marat_Pernabekov
puts "Content-type: text/html"
puts # This blank line is mandatory

def palindrome(string)
   string.force_encoding('UTF-8").upcase.gsub!(/(\W*)/)
   puts string  == string.reverse ? string : string
end

str = 'Dennis, Nell, Edna, Leon, Nedra, Anita, Rolf, Nora, Alice, Carol, Leo, Jane, Reed, Dena, Dale, Basil, Rae, Penny, Lana, Dave, Denny, Lena, Ida, Bernadette, Ben, Ray, Lila, Nina, Jo, Ira, Mara, Sara, Mario, Jan, Ina, Lily, Arne, Bette, Dan, Reba, Diane, Lynn, Ed, Eva, Dana, Lynne, Pearl, Isabel, Ada, Ned, Dee, Rena, Joel, Lora, Cecil, Aaron, Flora, Tina, Arden, Noel, and Ellen sinned.'

palindrome(str)