import worker
from tasks import *

RESULT = slowly_reverse_string.delay(string="qwerty")

for i in range(1, 20):
    time.sleep(1)
    print("%s %s %s" % (RESULT.status, RESULT.ready(), RESULT.info))


