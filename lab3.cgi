#!/usr/local/bin/ruby
# Name      : Marat_Pernabekov
# CRN       : 73157
# Assignment: Lab 3
# File      : lab3.cgi
puts "Content-type: text/html"
puts

#HTML beginning
puts <<HTML
<!DOCTYPE html>
<html>
<head>
<title>Lab 3 - Marat Pernabekov</title>
</head>
<body>
<h1>CS 132A Lab 3 Solution</h1>
<br />
HTML

speeches = [] # filename array
stop_words = File.read("../../stop_words.txt") # stop words

# fill the speeches array
Dir.glob("../../speeches/*.txt").each do|file|
	speeches << file.to_s
end

#Lincoln 1st
text_linc1 = File.read(speeches.at(1)).force_encoding('UTF-8')
linc1_words = text_linc1.downcase.scan(/\w+/)
linc1_good = linc1_words.select { |linc1| !stop_words.include?(linc1) }
linc1_sents = text_linc1.gsub(/\s+/, ' ').strip.split(/\.|\?|!/)
linc1_sorted = linc1_sents.sort_by {|sentence| linc1_sents.length}
linc1_split = linc1_sorted.length / 3
ideal_linc1 = linc1_sorted.slice(linc1_split + 1..-1)
ideal_linc1 = ideal_linc1.select { |ideal| ideal =~ /is|are/ }

puts '<div><h2><a href="~mpernabe/speeches/abraham_lincoln_1st.txt">Abraham Lincoln 1st Inauguration Speech</h2>'
puts "<h3>STATISTICS</h3>"
puts "<p>Lines &emsp;&emsp; #{text_linc1.lines.count}</p>"
puts "<p>Characters &emsp;&emsp; #{text_linc1.length}</p>"
puts "<p>Characters (exc. spaces) &emsp;&emsp; #{text_linc1.gsub(/\s+/, '').length}</p>"
puts "<p>Word Count &emsp;&emsp; #{text_linc1.split.length}</p>"
puts "<p>sentences &emsp;&emsp; #{text_linc1.split(/\.|\?|!/).length}</p>"
puts "<p>Paragraphs &emsp;&emsp; #{text_linc1.split(/\n\n/).length}</p>"
puts "<p>Sentences / Paragraph &emsp;&emsp;" +
"#{text_linc1.split(/\.|\?|!/).length / text_linc1.split(/\n\n/).length}</p>"
puts "<p> Words / Sentence &emsp;&emsp; #{text_linc1.split.length / text_linc1.split(/\.|\?|!/).length}</p>"
puts "<p> Non-fluff &emsp;&emsp; #{(linc1_good.length.to_f / linc1_words.length.to_f * 100).to_i }\%</p><br />"
puts "<h3>ABSTRACT</h3>"
puts "<p>#{ideal_linc1.join(". ") }. </p><br />"
puts "<h3>THE TEN MOST COMMON WORDS</h3>"
common_linc1 = ideal_linc1.each_with_object(Hash.new(0)) { |words, num| words[num] += 1}
puts "<p>#{common_linc1.sort {|a,b| a[1] <=> b[1] }.reverse![0,10].join(" ") }</p>"


#Lincoln 2nd
text_linc2 = File.read(speeches.at(9)).force_encoding('UTF-8')
linc2_words = text_linc2.downcase.scan(/\w+/)
linc2_good = linc2_words.select { |linc2| !stop_words.include?(linc2) }
linc2_sents = text_linc2.gsub(/\s+/, ' ').strip.split(/\.|\?|!/)
linc2_sorted = linc2_sents.sort_by {|sentence| sentence.length}
linc2_split = linc2_sorted.length / 3
ideal2_linc2 = linc2_sorted.slice(linc2_split + 1..-1)
ideal2_linc2 = ideal_linc2.select { |ideal| ideal =~ /is|are/ }

puts '<div><h2><a href="~mpernabe/speeches/abraham_lincoln_2nd.txt">Abraham Lincoln 2nd Inauguration Speech</h2>'
puts "<h3>STATISTICS</h3>"
puts "<p>Lines &emsp;&emsp; #{text_linc2.lines.count}</p>"
puts "<p>Characters &emsp;&emsp; #{text_linc2.length}</p>"
puts "<p>Characters (exc. spaces) &emsp;&emsp; #{text_linc2.gsub(/\s+/, '').length}</p>"
puts "<p>Word Count &emsp;&emsp; #{text_linc2.split.length}</p>"
puts "<p>sentences &emsp;&emsp; #{text_linc2.split(/\.|\?|!/).length}</p>"
puts "<p>Paragraphs &emsp;&emsp; #{text_linc2.split(/\n\n/).length}</p>"
puts "<p>Sentences / Paragraph &emsp;&emsp; #{text_linc2.split(/\.|\?|!/).length / text_linc2.split(/\n\n/).length}</p>"
puts "<p> Words / Sentence &emsp;&emsp; #{text_linc2.split.length / text_linc2.split(/\.|\?|!/).length}</p>"
puts "<p> Non-fluff &emsp;&emsp; #{(linc2_good.length.to_f / linc2_words.length.to_f * 100).to_i }\%</p><br />"
puts "<h3>ABSTRACT</h3>"
puts "<p>#{ideal_linc2.join(". ") }. </p><br />"
puts "<h3>THE TEN MOST COMMON WORDS</h3>"
common_linc2 = ideal_linc2.each_with_object(Hash.new(0)) { |words, num| words[num] += 1}
puts "<p>#{common_linc2.sort {|a,b| a[1] <=> b[1] }.reverse![0,10].join("  ") }</p>"


#Clinton 1st
text_clint = File.read(speeches.at(2)).force_encoding('UTF-8')
clint_words = text_clint.downcase.scan(/\w+/)
clint_good = clint_words.select { |words| !stop_words.include?(words) }
clint_sents = text_clint.gsub(/\s+/, ' ').strip.split(/\.|\?|!/)
clint_sorted = clint_sents.sort_by { |sentence| sentence.length }
clint_split = clint_sorted.length / 3
ideal_clint = clint_sorted.slice(clint_split + 1..-1)
ideal_clint = ideal_clint.select { |ideal| ideal =~ /is|are/ }

puts '<div><h2><a href="~mpernabe/speeches/bill_clinton_1st.txt">Abraham Lincoln 2nd Inauguration Speech</h2>'
puts "<h3>STATISTICS</h3>"
puts "<p>Lines &emsp;&emsp; #{text_clint.lines.count}</p>"
puts "<p>Characters &emsp;&emsp; #{text_clint.length}</p>"
puts "<p>Characters (exc. spaces) &emsp;&emsp; #{text_clint.gsub(/\s+/, '').length}</p>"
puts "<p>Word Count &emsp;&emsp; #{text_clint.split.length}</p>"
puts "<p>sentences &emsp;&emsp; #{text_clint.split(/\.|\?|!/).length}</p>"
puts "<p>Paragraphs &emsp;&emsp; #{text_clint.split(/\n\n/).length}</p>"
puts "<p>Sentences / Paragraph &emsp;&emsp; #{text_linc2.split(/\.|\?|!/).length / text_linc2.split(/\n\n/).length}</p>"
puts "<p> Words / Sentence &emsp;&emsp; #{text_clint.split.length / text_clint.split(/\.|\?|!/).length}</p>"
puts "<p> Non-fluff &emsp;&emsp; #{(clint_good.length.to_f / clint_words.length.to_f * 100).to_i }\%</p><br />"
puts "<h3>ABSTRACT</h3>"
puts "<p>#{ideal_clint.join(". ") }. </p><br />"
puts "<h3>THE TEN MOST COMMON WORDS</h3>"
common_clint = ideal_clint.each_with_object(Hash.new(0)) { |words, num| words[num] += 1}
puts "<p>#{common_clint.sort {|a,b| a[1] <=> b[1] }.reverse![0,10].join("  ") }</p>"


#Jefferson 1st
text_jef = File.read(speeches.at(5)).force_encoding('UTF-8')
jef_words = text_jef.downcase.scan(/\w+/)
jef_good = jef_words.select { |words| !stop_words.include?(words) }
jef_sents = text_jef.gsub(/\s+/, ' ').strip.split(/\.|\?|!/)
jef_sorted = jef_sents.sort_by { |sentence| sentence.length }
jef_split = jef_sorted.length / 3
ideal_jef = jef_sorted.slice(jefsplit + 1..-1)
ideal_jef = ideal_jef.select { |ideal| ideal =~ /is|are/ }

puts '<div><h2><a href="~mpernabe/speeches/thomas_jefferson_1st.txt">Thomas Jefferson 1st Inauguration Speech</h2>'
puts "<h3>STATISTICS</h3>"
puts "<p>Lines &emsp;&emsp; #{text_jef.lines.count}</p>"
puts "<p>Characters &emsp;&emsp; #{text_jef.length}</p>"
puts "<p>Characters (exc. spaces) &emsp;&emsp; #{text_jef.gsub(/\s+/, '').length}</p>"
puts "<p>Word Count &emsp;&emsp; #{text_jef.split.length}</p>"
puts "<p>sentences &emsp;&emsp; #{text_jef.split(/\.|\?|!/).length}</p>"
puts "<p>Paragraphs &emsp;&emsp; #{text_jef.split(/\n\n/).length}</p>"
puts "<p>Sentences / Paragraph &emsp;&emsp; #{text_jef.split(/\.|\?|!/).length / text_jef.split(/\n\n/).length}</p>"
puts "<p> Words / Sentence &emsp;&emsp; #{text_jef.split.length / text_jef.split(/\.|\?|!/).length}</p>"
puts "<p> Non-fluff &emsp;&emsp; #{(jef_good.length.to_f / jef_words.length.to_f * 100).to_i }\%</p><br />"
puts "<h3>ABSTRACT</h3>"
puts "<p>#{ideal_jef.join(". ") }. </p><br />"
puts "<h3>THE TEN MOST COMMON WORDS</h3>"
common_jef = ideal_jef.each_with_object(Hash.new(0)) { |words, num| words[num] += 1}
puts "<p>#{common_jef.sort {|a,b| a[1] <=> b[1] }.reverse![0,10].join(" ") }</p>"



#Obama
text_ob = File.read(speeches.at(6)).force_encoding('UTF-8')
ob_words = text_ob.downcase.scan(/\w+/)
ob_good = ob_words.select { |words| !stop_words.include?(words) }
ob_sents = text_ob.gsub(/\s+/, ' ').strip.split(/\.|\?|!/)
ob_sorted = ob_sents.sort_by { |sentence| sentence.length }
ob_split = ob_sorted.length / 3
ideal_ob = ob_sorted.slice(ob_split + 1..-1)
ideal_ob = ideal_ob.select { |ideal| ideal =~ /is|are/ }

puts '<div><h2><a href="~mpernabe/speeches/barack_obama.txt">Barack Obama Inauguration Speech</h2>'
puts "<h3>STATISTICS</h3>"
puts "<p>Lines &emsp;&emsp; #{text_ob.lines.count}</p>"
puts "<p>Characters &emsp;&emsp; #{text_ob.length}</p>"
puts "<p>Characters (exc. spaces) &emsp;&emsp; #{text_ob.gsub(/\s+/, '').length}</p>"
puts "<p>Word Count &emsp;&emsp; #{text_ob.split.length}</p>"
puts "<p>sentences &emsp;&emsp; #{text_ob.split(/\.|\?|!/).length}</p>"
puts "<p>Paragraphs &emsp;&emsp; #{text_ob.split(/\n\n/).length}</p>"
puts "<p>Sentences / Paragraph &emsp;&emsp; #{text_ob.split(/\.|\?|!/).length / text_ob.split(/\n\n/).length}</p>"
puts "<p> Words / Sentence &emsp;&emsp; #{text_ob.split.length / text_ob.split(/\.|\?|!/).length}</p>"
puts "<p> Non-fluff &emsp;&emsp; #{(ob_good.length.to_f / ob_words.length.to_f * 100).to_i }\%</p><br />"
puts "<h3>ABSTRACT</h3>"
puts "<p>#{ideal_ob.join(". ") }. </p><br />"
puts "<h3>THE TEN MOST COMMON WORDS</h3>"
common_ob = ideal_ob.each_with_object(Hash.new(0)) { |words, num| words[num] += 1}
puts "<p>#{common_ob.sort {|a,b| a[1] <=> b[1] }.reverse![0,10].join(" ") }</p>"


#FDR
text_fdr = File.read(speeches.at(7)).force_encoding('UTF-8')
fdr_words = text_fdr.downcase.scan(/\w+/)
fdr_good = fdr_words.select { |words| !stop_words.include?(words) }
fdr_sent = text_fdr.gsub(/\s+/, ' ').strip.split(/\.|\?|!/)
fdr_sorted = fdr_sents.sort_by { |sentence| sentence.length }
fdr_split = fdr_sorted.length / 3
ideal_fdr = fdr_sorted.slice(fdrsplit + 1..-1)
ideal_fdr = ideal_fdr.select { |ideal| ideal =~ /is|are/ }

puts '<div><h2><a href="~mpernabe/speeches/franklin_roosevelt_2nd.txt">Frankling Roosevelt 2nd Inauguration Speech</h2>'
puts "<h3>STATISTICS</h3>"
puts "<p>Lines &emsp;&emsp; #{text_fdr.lines.count}</p>"
puts "<p>Characters &emsp;&emsp; #{text_fdr.length}</p>"
puts "<p>Characters (exc. spaces) &emsp;&emsp; #{text_fdr.gsub(/\s+/, '').length}</p>"
puts "<p>Word Count &emsp;&emsp; #{text_fdr.split.length}</p>"
puts "<p>sentences &emsp;&emsp; #{text_fdr.split(/\.|\?|!/).length}</p>"
puts "<p>Paragraphs &emsp;&emsp; #{text_fdr.split(/\n\n/).length}</p>"
puts "<p>Sentences / Paragraph &emsp;&emsp; #{text_fdr.split(/\.|\?|!/).length / text_fdr.split(/\n\n/).length}</p>"
puts "<p> Words / Sentence &emsp;&emsp; #{text_fdr.split.length / text_fdr.split(/\.|\?|!/).length}</p>"
puts "<p> Non-fluff &emsp;&emsp; #{(fdr_good.length.to_f / fdr_words.length.to_f * 100).to_i }\%</p><br />"
puts "<h3>ABSTRACT</h3>"
puts "<p>#{ideal_fdr.join(". ") }. </p><br />"
puts "<h3>THE TEN MOST COMMON WORDS</h3>"
common_fdr = ideal_fdr.each_with_object(Hash.new(0)) { |words, num| words[num] += 1}
puts "<p>#{common_fdr.sort {|a,b| a[1] <=> b[1] }.reverse![0,10].join(" ") }</p>"


#Teddy Roosevelt
text_ted = File.read(speeches.at(0)).force_encoding('UTF-8')
ted_words = text_ted.downcase.scan(/\w+/)
ted_good = tedwords.select { |words| !stop_words.include?(words) }
ted_sents = text_ted.gsub(/\s+/, ' ').strip.split(/\.|\?|!/)
ted_sorted = ted_sents.sort_by { |sentence| sentence.length }
ted_split = ted_sorted.length / 3
ideal_ted = ted_sorted.slice(ted_split + 1..-1)
ideal_ted = ideal_ted.select { |ideal| ideal =~ /is|are/ }

puts '<div><h2><a href="~mpernabe/speeches/teddy_roosevelt.txt">Teddy Roosevelt Inauguration Speech</h2>'
puts "<h3>STATISTICS</h3>"
puts "<p>Lines &emsp;&emsp; #{text_ted.lines.count}</p>"
puts "<p>Characters &emsp;&emsp; #{text_ted.length}</p>"
puts "<p>Characters (exc. spaces) &emsp;&emsp; #{text_ted.gsub(/\s+/, '').length}</p>"
puts "<p>Word Count &emsp;&emsp; #{text_ted.split.length}</p>"
puts "<p>sentences &emsp;&emsp; #{text_ted.split(/\.|\?|!/).length}</p>"
puts "<p>Paragraphs &emsp;&emsp; #{text_ted.split(/\n\n/).length}</p>"
puts "<p>Sentences / Paragraph &emsp;&emsp; #{text_ted.split(/\.|\?|!/).length / text_ted.split(/\n\n/).length}</p>"
puts "<p> Words / Sentence &emsp;&emsp; #{text_ted.split.length / text_ted.split(/\.|\?|!/).length}</p>"
puts "<p> Non-fluff &emsp;&emsp; #{(ted_good.length.to_f / ted_words.length.to_f * 100).to_i }\%</p><br />"
puts "<h3>ABSTRACT</h3>"
puts "<p>#{ideal_ted.join(". ") }. </p><br />"
puts "<h3>THE TEN MOST COMMON WORDS</h3>"
common_ted = ideal_ted.each_with_object(Hash.new(0)) { |words, num| words[num] += 1}
puts "<p>#{common_ted.sort {|a,b| a[1] <=> b[1] }.reverse![0,10].join(" ") }</p>"



#Nixon
text_nix = File.read(speeches.at(8).force_encoding('UTF-8')
nix_words = text_nix.downcase.scan(/\w+/)
nix_good = nix_words.select { |words| !stop_words.include?(words) }
nixsents = text_nix.gsub(/\s+/, ' ').strip.split(/\.|\?|!/)
nix_sorted = nix_sents.sort_by { |sentence| sentence.length }
nix_split = nix_sorted.length / 3
ideal_nix = nixsorted.slice(nixsplit + 1..-1)
ideal_nix = idealnix.select { |ideal| ideal =~ /is|are/ }

puts '<div><h2><a href="~mpernabe/speeches/richard_nixon.txt">Richard Nixon Inauguration Speech</h2>'
puts "<h3>STATISTICS</h3>"
puts "<p>Lines &emsp;&emsp; #{text_nix.lines.count}</p>"
puts "<p>Characters &emsp;&emsp; #{text_nix.length}</p>"
puts "<p>Characters (exc. spaces) &emsp;&emsp; #{text_nix.gsub(/\s+/, '').length}</p>"
puts "<p>Word Count &emsp;&emsp; #{text_nix.split.length}</p>"
puts "<p>sentences &emsp;&emsp; #{text_nix.split(/\.|\?|!/).length}</p>"
puts "<p>Paragraphs &emsp;&emsp; #{text_nix.split(/\n\n/).length}</p>"
puts "<p>Sentences / Paragraph &emsp;&emsp; #{text_nix.split(/\.|\?|!/).length / text_nix.split(/\n\n/).length}</p>"
puts "<p> Words / Sentence &emsp;&emsp; #{text_nix.split.length / text_nix.split(/\.|\?|!/).length}</p>"
puts "<p> Non-fluff &emsp;&emsp; #{(nix_good.length.to_f / nix_words.length.to_f * 100).to_i }\%</p><br />"
puts "<h3>ABSTRACT</h3>"
puts "<p>#{ideal_nix.join(". ") }. </p><br />"
puts "<h3>THE TEN MOST COMMON WORDS</h3>"
common_nix = ideal_nix.each_with_object(Hash.new(0)) { |words, num| words[num] += 1}
puts "<p>#{common_nix.sort {|a,b| a[1] <=> b[1] }.reverse![0,10].join(" ") }</p>"


#Reagan
text_reg = File.read(speeches.at(3).force_encoding('UTF-8')
reg_words = text_reg.downcase.scan(/\w+/)
reg_good = reg_words.select { |word| !stop_words.include?(word) }
reg_sents = lines_reg.gsub(/\s+/, ' ').strip.split(/\.|\?|!/)
reg_sorted = reg_sents.sort_by { |sentence| sentence.length }
reg_split = reg_sorted.length / 3
ideal_reg = reg_sorted.slice(reasplit + 1..-1)
ideal_reg = ideal_reg.select { |ideal| ideal =~ /is|are/ }

puts '<div><h2><a href="~mpernabe/speeches/ronald_reagan_1st.txt">Ronald Reagan Inauguration Speech</h2>'
puts "<h3>STATISTICS</h3>"
puts "<p>Lines &emsp;&emsp; #{text_reg.lines.count}</p>"
puts "<p>Characters &emsp;&emsp; #{text_reg.length}</p>"
puts "<p>Characters (exc. spaces) &emsp;&emsp; #{text_reg.gsub(/\s+/, '').length}</p>"
puts "<p>Word Count &emsp;&emsp; #{text_reg.split.length}</p>"
puts "<p>sentences &emsp;&emsp; #{text_reg.split(/\.|\?|!/).length}</p>"
puts "<p>Paragraphs &emsp;&emsp; #{text_reg.split(/\n\n/).length}</p>"
puts "<p>Sentences / Paragraph &emsp;&emsp; #{text_reg.split(/\.|\?|!/).length / text_reg.split(/\n\n/).length}</p>"
puts "<p> Words / Sentence &emsp;&emsp; #{text_reg.split.length / text_reg.split(/\.|\?|!/).length}</p>"
puts "<p> Non-fluff &emsp;&emsp; #{(reg_good.length.to_f / reg_words.length.to_f * 100).to_i }\%</p><br />"
puts "<h3>ABSTRACT</h3>"
puts "<p>#{ideal_reg.join(". ") }. </p><br />"
puts "<h3>THE TEN MOST COMMON WORDS</h3>"
common_reg = ideal_reg.each_with_object(Hash.new(0)) { |words, num| words[num] += 1}
puts "<p>#{common_reg.sort {|a,b| a[1] <=> b[1] }.reverse![0,10].join(" ") }</p>"

#Kennedy
text_ken = File.read(speeches.at(4)).force_encoding('UTF-8')
ken_words = text_ken.downcase.scan(/\w+/)
ken_good = ken_words.select { |words| !stop_words.include?(words) }
ken_sents = text_ken.gsub(/\s+/, ' ').strip.split(/\.|\?|!/)
ken_sorted = ken_sents.sort_by { |sentence| kensent.length }
ken_split = ken_sorted.length / 3
ideal_ken = ken_sorted.slice(ken_split, ken_split + 1)
ideal_ken = ideal_ken.select { |ideal| ideal =~ /is|are/ }

puts '<div><h2><a href="~mpernabe/speeches/john_kennedy.txt">John Kennedy Inauguration Speech</h2>'
puts "<h3>STATISTICS</h3>"
puts "<p>Lines &emsp;&emsp; #{text_ken.lines.count}</p>"
puts "<p>Characters &emsp;&emsp; #{text_ken.length}</p>"
puts "<p>Characters (exc. spaces) &emsp;&emsp; #{text_ken.gsub(/\s+/, '').length}</p>"
puts "<p>Word Count &emsp;&emsp; #{text_ken.split.length}</p>"
puts "<p>sentences &emsp;&emsp; #{text_ken.split(/\.|\?|!/).length}</p>"
puts "<p>Paragraphs &emsp;&emsp; #{text_ken.split(/\n\n/).length}</p>"
puts "<p>Sentences / Paragraph &emsp;&emsp; #{text_ken.split(/\.|\?|!/).length / text_ken.split(/\n\n/).length}</p>"
puts "<p> Words / Sentence &emsp;&emsp; #{text_ken.split.length / text_ken.split(/\.|\?|!/).length}</p>"
puts "<p> Non-fluff &emsp;&emsp; #{(ken_good.length.to_f / ken_words.length.to_f * 100).to_i }\%</p><br />"
puts "<h3>ABSTRACT</h3>"
puts "<p>#{ideal_ken.join(". ") }. </p><br />"
puts "<h3>THE TEN MOST COMMON WORDS</h3>"
common_ken = ideal_ken.each_with_object(Hash.new(0)) { |words, num| words[num] += 1}
puts "<p>#{common_ken.sort {|a,b| a[1] <=> b[1] }.reverse![0,10].join(" ") }</p>"
"

#HTML ending
puts <<HTML
</body>
</html>
HTML

#Exception will be caught here
rescue Exception => e
   puts "<pre>Stack Trace:"
   puts e.backtrace.join("<br />\n")
   puts "</pre>"
end

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
public_html/cgi-bin/cs132a/lab3.rb:240: syntax error, unexpected tIDENTIFIER, expecting ')'
nix_words = text_nix.downcase.scan(/\w+/)
         ^
public_html/cgi-bin/cs132a/lab3.rb:269: syntax error, unexpected tIDENTIFIER, expecting ')'
reg_words = text_reg.downcase.scan(/\w+/)
         ^
public_html/cgi-bin/cs132a/lab3.rb:333: syntax error, unexpected tLABEL, expecting keyword_do or '{' or '('
   puts "<pre>Stack Trace:"
                          ^
public_html/cgi-bin/cs132a/lab3.rb:334: syntax error, unexpected tREGEXP_BEG, expecting keyword_do or '{' or '('
   puts e.backtrace.join("<br />\n")
                               ^
public_html/cgi-bin/cs132a/lab3.rb:335: unknown regexp options - pr
public_html/cgi-bin/cs132a/lab3.rb:335: unterminated string meets end of file
public_html/cgi-bin/cs132a/lab3.rb:335: syntax error, unexpected $end, expecting keyword_end
