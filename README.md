# Python Web Framework Simple Benchmark

###### Test Python Webframework Async and Sync

## Simple Test Flow

- on server side, add 2 seconds sleep before return the response
- use `wrk` for testing the API: `wrk -t5 -c400 -d30s --timeout 3 http://localhost:8000/`
- the server will run using gunicorn with settings 1 worker, 1 threads, 3s timeout and for ASGI type will use `Uvicorn`.<br/>
  command: `gunicorn -w 1 --threads 1 --timeout 3 --worker-class uvicorn.workers.UvicornWorker`
- Tested on MBP - Processor i9 and RAM 16 GB

# Results

#### FastAPI (ASGI)

```
Running 30s test @ http://localhost:8000/
  5 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     2.01s     7.33ms   2.04s    90.30%
    Req/Sec   136.37    158.18   578.00     85.31%
  5600 requests in 30.07s, 776.56KB read
  Socket errors: connect 0, read 253, write 0, timeout 0
Requests/sec:    186.22
Transfer/sec:     25.82KB
```

#### Sanic (ASGI)

```
Sanic ASGI
Running 30s test @ http://localhost:8000/
  5 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     2.01s     6.30ms   2.04s    92.39%
    Req/Sec   107.40    140.58   509.00     85.89%
  5623 requests in 30.09s, 0.86MB read
  Socket errors: connect 0, read 261, write 0, timeout 0
Requests/sec:    186.88
Transfer/sec:     29.38KB
```

#### Falcon (ASGI)

```
Running 30s test @ http://localhost:8000/
  5 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     2.01s     5.28ms   2.03s    93.29%
    Req/Sec   110.30    132.11   542.00     83.89%
  5619 requests in 30.10s, 784.68KB read
  Socket errors: connect 0, read 254, write 0, timeout 0
Requests/sec:    186.71
Transfer/sec:     26.07KB
```

#### Django (ASGI)

```
Running 30s test @ http://localhost:8000/
  5 threads and 400 connections

  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     2.12s    84.83ms   2.31s    66.40%
    Req/Sec    82.06     87.30   509.00     84.09%
  5363 requests in 30.07s, 1.17MB read
  Socket errors: connect 0, read 257, write 0, timeout 0
Requests/sec:    178.34
Transfer/sec:     39.88KB
```

#### Falcon

```
Running 30s test @ http://localhost:8000/
  5 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     2.02s     0.00us   2.02s   100.00%
    Req/Sec     0.00      0.00     0.00    100.00%
  15 requests in 30.10s, 2.39KB read
  Socket errors: connect 0, read 653, write 0, timeout 14
Requests/sec:      0.50
Transfer/sec:      81.24B
```

#### Flask (ASGI)

Using above gunicorn command with Uvicorn its not working, so I follow the [documentation](https://flask.palletsprojects.com/en/2.0.x/deploying/asgi/) and use `Hypercorn`.<br/>
run server command: `hypercorn -w 1 app:asgi_app`
<br/>the result is quite suprising because it's the same as without using any ASGI (not quite sure what's wrong for this case) 🤔🤔🤔🤔

```
Flask ASGI
Running 30s test @ http://localhost:8000/
  5 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     2.03s     0.00us   2.03s   100.00%
    Req/Sec     0.00      0.00     0.00    100.00%
  14 requests in 30.07s, 2.01KB read
  Socket errors: connect 0, read 353, write 0, timeout 13
Requests/sec:      0.47
Transfer/sec:      68.44B
```

#### Flask

```
Running 30s test @ http://localhost:8000/
  5 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     2.56s     0.00us   2.56s   100.00%
    Req/Sec     0.00      0.00     0.00    100.00%
  14 requests in 30.03s, 2.23KB read
  Socket errors: connect 0, read 735, write 1, timeout 13
Requests/sec:      0.47
Transfer/sec:      75.98B
```

## Conclusion

Python Web Framework with `ASGI` will have ability to handle more requests
