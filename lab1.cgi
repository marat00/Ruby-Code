<!DOCTYPE html>
<!-- saved from url=(0047)http://hills.ccsf.cc.ca.us/~dtu/cs132a/lab1.cgi -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>Lab 1 - The String Class</title>
	<meta charset="UTF-8">
	<style type="text/css">
	body
	{
		color: #ffffff;
		background-color: #000000;
		width: 800px;
	}
	</style>
<style type="text/css"></style></head>
<body>

<pre style="white-space: pre-wrap; word-wrap: break-word;">Problem 3.1.1 - Squeeze -------------------------------------------------------------
 this string has leading space and too MANY tabs and sPaCes betweenX
 the indiVidual Words in each Line.X
 each Line ends with a accidentally aDDED X.X
 in this lab you wilL WRITE code that "sAnITizES" this string by normalizingX
 ("normalizing" means capitalizing sentences and setting otherX
 characters to lower case) and removes in the extra spaces between WOrds.X
-------------------------------------------------------------------------------------

Problem 3.1.2 - Downcase ------------------------------------------------------------
               this string has leading space and too    many tabs and spaces betweenx
   the individual words in each line.x
  each line ends with a accidentally  added  x.x
            in this lab you will write code that "sanitizes" this string by normalizingx
   ("normalizing" means   capitalizing sentences   and setting otherx
  characters to lower case)     and removes in       the extra spaces between words.x
-------------------------------------------------------------------------------------

Problem 3.1.3 - Upcase --------------------------------------------------------------
               THIS STRING HAS LEADING SPACE AND TOO    MANY TABS AND SPACES BETWEENX
   THE INDIVIDUAL WORDS IN EACH LINE.X
  EACH LINE ENDS WITH A ACCIDENTALLY  ADDED  X.X
            IN THIS LAB YOU WILL WRITE CODE THAT "SANITIZES" THIS STRING BY NORMALIZINGX
   ("NORMALIZING" MEANS   CAPITALIZING SENTENCES   AND SETTING OTHERX
  CHARACTERS TO LOWER CASE)     AND REMOVES IN       THE EXTRA SPACES BETWEEN WORDS.X
-------------------------------------------------------------------------------------

Problem 3.1.4 - Capitalize ----------------------------------------------------------
               This string has leading space and too    MANY tabs and sPaCes betweenX
   The indiVidual Words in each Line.X
  Each Line ends with a accidentally  aDDED  X.X
            In this lab you wilL WRITE code that "sAnITizES" this string by normalizingX
   ("Normalizing" means   capitalizing sentences   and setting otherX
  Characters to lower case)     and removes in       the extra spaces between WOrds.X
-------------------------------------------------------------------------------------

Problem 3.1.5 - Removing The Ending "X" ---------------------------------------------
               this string has leading space and too    MANY tabs and sPaCes between
   the indiVidual Words in each Line.
  each Line ends with a accidentally  aDDED  X.
            in this lab you wilL WRITE code that "sAnITizES" this string by normalizing
   ("normalizing" means   capitalizing sentences   and setting other
  characters to lower case)     and removes in       the extra spaces between WOrds.
-------------------------------------------------------------------------------------

Problem 3.1.6 - Each_byte -----------------------------------------------------------
----------
C|Dec|Hex
----------
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
t|116|0x74
h|104|0x68
i|105|0x69
s|115|0x73
 | 32|0x20
s|115|0x73
t|116|0x74
r|114|0x72
i|105|0x69
n|110|0x6e
g|103|0x67
 | 32|0x20
h|104|0x68
a| 97|0x61
s|115|0x73
 | 32|0x20
l|108|0x6c
e|101|0x65
a| 97|0x61
d|100|0x64
i|105|0x69
n|110|0x6e
g|103|0x67
 | 32|0x20
s|115|0x73
p|112|0x70
a| 97|0x61
c| 99|0x63
e|101|0x65
 | 32|0x20
a| 97|0x61
n|110|0x6e
d|100|0x64
 | 32|0x20
t|116|0x74
o|111|0x6f
o|111|0x6f
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
M| 77|0x4d
A| 65|0x41
N| 78|0x4e
Y| 89|0x59
 | 32|0x20
t|116|0x74
a| 97|0x61
b| 98|0x62
s|115|0x73
 | 32|0x20
a| 97|0x61
n|110|0x6e
d|100|0x64
 | 32|0x20
s|115|0x73
P| 80|0x50
a| 97|0x61
C| 67|0x43
e|101|0x65
s|115|0x73
 | 32|0x20
b| 98|0x62
e|101|0x65
t|116|0x74
w|119|0x77
e|101|0x65
e|101|0x65
n|110|0x6e
X| 88|0x58

| 10|0x0a
 | 32|0x20
 | 32|0x20
 | 32|0x20
t|116|0x74
h|104|0x68
e|101|0x65
 | 32|0x20
i|105|0x69
n|110|0x6e
d|100|0x64
i|105|0x69
V| 86|0x56
i|105|0x69
d|100|0x64
u|117|0x75
a| 97|0x61
l|108|0x6c
 | 32|0x20
W| 87|0x57
o|111|0x6f
r|114|0x72
d|100|0x64
s|115|0x73
 | 32|0x20
i|105|0x69
n|110|0x6e
 | 32|0x20
e|101|0x65
a| 97|0x61
c| 99|0x63
h|104|0x68
 | 32|0x20
L| 76|0x4c
i|105|0x69
n|110|0x6e
e|101|0x65
.| 46|0x2e
X| 88|0x58

| 10|0x0a
 | 32|0x20
 | 32|0x20
e|101|0x65
a| 97|0x61
c| 99|0x63
h|104|0x68
 | 32|0x20
L| 76|0x4c
i|105|0x69
n|110|0x6e
e|101|0x65
 | 32|0x20
e|101|0x65
n|110|0x6e
d|100|0x64
s|115|0x73
 | 32|0x20
w|119|0x77
i|105|0x69
t|116|0x74
h|104|0x68
 | 32|0x20
a| 97|0x61
 | 32|0x20
a| 97|0x61
c| 99|0x63
c| 99|0x63
i|105|0x69
d|100|0x64
e|101|0x65
n|110|0x6e
t|116|0x74
a| 97|0x61
l|108|0x6c
l|108|0x6c
y|121|0x79
 | 32|0x20
 | 32|0x20
a| 97|0x61
D| 68|0x44
D| 68|0x44
E| 69|0x45
D| 68|0x44
 | 32|0x20
 | 32|0x20
X| 88|0x58
.| 46|0x2e
X| 88|0x58

| 10|0x0a
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
i|105|0x69
n|110|0x6e
 | 32|0x20
t|116|0x74
h|104|0x68
i|105|0x69
s|115|0x73
 | 32|0x20
l|108|0x6c
a| 97|0x61
b| 98|0x62
 | 32|0x20
y|121|0x79
o|111|0x6f
u|117|0x75
 | 32|0x20
w|119|0x77
i|105|0x69
l|108|0x6c
L| 76|0x4c
 | 32|0x20
W| 87|0x57
R| 82|0x52
I| 73|0x49
T| 84|0x54
E| 69|0x45
 | 32|0x20
c| 99|0x63
o|111|0x6f
d|100|0x64
e|101|0x65
 | 32|0x20
t|116|0x74
h|104|0x68
a| 97|0x61
t|116|0x74
 | 32|0x20
"| 34|0x22
s|115|0x73
A| 65|0x41
n|110|0x6e
I| 73|0x49
T| 84|0x54
i|105|0x69
z|122|0x7a
E| 69|0x45
S| 83|0x53
"| 34|0x22
 | 32|0x20
t|116|0x74
h|104|0x68
i|105|0x69
s|115|0x73
 | 32|0x20
s|115|0x73
t|116|0x74
r|114|0x72
i|105|0x69
n|110|0x6e
g|103|0x67
 | 32|0x20
b| 98|0x62
y|121|0x79
 | 32|0x20
n|110|0x6e
o|111|0x6f
r|114|0x72
m|109|0x6d
a| 97|0x61
l|108|0x6c
i|105|0x69
z|122|0x7a
i|105|0x69
n|110|0x6e
g|103|0x67
X| 88|0x58

| 10|0x0a
 | 32|0x20
 | 32|0x20
 | 32|0x20
(| 40|0x28
"| 34|0x22
n|110|0x6e
o|111|0x6f
r|114|0x72
m|109|0x6d
a| 97|0x61
l|108|0x6c
i|105|0x69
z|122|0x7a
i|105|0x69
n|110|0x6e
g|103|0x67
"| 34|0x22
 | 32|0x20
m|109|0x6d
e|101|0x65
a| 97|0x61
n|110|0x6e
s|115|0x73
 | 32|0x20
 | 32|0x20
 | 32|0x20
c| 99|0x63
a| 97|0x61
p|112|0x70
i|105|0x69
t|116|0x74
a| 97|0x61
l|108|0x6c
i|105|0x69
z|122|0x7a
i|105|0x69
n|110|0x6e
g|103|0x67
 | 32|0x20
s|115|0x73
e|101|0x65
n|110|0x6e
t|116|0x74
e|101|0x65
n|110|0x6e
c| 99|0x63
e|101|0x65
s|115|0x73
 | 32|0x20
 | 32|0x20
 | 32|0x20
a| 97|0x61
n|110|0x6e
d|100|0x64
 | 32|0x20
s|115|0x73
e|101|0x65
t|116|0x74
t|116|0x74
i|105|0x69
n|110|0x6e
g|103|0x67
 | 32|0x20
o|111|0x6f
t|116|0x74
h|104|0x68
e|101|0x65
r|114|0x72
X| 88|0x58

| 10|0x0a
 | 32|0x20
 | 32|0x20
c| 99|0x63
h|104|0x68
a| 97|0x61
r|114|0x72
a| 97|0x61
c| 99|0x63
t|116|0x74
e|101|0x65
r|114|0x72
s|115|0x73
 | 32|0x20
t|116|0x74
o|111|0x6f
 | 32|0x20
l|108|0x6c
o|111|0x6f
w|119|0x77
e|101|0x65
r|114|0x72
 | 32|0x20
c| 99|0x63
a| 97|0x61
s|115|0x73
e|101|0x65
)| 41|0x29
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
a| 97|0x61
n|110|0x6e
d|100|0x64
 | 32|0x20
r|114|0x72
e|101|0x65
m|109|0x6d
o|111|0x6f
v|118|0x76
e|101|0x65
s|115|0x73
 | 32|0x20
i|105|0x69
n|110|0x6e
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
t|116|0x74
h|104|0x68
e|101|0x65
 | 32|0x20
e|101|0x65
x|120|0x78
t|116|0x74
r|114|0x72
a| 97|0x61
 | 32|0x20
s|115|0x73
p|112|0x70
a| 97|0x61
c| 99|0x63
e|101|0x65
s|115|0x73
 | 32|0x20
b| 98|0x62
e|101|0x65
t|116|0x74
w|119|0x77
e|101|0x65
e|101|0x65
n|110|0x6e
 | 32|0x20
W| 87|0x57
O| 79|0x4f
r|114|0x72
d|100|0x64
s|115|0x73
.| 46|0x2e
X| 88|0x58

| 10|0x0a
-------------------------------------------------------------------------------------

Problem 3.1.7 - Split ---------------------------------------------------------------
["this", "string", "has", "leading", "space", "and", "too", "MANY", "tabs", "and", "sPaCes", "betweenX", "the", "indiVidual", "Words", "in", "each", "Line.X", "each", "Line", "ends", "with", "a", "accidentally", "aDDED", "X.X", "in", "this", "lab", "you", "wilL", "WRITE", "code", "that", "\"sAnITizES\"", "this", "string", "by", "normalizingX", "(\"normalizing\"", "means", "capitalizing", "sentences", "and", "setting", "otherX", "characters", "to", "lower", "case)", "and", "removes", "in", "the", "extra", "spaces", "between", "WOrds.X"]
-------------------------------------------------------------------------------------

Problem 3.1.8 - Crypt ---------------------------------------------------------------
Encrypted String: aajU7Tjl/tIb2
-------------------------------------------------------------------------------------

Problem 3.1.9 - Replace The Contents Of A String Object -----------------------------
Object ID (Before): 17021700
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
DIVIDNI EHT 
XNEEWTEB SECAPS DNA SBAT YNAM OOT DNA ECAPS GNIDAEL SAH GNIRTS SIHTual Words in each Line.X
  each Line ends with a accidentally  aDDED  X.X
            in this lab you wilL WRITE code that "sAnITizES" this string by normalizingX
   ("normalizing" means   capitalizing sentences   and setting otherX
  characters to lower case)     and removes in       the extra spaces between WOrds.X
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Object ID (After): 17021700
-------------------------------------------------------------------------------------

Problem 3.1.10 - Inspect ------------------------------------------------------------
"DIVIDNI EHT \nXNEEWTEB SECAPS DNA SBAT YNAM OOT DNA ECAPS GNIDAEL SAH GNIRTS SIHTual Words in each Line.X\n  each Line ends with a accidentally  aDDED  X.X\n            in this lab you wilL WRITE code that \"sAnITizES\" this string by normalizingX\n   (\"normalizing\" means   capitalizing sentences   and setting otherX\n  characters to lower case)     and removes in       the extra spaces between WOrds.X\n"
-------------------------------------------------------------------------------------
</pre>



</body></html>