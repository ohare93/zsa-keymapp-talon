from talon import Module

import grpc

from .protos import keymapp_pb2_grpc
from .protos import keymapp_pb2

mod = Module()


def set_layer(layer: int):
    try:
        channel = grpc.insecure_channel("localhost:50051")
        stub = keymapp_pb2_grpc.KeyboardServiceStub(channel)
        res = stub.SetLayer(keymapp_pb2.SetLayerRequest(layer=layer))
        print(f"Set layer to {layer}")
    except Exception as e:
        print("Error when setting keymapp layer. Is the keymapp server running?")


# --- Implement actions ---
@mod.action_class
class UserActions:
    def set_keymapp_layer(layer: int):
        """Set the keymapp layer"""
        set_layer(layer)
