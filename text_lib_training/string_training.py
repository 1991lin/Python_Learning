#!user/bin/python3
"""this python file is used for
string lib learning
"""
import string
s = 'this is eric from fuJian province'
# print(s)
# print(string.capwords(s))  # capital word

values = {'name': 'eric', 'age': 27}

t = string.Template("""
name            : ${name}
age             : ${test}
""")
try:
	print('TEMPLATE:', t.substitute(values))
except KeyError as err:
	print('Error:', str(err))

print('safe substitute : ', t.safe_substitute(values))

	
# advanced templates example
"""we can define the pattern we like
and then show the template we like"""


class MyTemplate(string.Template):
	delimiter = '%'
	idpattern = '[a-z]+_[a-z]+'
new_template_string = {'name': 'eric', 'age_test': 27}
template_text = """
name is %name
age is %age_test
"""
t = MyTemplate(template_text)
print(t.safe_substitute(new_template_string))
