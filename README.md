# connections_async

A demo app showing a async service using quart and some supporting packages

### Requirements

 * Docker CE >= 17.04

### Stack Information

* pypy quart
* tortoise-orm
* mysql
* nginx + hypercorn

**All API calls will go through nginx at http://localhost:5000. All the other services are handled within Docker's internal network and no other ports are exposed to the host machine.**

### Instructions

- Build and kick off all the services with docker-compose.

```
docker-compose up -d --build
```

- Init the database

```
docker-compose exec web python manage.py generate-schemas
```
### Proformance

- Flask WSGI

```
wrk -t10 -c1000 -d10s --latency "http://127.0.0.1:5000/people"   dylan@DESKTOP-R64EE08
Running 10s test @ http://127.0.0.1:5000/people
  10 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.88s     0.00us   1.88s   100.00%
    Req/Sec    54.76     58.83   320.00     85.99%
  Latency Distribution
     50%    1.88s
     75%    1.88s
     90%    1.88s
     99%    1.88s
  1929 requests in 10.02s, 0.89MB read
  Socket errors: connect 0, read 0, write 0, timeout 1928
Requests/sec:    192.46
Transfer/sec:     90.59KB
```

- Quart ASGI

```
wrk -t10 -c1000 -d10s --latency "http://127.0.0.1:5000/people"   dylan@DESKTOP-R64EE08
Running 10s test @ http://127.0.0.1:5000/people
  10 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   813.72ms  769.39ms   1.98s    41.30%
    Req/Sec    62.14     68.30   646.00     89.86%
  Latency Distribution
     50%  632.21ms
     75%    1.68s
     90%    1.79s
     99%    1.90s
  4913 requests in 10.02s, 2.26MB read
  Socket errors: connect 0, read 0, write 0, timeout 1063
Requests/sec:    490.08
Transfer/sec:    230.90KB
```
