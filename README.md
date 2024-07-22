# mock-async-api

`FastAPI`と`httpx`を使って, バックグラウンドで非同期処理をするデモ.

## Usage

1. `$ python main.py`
```
INFO:     Uvicorn running on http://localhost:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [68092] using WatchFiles
INFO:     Started server process [68094]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
2. `$ curl -XPOST 'http://localhost:8000/?task_id=a' && curl -XPOST 'http://localhost:8000/?task_id=b'`
```
INFO:     127.0.0.1:56115 - "POST /?task_id=a HTTP/1.1" 200 OK
INFO:     127.0.0.1:56116 - "POST /?task_id=b HTTP/1.1" 200 OK
INFO:     127.0.0.1:56120 - "POST /second_job?task_id=a HTTP/1.1" 200 OK
INFO:     127.0.0.1:56119 - "POST /first_job?task_id=a HTTP/1.1" 200 OK
INFO:     127.0.0.1:56124 - "POST /second_job?task_id=b HTTP/1.1" 200 OK
INFO:     127.0.0.1:56123 - "POST /first_job?task_id=b HTTP/1.1" 200 OK
INFO:     127.0.0.1:56119 - "POST /third_job?task_id=a HTTP/1.1" 200 OK
INFO:     127.0.0.1:56123 - "POST /third_job?task_id=b HTTP/1.1" 200 OK
```
3. `$ tail -n8 app.log`
```
2024-07-22 19:47:06 task a is scheduled
2024-07-22 19:47:06 task b is scheduled
2024-07-22 19:47:09 Done second job of a
2024-07-22 19:47:09 Done first job of a
2024-07-22 19:47:09 Done first job of b
2024-07-22 19:47:09 Done second job of b
2024-07-22 19:47:12 Done third job of a
2024-07-22 19:47:12 Done third job of b
```