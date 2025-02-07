# zsa-keymapp-talon

Control your ZSA keyboard (Moonlander / Voyager / Ergodox) using the [Keymapp](https://www.zsa.io/flash) API (Protobuf) in Talon (https://talon.wiki/)

🗣 Say `layer two` to switch to that layer. `layer reset` to be back on the default. Can make your own voice command `layer numbers` or `layer symbols` with ease.

👞 Best enjoyed with a foot pedal ([supported by talon](https://talon.wiki/quickstart/hardware/#foot-pedals
)) to be on a layer while holding the pedal down

# Installation

1. Clone this repo into your talon user folder (`~/AppData/Roaming/talon/user`)

2. Install grpc into your talon virtual environment

```shell
cd ~/AppData/Roaming/talon/venv/3.13/Scripts
pip install grpcio
```

3. Restart Talon

# Usage

Ensure your Keymapp API is enabled in the application,

![](./assets/keymapp-settings.png)

## keymapp.talon file

Say `layer two` to switch to the 2nd layer (layer number 1, 0 is first)

### Making your own talon usage

Trigger the layer change by using the `set_keymapp_layer` function in a .talon file.

Switch between layer 1 and 2 using a foot pedal:

```
deck(pedal_middle:down): user.set_keymapp_layer(1)
deck(pedal_middle:up): user.set_keymapp_layer(0)
```

# Notes

See also https://github.com/ohare93/zsa-keymapp-python/ for a non Talon implementation

## Generating the grpc files

No need to do this, since the generated files are included in this repo. But for the sake of documentation here is how they were generated:

```shell
poetry run python -m grpc.tools.protoc -I. --proto_path . --python_out . --mypy_out . --grpc_python_out . ./protos/*.proto
```

You will also need to install the following, the same way as the `grpcio` package:

```shell
pip install grpcio-tools mypy-protobuf
```

A manual edit was made in the generated `keymapp_pb2_grpc.py` file. Adding `from .` to the import statement of the other generated file on line 6.
