import worker
from tasks import *

RESULT = fetch_data.delay(url='http://bees.bagbatch.co.uk/')
print(RESULT.get())

# for i in range(1, 20):
#     time.sleep(1)
#     print("%s %s" % (RESULT.status, RESULT.ready()))

# print(RESULT.get())
# print(RESULT.get())
# print(RESULT.get())
# print(RESULT.get())
# print(RESULT.get())
# print(RESULT.forget())
