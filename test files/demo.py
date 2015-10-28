__author__ = 'ilu'
import re
text = open('abc.txt').read()
print text
basic_info = re.search('(.*)',text)
print(basic_info)