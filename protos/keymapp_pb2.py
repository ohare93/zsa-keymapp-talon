# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/keymapp.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14protos/keymapp.proto\x12\x03\x61pi\"C\n\x08Keyboard\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x15\n\rfriendly_name\x18\x02 \x01(\t\x12\x14\n\x0cis_connected\x18\x03 \x01(\x08\"[\n\x11\x43onnectedKeyboard\x12\x15\n\rfriendly_name\x18\x01 \x01(\t\x12\x18\n\x10\x66irmware_version\x18\x02 \x01(\t\x12\x15\n\rcurrent_layer\x18\x03 \x01(\x05\"\x12\n\x10GetStatusRequest\"]\n\x0eGetStatusReply\x12\x17\n\x0fkeymapp_version\x18\x01 \x01(\t\x12\x32\n\x12\x63onnected_keyboard\x18\x02 \x01(\x0b\x32\x16.api.ConnectedKeyboard\"\x15\n\x13GetKeyboardsRequest\"5\n\x11GetKeyboardsReply\x12 \n\tkeyboards\x18\x01 \x03(\x0b\x32\r.api.Keyboard\"\x1b\n\x19\x43onnectAnyKeyboardRequest\"$\n\x16\x43onnectKeyboardRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"\'\n\x14\x43onnectKeyboardReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x1b\n\x19\x44isconnectKeyboardRequest\"*\n\x17\x44isconnectKeyboardReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\" \n\x0fSetLayerRequest\x12\r\n\x05layer\x18\x01 \x01(\x05\" \n\rSetLayerReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\"Z\n\x10SetRGBLedRequest\x12\x0b\n\x03led\x18\x01 \x01(\x05\x12\x0b\n\x03red\x18\x02 \x01(\x05\x12\r\n\x05green\x18\x03 \x01(\x05\x12\x0c\n\x04\x62lue\x18\x04 \x01(\x05\x12\x0f\n\x07sustain\x18\x05 \x01(\x05\"!\n\x0eSetRGBLedReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\"M\n\x10SetRGBAllRequest\x12\x0b\n\x03red\x18\x01 \x01(\x05\x12\r\n\x05green\x18\x02 \x01(\x05\x12\x0c\n\x04\x62lue\x18\x03 \x01(\x05\x12\x0f\n\x07sustain\x18\x04 \x01(\x05\"!\n\x0eSetRGBAllReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\"?\n\x13SetStatusLedRequest\x12\x0b\n\x03led\x18\x01 \x01(\x05\x12\n\n\x02on\x18\x02 \x01(\x08\x12\x0f\n\x07sustain\x18\x03 \x01(\x05\"$\n\x11SetStatusLedReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x1b\n\x19IncreaseBrightnessRequest\"\x1b\n\x19\x44\x65\x63reaseBrightnessRequest\"(\n\x15\x42rightnessUpdateReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\xda\x06\n\x0fKeyboardService\x12\x39\n\tGetStatus\x12\x15.api.GetStatusRequest\x1a\x13.api.GetStatusReply\"\x00\x12\x42\n\x0cGetKeyboards\x12\x18.api.GetKeyboardsRequest\x1a\x16.api.GetKeyboardsReply\"\x00\x12K\n\x0f\x43onnectKeyboard\x12\x1b.api.ConnectKeyboardRequest\x1a\x19.api.ConnectKeyboardReply\"\x00\x12Q\n\x12\x43onnectAnyKeyboard\x12\x1e.api.ConnectAnyKeyboardRequest\x1a\x19.api.ConnectKeyboardReply\"\x00\x12T\n\x12\x44isconnectKeyboard\x12\x1e.api.DisconnectKeyboardRequest\x1a\x1c.api.DisconnectKeyboardReply\"\x00\x12\x36\n\x08SetLayer\x12\x14.api.SetLayerRequest\x1a\x12.api.SetLayerReply\"\x00\x12\x38\n\nUnsetLayer\x12\x14.api.SetLayerRequest\x1a\x12.api.SetLayerReply\"\x00\x12\x39\n\tSetRGBLed\x12\x15.api.SetRGBLedRequest\x1a\x13.api.SetRGBLedReply\"\x00\x12\x39\n\tSetRGBAll\x12\x15.api.SetRGBAllRequest\x1a\x13.api.SetRGBAllReply\"\x00\x12\x42\n\x0cSetStatusLed\x12\x18.api.SetStatusLedRequest\x1a\x16.api.SetStatusLedReply\"\x00\x12R\n\x12IncreaseBrightness\x12\x1e.api.IncreaseBrightnessRequest\x1a\x1a.api.BrightnessUpdateReply\"\x00\x12R\n\x12\x44\x65\x63reaseBrightness\x12\x1e.api.DecreaseBrightnessRequest\x1a\x1a.api.BrightnessUpdateReply\"\x00\x42\x1fZ\x1agithub.com/zsa/keymapp/api\x90\x01\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.keymapp_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\032github.com/zsa/keymapp/api\220\001\001'
  _globals['_KEYBOARD']._serialized_start=29
  _globals['_KEYBOARD']._serialized_end=96
  _globals['_CONNECTEDKEYBOARD']._serialized_start=98
  _globals['_CONNECTEDKEYBOARD']._serialized_end=189
  _globals['_GETSTATUSREQUEST']._serialized_start=191
  _globals['_GETSTATUSREQUEST']._serialized_end=209
  _globals['_GETSTATUSREPLY']._serialized_start=211
  _globals['_GETSTATUSREPLY']._serialized_end=304
  _globals['_GETKEYBOARDSREQUEST']._serialized_start=306
  _globals['_GETKEYBOARDSREQUEST']._serialized_end=327
  _globals['_GETKEYBOARDSREPLY']._serialized_start=329
  _globals['_GETKEYBOARDSREPLY']._serialized_end=382
  _globals['_CONNECTANYKEYBOARDREQUEST']._serialized_start=384
  _globals['_CONNECTANYKEYBOARDREQUEST']._serialized_end=411
  _globals['_CONNECTKEYBOARDREQUEST']._serialized_start=413
  _globals['_CONNECTKEYBOARDREQUEST']._serialized_end=449
  _globals['_CONNECTKEYBOARDREPLY']._serialized_start=451
  _globals['_CONNECTKEYBOARDREPLY']._serialized_end=490
  _globals['_DISCONNECTKEYBOARDREQUEST']._serialized_start=492
  _globals['_DISCONNECTKEYBOARDREQUEST']._serialized_end=519
  _globals['_DISCONNECTKEYBOARDREPLY']._serialized_start=521
  _globals['_DISCONNECTKEYBOARDREPLY']._serialized_end=563
  _globals['_SETLAYERREQUEST']._serialized_start=565
  _globals['_SETLAYERREQUEST']._serialized_end=597
  _globals['_SETLAYERREPLY']._serialized_start=599
  _globals['_SETLAYERREPLY']._serialized_end=631
  _globals['_SETRGBLEDREQUEST']._serialized_start=633
  _globals['_SETRGBLEDREQUEST']._serialized_end=723
  _globals['_SETRGBLEDREPLY']._serialized_start=725
  _globals['_SETRGBLEDREPLY']._serialized_end=758
  _globals['_SETRGBALLREQUEST']._serialized_start=760
  _globals['_SETRGBALLREQUEST']._serialized_end=837
  _globals['_SETRGBALLREPLY']._serialized_start=839
  _globals['_SETRGBALLREPLY']._serialized_end=872
  _globals['_SETSTATUSLEDREQUEST']._serialized_start=874
  _globals['_SETSTATUSLEDREQUEST']._serialized_end=937
  _globals['_SETSTATUSLEDREPLY']._serialized_start=939
  _globals['_SETSTATUSLEDREPLY']._serialized_end=975
  _globals['_INCREASEBRIGHTNESSREQUEST']._serialized_start=977
  _globals['_INCREASEBRIGHTNESSREQUEST']._serialized_end=1004
  _globals['_DECREASEBRIGHTNESSREQUEST']._serialized_start=1006
  _globals['_DECREASEBRIGHTNESSREQUEST']._serialized_end=1033
  _globals['_BRIGHTNESSUPDATEREPLY']._serialized_start=1035
  _globals['_BRIGHTNESSUPDATEREPLY']._serialized_end=1075
  _globals['_KEYBOARDSERVICE']._serialized_start=1078
  _globals['_KEYBOARDSERVICE']._serialized_end=1936
_builder.BuildServices(DESCRIPTOR, 'protos.keymapp_pb2', _globals)
# @@protoc_insertion_point(module_scope)
