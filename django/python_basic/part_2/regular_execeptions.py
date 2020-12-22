import re

sample_txt = 'This is a sample test for searching 12345432 no check'

print(type(re.search('a',sample_txt)))

print(re.search('a',sample_txt)) # gives index of first match

print(re.findall('a',sample_txt)) #returns all the matching string

print(re.findall(r'\d+',sample_txt))  #get all the digits