from talon import Module

import grpc

from .protos import keymapp_pb2_grpc
from .protos import keymapp_pb2

mod = Module()

previous_layer = 0

def set_layer(layer: int):
    global previous_layer 
    try:
        channel = grpc.insecure_channel("localhost:50051")
        stub = keymapp_pb2_grpc.KeyboardServiceStub(channel)
        old_layer = stub.GetStatus(keymapp_pb2.GetStatusRequest()).connected_keyboard.current_layer
        previous_layer = old_layer
        res = stub.SetLayer(keymapp_pb2.SetLayerRequest(layer=layer))

        print(f"Set layer to {layer}")
    except Exception as e:
        print("Error when setting keymapp layer. Is the keymapp server running?")

def unset_layer(layer: int):
    try:
        channel = grpc.insecure_channel("localhost:50051")
        stub = keymapp_pb2_grpc.KeyboardServiceStub(channel)
        res = stub.UnsetLayer(keymapp_pb2.SetLayerRequest(layer=layer))
        print(f"Unset layer {layer}")
    except Exception as e:
        print("Error when unsetting keymapp layer. Is the keymapp server running?") 
        

def set_previous_layer():
    try:
        channel = grpc.insecure_channel("localhost:50051")
        stub = keymapp_pb2_grpc.KeyboardServiceStub(channel)
        res = stub.SetLayer(keymapp_pb2.SetLayerRequest(layer=previous_layer))
        print(f"Set layer to {previous_layer}")
    except Exception as e:
        print("Error when setting keymapp layer. Is the keymapp server running?")

# --- Implement actions ---
@mod.action_class
class UserActions:
    def set_keymapp_layer(layer: int):
        """Set the keymapp layer"""
        set_layer(layer)

    def unset_keymapp_layer(layer: int):
        """Unset the keymapp layer"""
        unset_layer(layer)
    
    def set_previous_keymapp_layer():
        """Set the keymapp layer to the previous layer"""
        set_previous_layer()