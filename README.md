

# Send message with meshtastic CLI to a port

## Installation

need to have python3


### Download submodule with protobuf

```bash
$ git submodule init
$ git submodule update
```

### Install all python dependency

```bash
$ install.sh
```

### Load python virtual environnement

```bash
$ source ./set_env.sh
```

### Compiling protobuf for python
```bash
$ protoc --python_out=. ./protobufs_ews/meshtastic/ews.proto 
```

