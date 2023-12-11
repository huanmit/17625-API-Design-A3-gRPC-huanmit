# 17625-API-Design-A3
This is the repo for 17625 Fall23's assignment.

## 2 Setup
### 2.1 Environment
Build in the virtual environment.
```sh
# perform in Component3
python -m venv grpc_env
source grpc_env/bin/activate
pip install -r requirements.txt
# for exiting the env:
# deactivate
```
### 2.2 Generate gRPC code:
In Component3, define the proto in `protos/reddit.proto` and generate gRPC code using:
```sh
python -m grpc_tools.protoc -I./proto --python_out=./generated --pyi_out=./generated --grpc_python_out=./generated ./proto/reddit.proto
```

### 2.3 Run Server/Client
Run with:
```sh
python assistant/server.py
python assistant/client.py 
```

### 2.4 Run unit tests
Run with server on, then run:
```sh
python assistant/test.py
```