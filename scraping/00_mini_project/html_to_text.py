import re





response = \
"<td><b>Legal Name of Business</b></td>\
<td>PULKIT  SHARMA</td>\
<td><b>Trade Name</b></td>\
<td>PULKIT SHARMA AND ASSOCIATES</td>"

response = re.split("<[^<]+?>", response)

#print (type (response))

response_organized = "\n{} : {}\n{} : {}\n\n".format(response[2], response[5], response[8], response[11])

print (response_organized)
