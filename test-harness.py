import worker
from tasks import *

#RESULT = fetch_data.signature(url='http://bees.bagbatch.co.uk/').apply()
RESULT = slowly_reverse_string.s(string="qwerty").apply()
print(RESULT.get())

