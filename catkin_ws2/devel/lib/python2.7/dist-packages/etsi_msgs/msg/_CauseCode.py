# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from etsi_msgs/CauseCode.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class CauseCode(genpy.Message):
  _md5sum = "fc8877aef6cd5537c1ab4131c260e325"
  _type = "etsi_msgs/CauseCode"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint8 cause_code
uint8 sub_cause_code

uint8 RESERVED = 0
uint8 TRAFFIC_CONDITION = 1
uint8 ACCIDENT = 2
uint8 ROADWORKS = 3
uint8 ADVERSE_WEATHER_CONDITIONS_ADHESION = 4
uint8 HAZARDOUS_LOCATION_SURFACE_CONDITION = 9
uint8 HAZARDOUS_LOCATION_OBSTACLE_ON_THE_ROAD = 10
uint8 HAZARDOUS_LOCATION_ANIMAL_ON_THE_ROAD = 11
uint8 HUMAN_PRESENCE_ON_THE_ROAD = 12
uint8 WRONG_WAY_DRIVING = 14
uint8 RESCUE_AND_RECOVERY_WORK_IN_PROGRESS = 15
uint8 ADVERSE_WEATHER_CONDITIONS_EXTREME_WEATHER_CONDITION = 17
uint8 ADVERSE_WEATHER_CONDITIONS_VISIBILITY = 18
uint8 ADVERSE_WEATHER_CONDITIONS_PRECIPITATION = 19
uint8 SLOW_VEHICLE = 26
uint8 DANGEROUS_END_OF_QUEUE = 27
uint8 VEHICLE_BREAKDOWN = 91
uint8 POST_CRASH = 92
uint8 HUMAN_PROBLEM = 93
uint8 STATIONARY_VEHICLE = 94
uint8 EMERGENCY_VEHICLE_APPROACHING = 95
uint8 HAZARDOUS_LOCATION_DANGEROUS_CURVE = 96
uint8 COLLISION_RISK = 97
uint8 SIGNAL_VIOLATION = 98
uint8 DANGEROUS_SITUATION = 99
"""
  # Pseudo-constants
  RESERVED = 0
  TRAFFIC_CONDITION = 1
  ACCIDENT = 2
  ROADWORKS = 3
  ADVERSE_WEATHER_CONDITIONS_ADHESION = 4
  HAZARDOUS_LOCATION_SURFACE_CONDITION = 9
  HAZARDOUS_LOCATION_OBSTACLE_ON_THE_ROAD = 10
  HAZARDOUS_LOCATION_ANIMAL_ON_THE_ROAD = 11
  HUMAN_PRESENCE_ON_THE_ROAD = 12
  WRONG_WAY_DRIVING = 14
  RESCUE_AND_RECOVERY_WORK_IN_PROGRESS = 15
  ADVERSE_WEATHER_CONDITIONS_EXTREME_WEATHER_CONDITION = 17
  ADVERSE_WEATHER_CONDITIONS_VISIBILITY = 18
  ADVERSE_WEATHER_CONDITIONS_PRECIPITATION = 19
  SLOW_VEHICLE = 26
  DANGEROUS_END_OF_QUEUE = 27
  VEHICLE_BREAKDOWN = 91
  POST_CRASH = 92
  HUMAN_PROBLEM = 93
  STATIONARY_VEHICLE = 94
  EMERGENCY_VEHICLE_APPROACHING = 95
  HAZARDOUS_LOCATION_DANGEROUS_CURVE = 96
  COLLISION_RISK = 97
  SIGNAL_VIOLATION = 98
  DANGEROUS_SITUATION = 99

  __slots__ = ['cause_code','sub_cause_code']
  _slot_types = ['uint8','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       cause_code,sub_cause_code

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CauseCode, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.cause_code is None:
        self.cause_code = 0
      if self.sub_cause_code is None:
        self.sub_cause_code = 0
    else:
      self.cause_code = 0
      self.sub_cause_code = 0

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
      buff.write(_get_struct_2B().pack(_x.cause_code, _x.sub_cause_code))
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
      end += 2
      (_x.cause_code, _x.sub_cause_code,) = _get_struct_2B().unpack(str[start:end])
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
      buff.write(_get_struct_2B().pack(_x.cause_code, _x.sub_cause_code))
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
      end += 2
      (_x.cause_code, _x.sub_cause_code,) = _get_struct_2B().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2B = None
def _get_struct_2B():
    global _struct_2B
    if _struct_2B is None:
        _struct_2B = struct.Struct("<2B")
    return _struct_2B
