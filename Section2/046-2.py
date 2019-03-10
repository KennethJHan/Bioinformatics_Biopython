#046-2.py

import re
seq = "11A2TG3TT000AT1A2G"
match = re.findall(r'[a-zA-Z]', seq)
 
if match:
    print(''.join(match))
