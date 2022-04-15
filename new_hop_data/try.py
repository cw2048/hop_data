import re


SSR = 'ATATATGGGCGATATATATCCATATC'
matches=re.findall("((AT){2,})", SSR)
for m in matches:
    print(m)
