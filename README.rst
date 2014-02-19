Lex
===

API for recommending news using content-based algorithms.


Try it
------

http://lex.cloud.tsuru.io/


How it works
------------

Currently Lex is a mock.


Success example
...............

::

    $ curl -i -X POST "http://lex.cloud.globoi.com/recommendation" -d  '{"userId": 1234, "userProvider": 2, "excludeIds": [123,5235,123], "dateStart": "1997-07-16T19:20:30.45+01:00", "dateEnd": "1997-07-16T19:20:30.45+01:00", "product":  "mobile", "limit": 2}'

    HTTP/1.1 200 OK
    date: Wed, 19 Feb 2014 13:17:01 GMT
    access-control-allow-origin: *
    content-type: text/html; charset=UTF-8
    content-length: 148
    server: TornadoServer/3.2
    connection: keep-alive

    [{"score":0.999,"documentId":6116038798098712381},{"score":0.666,"documentId":6502978799245377158},{"score":0.333,"documentId":5412347350701788586}]


Failure example
...............

::

    $ curl -i -X POST "http://lex.cloud.globoi.com/recommendation" -d "{}"

    HTTP/1.1 400 Bad Request
    date: Wed, 19 Feb 2014 13:16:05 GMT
    access-control-allow-origin: *
    content-type: application/json; charset=UTF-8
    content-length: 144
    server: TornadoServer/3.2
    connection: keep-alive

    {"error": "Expected the following keys: ['dateEnd', 'dateStart', 'excludeIds', 'limit', 'product', 'userId', 'userProvider'], but received: []"}(venus3)tati@tuxy ~/semrec/venus (master)


Healthcheck
...........

::

    $ curl -i -X GET "http://lex.cloud.globoi.com/healthcheck"

    HTTP/1.1 200 OK
    date: Wed, 19 Feb 2014 21:17:25 GMT
    content-length: 7
    etag: "451860c9eea89417e8c5baf88501beb03c8199f1"
    content-type: text/html; charset=UTF-8
    server: TornadoServer/3.2
    connection: keep-alive

    Atchim!


Version
.......

::

    $ curl -i -X GET "http://lex.cloud.globoi.com/version"

    HTTP/1.1 200 OK
    date: Wed, 19 Feb 2014 21:17:25 GMT
    content-length: 7
    etag: "451860c9eea89417e8c5baf88501beb03c8199f1"
    content-type: text/html; charset=UTF-8
    server: TornadoServer/3.2
    connection: keep-alive

    0.0.1

How to run
----------

In order to install dependencies and run the project: ::

    make setup
    make run


Check if service is running: ::

    curl http://0.0.0.0:8888/healthcheck

Is supposed to return ::

    Atchim!


How to run the tests
--------------------

We try hard to keep coverage to 100%, using unit tests whenever possible: ::

    make tests


Contributing
------------

Check if the style of the code is as expected: ::

    make style

And don't forget to provide tests in your patch! ;)
