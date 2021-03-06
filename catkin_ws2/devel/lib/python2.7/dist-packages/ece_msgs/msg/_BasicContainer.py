# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ece_msgs/BasicContainer.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import ece_msgs.msg

class BasicContainer(genpy.Message):
  _md5sum = "b89e5ecc81a0e7b1d5b7bf77ae93b6d4"
  _type = "ece_msgs/BasicContainer"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# ID expediteur
uint8 ID_exp

# ID destinataire
uint8 ID_dest

# Phase de plattoning
Phase phase

# Type de station
StationType station_type
================================================================================
MSG: ece_msgs/Phase
# Phase de plattoning
uint8 value

uint8 INIT = 0
uint8 INSERTION = 1
uint8 DESINSERTION = 2
uint8 FEU = 3
uint8 FREINAGE_URG = 4
================================================================================
MSG: ece_msgs/StationType
uint8 value

uint8 UNKNOWN = 0
uint8 PEDESTRIAN = 1
uint8 CYCLIST = 2
uint8 MOPED = 3
uint8 MOTORCYCLE = 4
uint8 PASSENGER_CAR = 5
uint8 BUS = 6
uint8 LIGHT_TRUCK = 7
uint8 HEAVY_TRUCK = 8
uint8 TRAILER = 9
uint8 SPECIAL_VEHICLE = 10
uint8 TRAM = 11
uint8 ROAD_SIDE_UNIT = 15"""
  __slots__ = ['ID_exp','ID_dest','phase','station_type']
  _slot_types = ['uint8','uint8','ece_msgs/Phase','ece_msgs/StationType']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       ID_exp,ID_dest,phase,station_type

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(BasicContainer, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.ID_exp is None:
        self.ID_exp = 0
      if self.ID_dest is None:
        self.ID_dest = 0
      if self.phase is None:
        self.phase = ece_msgs.msg.Phase()
      if self.station_type is None:
        self.station_type = ece_msgs.msg.StationType()
    else:
      self.ID_exp = 0
      self.ID_dest = 0
      self.phase = ece_msgs.msg.Phase()
      self.station_type = ece_msgs.msg.StationType()

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
      buff.write(_get_struct_4B().pack(_x.ID_exp, _x.ID_dest, _x.phase.value, _x.station_type.value))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.phase is None:
        self.phase = ece_msgs.msg.Phase()
      if self.station_type is None:
        self.station_type = ece_msgs.msg.StationType()
      end = 0
      _x = self
      start = end
      end += 4
      (_x.ID_exp, _x.ID_dest, _x.phase.value, _x.station_type.value,) = _get_struct_4B().unpack(str[start:end])
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
      buff.write(_get_struct_4B().pack(_x.ID_exp, _x.ID_dest, _x.phase.value, _x.station_type.value))
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
      if self.phase is None:
        self.phase = ece_msgs.msg.Phase()
      if self.station_type is None:
        self.station_type = ece_msgs.msg.StationType()
      end = 0
      _x = self
      start = end
      end += 4
      (_x.ID_exp, _x.ID_dest, _x.phase.value, _x.station_type.value,) = _get_struct_4B().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4B = None
def _get_struct_4B():
    global _struct_4B
    if _struct_4B is None:
        _struct_4B = struct.Struct("<4B")
    return _struct_4B
