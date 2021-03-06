# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ece_msgs/Desinsertion.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import ece_msgs.msg

class Desinsertion(genpy.Message):
  _md5sum = "289d0b836799889abdfb4fb904e756c7"
  _type = "ece_msgs/Desinsertion"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# Demande de sortie : 1 octet
bool demande_sortie

# Vitesse de sortie : 6 bits 
Speed speed

# Point de sortie : 8 octets
ReferencePosition point_sortie

# Nouvelle position dans P : 2 bits
uint8 position

# Confirmation insertion
bool confirmation_sortie

================================================================================
MSG: ece_msgs/Speed
uint16 value # 0.01 m/s
uint8 confidence # 0.01 m/s

uint16 VALUE_STANDSTILL = 0
uint16 VALUE_ONE_CENTIMETER_PER_SECOND = 1
uint16 VALUE_UNAVAILABLE = 16383

uint8 CONFIDENCE_OUT_OF_RANGE = 126
uint8 CONFIDENCE_UNAVAILABLE = 127

================================================================================
MSG: ece_msgs/ReferencePosition
int64 latitude # 0.1 micro degree
int64 longitude # 0.1 micro degree
int32 altitude

int64 LATITUDE_UNAVAILABLE = 900000001
int64 LONGITUDE_UNAVAILABLE = 1800000001
int32 ALTITUDE_UNAVAILABLE = 800001
"""
  __slots__ = ['demande_sortie','speed','point_sortie','position','confirmation_sortie']
  _slot_types = ['bool','ece_msgs/Speed','ece_msgs/ReferencePosition','uint8','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       demande_sortie,speed,point_sortie,position,confirmation_sortie

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Desinsertion, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.demande_sortie is None:
        self.demande_sortie = False
      if self.speed is None:
        self.speed = ece_msgs.msg.Speed()
      if self.point_sortie is None:
        self.point_sortie = ece_msgs.msg.ReferencePosition()
      if self.position is None:
        self.position = 0
      if self.confirmation_sortie is None:
        self.confirmation_sortie = False
    else:
      self.demande_sortie = False
      self.speed = ece_msgs.msg.Speed()
      self.point_sortie = ece_msgs.msg.ReferencePosition()
      self.position = 0
      self.confirmation_sortie = False

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
      buff.write(_get_struct_BHB2qi2B().pack(_x.demande_sortie, _x.speed.value, _x.speed.confidence, _x.point_sortie.latitude, _x.point_sortie.longitude, _x.point_sortie.altitude, _x.position, _x.confirmation_sortie))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.speed is None:
        self.speed = ece_msgs.msg.Speed()
      if self.point_sortie is None:
        self.point_sortie = ece_msgs.msg.ReferencePosition()
      end = 0
      _x = self
      start = end
      end += 26
      (_x.demande_sortie, _x.speed.value, _x.speed.confidence, _x.point_sortie.latitude, _x.point_sortie.longitude, _x.point_sortie.altitude, _x.position, _x.confirmation_sortie,) = _get_struct_BHB2qi2B().unpack(str[start:end])
      self.demande_sortie = bool(self.demande_sortie)
      self.confirmation_sortie = bool(self.confirmation_sortie)
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
      buff.write(_get_struct_BHB2qi2B().pack(_x.demande_sortie, _x.speed.value, _x.speed.confidence, _x.point_sortie.latitude, _x.point_sortie.longitude, _x.point_sortie.altitude, _x.position, _x.confirmation_sortie))
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
      if self.speed is None:
        self.speed = ece_msgs.msg.Speed()
      if self.point_sortie is None:
        self.point_sortie = ece_msgs.msg.ReferencePosition()
      end = 0
      _x = self
      start = end
      end += 26
      (_x.demande_sortie, _x.speed.value, _x.speed.confidence, _x.point_sortie.latitude, _x.point_sortie.longitude, _x.point_sortie.altitude, _x.position, _x.confirmation_sortie,) = _get_struct_BHB2qi2B().unpack(str[start:end])
      self.demande_sortie = bool(self.demande_sortie)
      self.confirmation_sortie = bool(self.confirmation_sortie)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_BHB2qi2B = None
def _get_struct_BHB2qi2B():
    global _struct_BHB2qi2B
    if _struct_BHB2qi2B is None:
        _struct_BHB2qi2B = struct.Struct("<BHB2qi2B")
    return _struct_BHB2qi2B
