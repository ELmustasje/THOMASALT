import re
import math

navnregex = re.compile(".+", re.DOTALL)

a = navnregex.search("first name thomas \n last name barth")
print(a)
