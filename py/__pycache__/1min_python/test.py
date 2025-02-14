import re
text='''
park 010-1234-1234
kim 010-1234-1234
lee 010-1234-1234
'''

modified_text=re.sub(r'(\d{3}-\d{4})-(\d{4})',r'\1-####', text)
print(modified_text)