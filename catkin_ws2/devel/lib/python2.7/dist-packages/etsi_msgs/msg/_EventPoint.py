# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from etsi_msgs/EventPoint.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import etsi_msgs.msg

class EventPoint(genpy.Message):
  _md5sum = "b537fe840862e2b80e7cc1e698e9ac33"
  _type = "etsi_msgs/EventPoint"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """DeltaReferencePosition event_position
PathDeltaTime event_delta_time
InformationQuality information_quality

================================================================================
MSG: etsi_msgs/DeltaReferencePosition
int32 delta_latitude # 0.1 micro degree
int32 delta_longitude # 0.1 micro degree
int16 delta_altitude # centimeter

int32 ONE_MICRODEGREE_NORTH = 10
int32 ONE_MICRODEGREE_SOUTH = -10
int32 ONE_MICRODEGREE_EAST = 10
int32 ONE_MICRODEGREE_WEST = -10
int32 ONE_CENTIMETER_UP = 1
int32 ONE_CENTIMETER_DOWN = -1
int32 LATITUDE_UNAVAILABLE = 131072
int32 LONGITUDE_UNAVAILABLE = 131072
int16 ALTITUDE_UNAVAILABLE = 12800

================================================================================
MSG: etsi_msgs/PathDeltaTime
uint16 value # 10 ms

uint16 UNAVAILABLE = 0
uint16 TEN_MILLISECONDS_IN_PAST = 1

================================================================================
MSG: etsi_msgs/InformationQuality
int8 value

int8 UNAVAILABLE = 0
int8 LOWEST = 1
int8 HIGHEST = 7
"""
  __slots__ = ['event_position','event_delta_time','information_quality']
  _slot_types = ['etsi_msgs/DeltaReferencePosition','etsi_msgs/PathDeltaTime','etsi_msgs/InformationQuality']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       event_position,event_delta_time,information_quality

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(EventPoint, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.event_position is None:
        self.event_position = etsi_msgs.msg.DeltaReferencePosition()
      if self.event_delta_time is None:
        self.event_delta_time = etsi_msgs.msg.PathDeltaTime()
      if self.information_quality is None:
        self.information_quality = etsi_msgs.msg.InformationQuality()
    else:
      self.event_position = etsi_msgs.msg.DeltaReferencePosition()
      self.event_delta_time = etsi_msgs.msg.PathDeltaTime()
      self.information_quality = etsi_msgs.msg.InformationQuality()

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
      buff.write(_get_struct_2ihHb().pack(_x.event_position.delta_latitude, _x.event_position.delta_longitude, _x.event_position.delta_altitude, _x.event_delta_time.value, _x.information_quality.value))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.event_position is None:
        self.event_position = etsi_msgs.msg.DeltaReferencePosition()
      if self.event_delta_time is None:
        self.event_delta_time = etsi_msgs.msg.PathDeltaTime()
      if self.information_quality is None:
        self.information_quality = etsi_msgs.msg.InformationQuality()
      end = 0
      _x = self
      start = end
      end += 13
      (_x.event_position.delta_latitude, _x.event_position.delta_longitude, _x.event_position.delta_altitude, _x.event_delta_time.value, _x.information_quality.value,) = _get_struct_2ihHb().unpack(str[start:end])
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
      buff.write(_get_struct_2ihHb().pack(_x.event_position.delta_latitude, _x.event_position.delta_longitude, _x.event_position.delta_altitude, _x.event_delta_time.value, _x.information_quality.value))
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
      if self.event_position is None:
        self.event_position = etsi_msgs.msg.DeltaReferencePosition()
      if self.event_delta_time is None:
        self.event_delta_time = etsi_msgs.msg.PathDeltaTime()
      if self.information_quality is None:
        self.information_quality = etsi_msgs.msg.InformationQuality()
      end = 0
      _x = self
      start = end
      end += 13
      (_x.event_position.delta_latitude, _x.event_position.delta_longitude, _x.event_position.delta_altitude, _x.event_delta_time.value, _x.information_quality.value,) = _get_struct_2ihHb().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2ihHb = None
def _get_struct_2ihHb():
    global _struct_2ihHb
    if _struct_2ihHb is None:
        _struct_2ihHb = struct.Struct("<2ihHb")
    return _struct_2ihHb
