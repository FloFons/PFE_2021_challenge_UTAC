# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from etsi_msgs/Altitude.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Altitude(genpy.Message):
  _md5sum = "968c3c0b85fd51b834ff2ab741786e5b"
  _type = "etsi_msgs/Altitude"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """int32 value # 0.01 meter
uint8 confidence

int32 VALUE_REFERENCE_ELLIPSOID_SURFACE = 0
int32 VALUE_ONE_CENTIMETER = 1
int32 VALUE_UNAVAILABLE = 800001

uint8 CONFIDENCE_1CM = 0
uint8 CONFIDENCE_2CM = 1
uint8 CONFIDENCE_5CM = 2
uint8 CONFIDENCE_10CM = 3
uint8 CONFIDENCE_20CM = 4
uint8 CONFIDENCE_50CM = 5
uint8 CONFIDENCE_1M = 6
uint8 CONFIDENCE_2M = 7
uint8 CONFIDENCE_5M = 8
uint8 CONFIDENCE_10M = 9
uint8 CONFIDENCE_20M = 10
uint8 CONFIDENCE_50M = 11
uint8 CONFIDENCE_100M = 12
uint8 CONFIDENCE_200M = 13
uint8 CONFIDENCE_OUT_OF_RANGE = 14
uint8 CONFIDENCE_UNAVAILABLE = 15
"""
  # Pseudo-constants
  VALUE_REFERENCE_ELLIPSOID_SURFACE = 0
  VALUE_ONE_CENTIMETER = 1
  VALUE_UNAVAILABLE = 800001
  CONFIDENCE_1CM = 0
  CONFIDENCE_2CM = 1
  CONFIDENCE_5CM = 2
  CONFIDENCE_10CM = 3
  CONFIDENCE_20CM = 4
  CONFIDENCE_50CM = 5
  CONFIDENCE_1M = 6
  CONFIDENCE_2M = 7
  CONFIDENCE_5M = 8
  CONFIDENCE_10M = 9
  CONFIDENCE_20M = 10
  CONFIDENCE_50M = 11
  CONFIDENCE_100M = 12
  CONFIDENCE_200M = 13
  CONFIDENCE_OUT_OF_RANGE = 14
  CONFIDENCE_UNAVAILABLE = 15

  __slots__ = ['value','confidence']
  _slot_types = ['int32','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       value,confidence

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Altitude, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.value is None:
        self.value = 0
      if self.confidence is None:
        self.confidence = 0
    else:
      self.value = 0
      self.confidence = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_iB().pack(_x.value, _x.confidence))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 5
      (_x.value, _x.confidence,) = _get_struct_iB().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_iB().pack(_x.value, _x.confidence))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 5
      (_x.value, _x.confidence,) = _get_struct_iB().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_iB = None
def _get_struct_iB():
    global _struct_iB
    if _struct_iB is None:
        _struct_iB = struct.Struct("<iB")
    return _struct_iB
