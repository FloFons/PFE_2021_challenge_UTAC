// Generated by gencpp from file ece_msgs/ItsPduHeader.msg
// DO NOT EDIT!


#ifndef ECE_MSGS_MESSAGE_ITSPDUHEADER_H
#define ECE_MSGS_MESSAGE_ITSPDUHEADER_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ece_msgs
{
template <class ContainerAllocator>
struct ItsPduHeader_
{
  typedef ItsPduHeader_<ContainerAllocator> Type;

  ItsPduHeader_()
    : protocol_version(0)
    , message_id(0)
    , station_id(0)  {
    }
  ItsPduHeader_(const ContainerAllocator& _alloc)
    : protocol_version(0)
    , message_id(0)
    , station_id(0)  {
  (void)_alloc;
    }



   typedef uint8_t _protocol_version_type;
  _protocol_version_type protocol_version;

   typedef uint8_t _message_id_type;
  _message_id_type message_id;

   typedef uint32_t _station_id_type;
  _station_id_type station_id;



  enum {
    MESSAGE_ID_DENM = 1u,
    MESSAGE_ID_CAM = 2u,
    MESSAGE_ID_ECE = 8u,
  };


  typedef boost::shared_ptr< ::ece_msgs::ItsPduHeader_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ece_msgs::ItsPduHeader_<ContainerAllocator> const> ConstPtr;

}; // struct ItsPduHeader_

typedef ::ece_msgs::ItsPduHeader_<std::allocator<void> > ItsPduHeader;

typedef boost::shared_ptr< ::ece_msgs::ItsPduHeader > ItsPduHeaderPtr;
typedef boost::shared_ptr< ::ece_msgs::ItsPduHeader const> ItsPduHeaderConstPtr;

// constants requiring out of line definition

   

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ece_msgs::ItsPduHeader_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ece_msgs::ItsPduHeader_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace ece_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'ece_msgs': ['/home/ppe2021/catkin_ws/src/ece_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::ece_msgs::ItsPduHeader_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ece_msgs::ItsPduHeader_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ece_msgs::ItsPduHeader_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ece_msgs::ItsPduHeader_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ece_msgs::ItsPduHeader_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ece_msgs::ItsPduHeader_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ece_msgs::ItsPduHeader_<ContainerAllocator> >
{
  static const char* value()
  {
    return "11c9ba5f62074a5d8d5f31309d5b72b6";
  }

  static const char* value(const ::ece_msgs::ItsPduHeader_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x11c9ba5f62074a5dULL;
  static const uint64_t static_value2 = 0x8d5f31309d5b72b6ULL;
};

template<class ContainerAllocator>
struct DataType< ::ece_msgs::ItsPduHeader_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ece_msgs/ItsPduHeader";
  }

  static const char* value(const ::ece_msgs::ItsPduHeader_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ece_msgs::ItsPduHeader_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint8 protocol_version\n\
uint8 message_id\n\
uint32 station_id\n\
\n\
uint8 MESSAGE_ID_DENM = 1\n\
uint8 MESSAGE_ID_CAM = 2\n\
uint8 MESSAGE_ID_ECE = 8\n\
";
  }

  static const char* value(const ::ece_msgs::ItsPduHeader_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ece_msgs::ItsPduHeader_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.protocol_version);
      stream.next(m.message_id);
      stream.next(m.station_id);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ItsPduHeader_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ece_msgs::ItsPduHeader_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ece_msgs::ItsPduHeader_<ContainerAllocator>& v)
  {
    s << indent << "protocol_version: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.protocol_version);
    s << indent << "message_id: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.message_id);
    s << indent << "station_id: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.station_id);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ECE_MSGS_MESSAGE_ITSPDUHEADER_H
