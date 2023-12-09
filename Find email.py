
import re
sen1  = 'My email address is sreedeep@gmail.com and my phone number is 9633159946'
regex = '[a-z,0-9]+@gmail.com'
re.findall(regex, sen1)
