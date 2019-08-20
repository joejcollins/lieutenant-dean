import worker
from tasks import *

RESULT = fetch_data.s(url='http://bees.bagbatch.co.uk/').apply()
print(RESULT.get())

