# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ece_msgs/ecemsg.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import ece_msgs.msg
import std_msgs.msg

class ecemsg(genpy.Message):
  _md5sum = "7ee37b09982376135f3ec683dcb0f358"
  _type = "ece_msgs/ecemsg"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """Header header
ItsPduHeader its_header
uint16 generation_delta_time # milliseconds since 2004 modulo 2^16

# basic container
BasicContainer basic_container

# Init
Init init

# Insertion
Insertion insertion

# Desinsertion
Desinsertion desinsertion 

# Freinage d'urgence
FreinageUrgence freinage_urgence

# Feu
Feu feu



================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: ece_msgs/ItsPduHeader
uint8 protocol_version
uint8 message_id
uint32 station_id

uint8 MESSAGE_ID_DENM = 1
uint8 MESSAGE_ID_CAM = 2
uint8 MESSAGE_ID_ECE = 8
================================================================================
MSG: ece_msgs/BasicContainer
# ID expediteur
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
uint8 ROAD_SIDE_UNIT = 15
================================================================================
MSG: ece_msgs/Init
# Destination : 8 octets
ReferencePosition destination

# Actual position : 8 octets
ReferencePosition actual_position



================================================================================
MSG: ece_msgs/ReferencePosition
int64 latitude # 0.1 micro degree
int64 longitude # 0.1 micro degree
int32 altitude

int64 LATITUDE_UNAVAILABLE = 900000001
int64 LONGITUDE_UNAVAILABLE = 1800000001
int32 ALTITUDE_UNAVAILABLE = 800001

================================================================================
MSG: ece_msgs/Insertion
# Point d'insertion : 8 octet 
ReferencePosition point_insertion

# Confirmation insertion : 1 octet
bool confirmation_insertion

# Platoon
Platoon platoon
================================================================================
MSG: ece_msgs/Platoon
# ID platoon : 3 bits
uint8 id_platoon

# ID autres véhicules platoon
IDs[] ids 

# Nombre de véhicules : 3 bits
uint8 nombre_vehicules

# Destination : 8 octets
ReferencePosition destination

# Vitesse et interdistance
VitesseInterdistance vitesse_interdistance
================================================================================
MSG: ece_msgs/IDs
uint8 ID
uint8 position
================================================================================
MSG: ece_msgs/VitesseInterdistance
# Vitesse : 6 bits
Speed speed

# Interdistance : 2 bits
uint8 interdistance
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
MSG: ece_msgs/Desinsertion
# Demande de sortie : 1 octet
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
MSG: ece_msgs/FreinageUrgence
# Position P : 2 bits
uint8 position
================================================================================
MSG: ece_msgs/Feu
# Permission de passer le feu : 1 octet
bool permission_feu"""
  __slots__ = ['header','its_header','generation_delta_time','basic_container','init','insertion','desinsertion','freinage_urgence','feu']
  _slot_types = ['std_msgs/Header','ece_msgs/ItsPduHeader','uint16','ece_msgs/BasicContainer','ece_msgs/Init','ece_msgs/Insertion','ece_msgs/Desinsertion','ece_msgs/FreinageUrgence','ece_msgs/Feu']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,its_header,generation_delta_time,basic_container,init,insertion,desinsertion,freinage_urgence,feu

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ecemsg, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.its_header is None:
        self.its_header = ece_msgs.msg.ItsPduHeader()
      if self.generation_delta_time is None:
        self.generation_delta_time = 0
      if self.basic_container is None:
        self.basic_container = ece_msgs.msg.BasicContainer()
      if self.init is None:
        self.init = ece_msgs.msg.Init()
      if self.insertion is None:
        self.insertion = ece_msgs.msg.Insertion()
      if self.desinsertion is None:
        self.desinsertion = ece_msgs.msg.Desinsertion()
      if self.freinage_urgence is None:
        self.freinage_urgence = ece_msgs.msg.FreinageUrgence()
      if self.feu is None:
        self.feu = ece_msgs.msg.Feu()
    else:
      self.header = std_msgs.msg.Header()
      self.its_header = ece_msgs.msg.ItsPduHeader()
      self.generation_delta_time = 0
      self.basic_container = ece_msgs.msg.BasicContainer()
      self.init = ece_msgs.msg.Init()
      self.insertion = ece_msgs.msg.Insertion()
      self.desinsertion = ece_msgs.msg.Desinsertion()
      self.freinage_urgence = ece_msgs.msg.FreinageUrgence()
      self.feu = ece_msgs.msg.Feu()

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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2BIH4B2qi2qi2qi2B().pack(_x.its_header.protocol_version, _x.its_header.message_id, _x.its_header.station_id, _x.generation_delta_time, _x.basic_container.ID_exp, _x.basic_container.ID_dest, _x.basic_container.phase.value, _x.basic_container.station_type.value, _x.init.destination.latitude, _x.init.destination.longitude, _x.init.destination.altitude, _x.init.actual_position.latitude, _x.init.actual_position.longitude, _x.init.actual_position.altitude, _x.insertion.point_insertion.latitude, _x.insertion.point_insertion.longitude, _x.insertion.point_insertion.altitude, _x.insertion.confirmation_insertion, _x.insertion.platoon.id_platoon))
      length = len(self.insertion.platoon.ids)
      buff.write(_struct_I.pack(length))
      for val1 in self.insertion.platoon.ids:
        _x = val1
        buff.write(_get_struct_2B().pack(_x.ID, _x.position))
      _x = self
      buff.write(_get_struct_B2qiH3BHB2qi4B().pack(_x.insertion.platoon.nombre_vehicules, _x.insertion.platoon.destination.latitude, _x.insertion.platoon.destination.longitude, _x.insertion.platoon.destination.altitude, _x.insertion.platoon.vitesse_interdistance.speed.value, _x.insertion.platoon.vitesse_interdistance.speed.confidence, _x.insertion.platoon.vitesse_interdistance.interdistance, _x.desinsertion.demande_sortie, _x.desinsertion.speed.value, _x.desinsertion.speed.confidence, _x.desinsertion.point_sortie.latitude, _x.desinsertion.point_sortie.longitude, _x.desinsertion.point_sortie.altitude, _x.desinsertion.position, _x.desinsertion.confirmation_sortie, _x.freinage_urgence.position, _x.feu.permission_feu))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.its_header is None:
        self.its_header = ece_msgs.msg.ItsPduHeader()
      if self.basic_container is None:
        self.basic_container = ece_msgs.msg.BasicContainer()
      if self.init is None:
        self.init = ece_msgs.msg.Init()
      if self.insertion is None:
        self.insertion = ece_msgs.msg.Insertion()
      if self.desinsertion is None:
        self.desinsertion = ece_msgs.msg.Desinsertion()
      if self.freinage_urgence is None:
        self.freinage_urgence = ece_msgs.msg.FreinageUrgence()
      if self.feu is None:
        self.feu = ece_msgs.msg.Feu()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 74
      (_x.its_header.protocol_version, _x.its_header.message_id, _x.its_header.station_id, _x.generation_delta_time, _x.basic_container.ID_exp, _x.basic_container.ID_dest, _x.basic_container.phase.value, _x.basic_container.station_type.value, _x.init.destination.latitude, _x.init.destination.longitude, _x.init.destination.altitude, _x.init.actual_position.latitude, _x.init.actual_position.longitude, _x.init.actual_position.altitude, _x.insertion.point_insertion.latitude, _x.insertion.point_insertion.longitude, _x.insertion.point_insertion.altitude, _x.insertion.confirmation_insertion, _x.insertion.platoon.id_platoon,) = _get_struct_2BIH4B2qi2qi2qi2B().unpack(str[start:end])
      self.insertion.confirmation_insertion = bool(self.insertion.confirmation_insertion)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.insertion.platoon.ids = []
      for i in range(0, length):
        val1 = ece_msgs.msg.IDs()
        _x = val1
        start = end
        end += 2
        (_x.ID, _x.position,) = _get_struct_2B().unpack(str[start:end])
        self.insertion.platoon.ids.append(val1)
      _x = self
      start = end
      end += 53
      (_x.insertion.platoon.nombre_vehicules, _x.insertion.platoon.destination.latitude, _x.insertion.platoon.destination.longitude, _x.insertion.platoon.destination.altitude, _x.insertion.platoon.vitesse_interdistance.speed.value, _x.insertion.platoon.vitesse_interdistance.speed.confidence, _x.insertion.platoon.vitesse_interdistance.interdistance, _x.desinsertion.demande_sortie, _x.desinsertion.speed.value, _x.desinsertion.speed.confidence, _x.desinsertion.point_sortie.latitude, _x.desinsertion.point_sortie.longitude, _x.desinsertion.point_sortie.altitude, _x.desinsertion.position, _x.desinsertion.confirmation_sortie, _x.freinage_urgence.position, _x.feu.permission_feu,) = _get_struct_B2qiH3BHB2qi4B().unpack(str[start:end])
      self.desinsertion.demande_sortie = bool(self.desinsertion.demande_sortie)
      self.desinsertion.confirmation_sortie = bool(self.desinsertion.confirmation_sortie)
      self.feu.permission_feu = bool(self.feu.permission_feu)
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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2BIH4B2qi2qi2qi2B().pack(_x.its_header.protocol_version, _x.its_header.message_id, _x.its_header.station_id, _x.generation_delta_time, _x.basic_container.ID_exp, _x.basic_container.ID_dest, _x.basic_container.phase.value, _x.basic_container.station_type.value, _x.init.destination.latitude, _x.init.destination.longitude, _x.init.destination.altitude, _x.init.actual_position.latitude, _x.init.actual_position.longitude, _x.init.actual_position.altitude, _x.insertion.point_insertion.latitude, _x.insertion.point_insertion.longitude, _x.insertion.point_insertion.altitude, _x.insertion.confirmation_insertion, _x.insertion.platoon.id_platoon))
      length = len(self.insertion.platoon.ids)
      buff.write(_struct_I.pack(length))
      for val1 in self.insertion.platoon.ids:
        _x = val1
        buff.write(_get_struct_2B().pack(_x.ID, _x.position))
      _x = self
      buff.write(_get_struct_B2qiH3BHB2qi4B().pack(_x.insertion.platoon.nombre_vehicules, _x.insertion.platoon.destination.latitude, _x.insertion.platoon.destination.longitude, _x.insertion.platoon.destination.altitude, _x.insertion.platoon.vitesse_interdistance.speed.value, _x.insertion.platoon.vitesse_interdistance.speed.confidence, _x.insertion.platoon.vitesse_interdistance.interdistance, _x.desinsertion.demande_sortie, _x.desinsertion.speed.value, _x.desinsertion.speed.confidence, _x.desinsertion.point_sortie.latitude, _x.desinsertion.point_sortie.longitude, _x.desinsertion.point_sortie.altitude, _x.desinsertion.position, _x.desinsertion.confirmation_sortie, _x.freinage_urgence.position, _x.feu.permission_feu))
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
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.its_header is None:
        self.its_header = ece_msgs.msg.ItsPduHeader()
      if self.basic_container is None:
        self.basic_container = ece_msgs.msg.BasicContainer()
      if self.init is None:
        self.init = ece_msgs.msg.Init()
      if self.insertion is None:
        self.insertion = ece_msgs.msg.Insertion()
      if self.desinsertion is None:
        self.desinsertion = ece_msgs.msg.Desinsertion()
      if self.freinage_urgence is None:
        self.freinage_urgence = ece_msgs.msg.FreinageUrgence()
      if self.feu is None:
        self.feu = ece_msgs.msg.Feu()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 74
      (_x.its_header.protocol_version, _x.its_header.message_id, _x.its_header.station_id, _x.generation_delta_time, _x.basic_container.ID_exp, _x.basic_container.ID_dest, _x.basic_container.phase.value, _x.basic_container.station_type.value, _x.init.destination.latitude, _x.init.destination.longitude, _x.init.destination.altitude, _x.init.actual_position.latitude, _x.init.actual_position.longitude, _x.init.actual_position.altitude, _x.insertion.point_insertion.latitude, _x.insertion.point_insertion.longitude, _x.insertion.point_insertion.altitude, _x.insertion.confirmation_insertion, _x.insertion.platoon.id_platoon,) = _get_struct_2BIH4B2qi2qi2qi2B().unpack(str[start:end])
      self.insertion.confirmation_insertion = bool(self.insertion.confirmation_insertion)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.insertion.platoon.ids = []
      for i in range(0, length):
        val1 = ece_msgs.msg.IDs()
        _x = val1
        start = end
        end += 2
        (_x.ID, _x.position,) = _get_struct_2B().unpack(str[start:end])
        self.insertion.platoon.ids.append(val1)
      _x = self
      start = end
      end += 53
      (_x.insertion.platoon.nombre_vehicules, _x.insertion.platoon.destination.latitude, _x.insertion.platoon.destination.longitude, _x.insertion.platoon.destination.altitude, _x.insertion.platoon.vitesse_interdistance.speed.value, _x.insertion.platoon.vitesse_interdistance.speed.confidence, _x.insertion.platoon.vitesse_interdistance.interdistance, _x.desinsertion.demande_sortie, _x.desinsertion.speed.value, _x.desinsertion.speed.confidence, _x.desinsertion.point_sortie.latitude, _x.desinsertion.point_sortie.longitude, _x.desinsertion.point_sortie.altitude, _x.desinsertion.position, _x.desinsertion.confirmation_sortie, _x.freinage_urgence.position, _x.feu.permission_feu,) = _get_struct_B2qiH3BHB2qi4B().unpack(str[start:end])
      self.desinsertion.demande_sortie = bool(self.desinsertion.demande_sortie)
      self.desinsertion.confirmation_sortie = bool(self.desinsertion.confirmation_sortie)
      self.feu.permission_feu = bool(self.feu.permission_feu)
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
_struct_2BIH4B2qi2qi2qi2B = None
def _get_struct_2BIH4B2qi2qi2qi2B():
    global _struct_2BIH4B2qi2qi2qi2B
    if _struct_2BIH4B2qi2qi2qi2B is None:
        _struct_2BIH4B2qi2qi2qi2B = struct.Struct("<2BIH4B2qi2qi2qi2B")
    return _struct_2BIH4B2qi2qi2qi2B
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_B2qiH3BHB2qi4B = None
def _get_struct_B2qiH3BHB2qi4B():
    global _struct_B2qiH3BHB2qi4B
    if _struct_B2qiH3BHB2qi4B is None:
        _struct_B2qiH3BHB2qi4B = struct.Struct("<B2qiH3BHB2qi4B")
    return _struct_B2qiH3BHB2qi4B
