# Testing Flask and Celery

Celery tasks are supposed to be asynchronous, so if you put a break point it 

Approach is to run tasks immediately, rather than have an instance of Celery available to run the tasks.
This allows the tasks to be debugged during testing.

Suggested by <https://www.distributedpython.com/2018/05/01/unit-testing-celery-tasks/>.

[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-908a85?logo=gitpod)](https://gitpod.io/#https://github.com/joejcollins/lieutenant-dean)
