// Generated by gencpp from file etsi_msgs/YawRate.msg
// DO NOT EDIT!


#ifndef ETSI_MSGS_MESSAGE_YAWRATE_H
#define ETSI_MSGS_MESSAGE_YAWRATE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <etsi_msgs/plugin/YawRate.h>

namespace etsi_msgs
{
template <class ContainerAllocator>
struct YawRate_
{
  typedef YawRate_<ContainerAllocator> Type;

#ifdef ETSI_MSGS_MESSAGE_YAWRATE_PLUGIN_CONSTRUCTOR
  ETSI_MSGS_MESSAGE_YAWRATE_PLUGIN_CONSTRUCTOR
#else
  YawRate_()
    : value(0)
    , confidence(0)  {
    }
  YawRate_(const ContainerAllocator& _alloc)
    : value(0)
    , confidence(0)  {
  (void)_alloc;
    }

#endif


   typedef int16_t _value_type;
  _value_type value;

   typedef uint8_t _confidence_type;
  _confidence_type confidence;



  enum {
    VALUE_UNAVAILABLE = 32767,
    CONFIDENCE_0DOT01_DEGSEC = 0u,
    CONFIDENCE_0DOT05_DEGSEC = 1u,
    CONFIDENCE_0DOT1_DEGSEC = 2u,
    CONFIDENCE_1_DEGSEC = 3u,
    CONFIDENCE_5_DEGSEC = 4u,
    CONFIDENCE_10_DEGSEC = 5u,
    CONFIDENCE_100_DEGSEC = 6u,
    CONFIDENCE_OUT_OF_RANGE = 7u,
    CONFIDENCE_UNAVAILABLE = 8u,
  };


  typedef boost::shared_ptr< ::etsi_msgs::YawRate_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::etsi_msgs::YawRate_<ContainerAllocator> const> ConstPtr;

#ifdef ETSI_MSGS_MESSAGE_YAWRATE_PLUGIN_CLASS_BODY
  ETSI_MSGS_MESSAGE_YAWRATE_PLUGIN_CLASS_BODY
#endif
}; // struct YawRate_

typedef ::etsi_msgs::YawRate_<std::allocator<void> > YawRate;

typedef boost::shared_ptr< ::etsi_msgs::YawRate > YawRatePtr;
typedef boost::shared_ptr< ::etsi_msgs::YawRate const> YawRateConstPtr;

// constants requiring out of line definition

   

   

   

   

   

   

   

   

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::etsi_msgs::YawRate_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::etsi_msgs::YawRate_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace etsi_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'etsi_msgs': ['/home/ppe2021/catkin_ws/src/etsi_msgs/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::etsi_msgs::YawRate_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::etsi_msgs::YawRate_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::etsi_msgs::YawRate_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::etsi_msgs::YawRate_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::etsi_msgs::YawRate_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::etsi_msgs::YawRate_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::etsi_msgs::YawRate_<ContainerAllocator> >
{
  static const char* value()
  {
    return "dca9682f2a1621772f3f01aff9d9e072";
  }

  static const char* value(const ::etsi_msgs::YawRate_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xdca9682f2a162177ULL;
  static const uint64_t static_value2 = 0x2f3f01aff9d9e072ULL;
};

template<class ContainerAllocator>
struct DataType< ::etsi_msgs::YawRate_<ContainerAllocator> >
{
  static const char* value()
  {
    return "etsi_msgs/YawRate";
  }

  static const char* value(const ::etsi_msgs::YawRate_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::etsi_msgs::YawRate_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int16 value # 0.01 degree/s\n\
uint8 confidence\n\
\n\
int16 VALUE_UNAVAILABLE = 32767\n\
\n\
uint8 CONFIDENCE_0DOT01_DEGSEC = 0\n\
uint8 CONFIDENCE_0DOT05_DEGSEC = 1\n\
uint8 CONFIDENCE_0DOT1_DEGSEC = 2\n\
uint8 CONFIDENCE_1_DEGSEC = 3\n\
uint8 CONFIDENCE_5_DEGSEC = 4\n\
uint8 CONFIDENCE_10_DEGSEC = 5\n\
uint8 CONFIDENCE_100_DEGSEC = 6\n\
uint8 CONFIDENCE_OUT_OF_RANGE = 7\n\
uint8 CONFIDENCE_UNAVAILABLE = 8\n\
";
  }

  static const char* value(const ::etsi_msgs::YawRate_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

#ifdef ETSI_MSGS_MESSAGE_YAWRATE_PLUGIN_SERIALIZER
  ETSI_MSGS_MESSAGE_YAWRATE_PLUGIN_SERIALIZER
#else
  template<class ContainerAllocator> struct Serializer< ::etsi_msgs::YawRate_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.value);
      stream.next(m.confidence);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct YawRate_
#endif

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

#ifdef ETSI_MSGS_MESSAGE_YAWRATE_PLUGIN_PRINTER
  ETSI_MSGS_MESSAGE_YAWRATE_PLUGIN_PRINTER
#else
template<class ContainerAllocator>
struct Printer< ::etsi_msgs::YawRate_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::etsi_msgs::YawRate_<ContainerAllocator>& v)
  {
    s << indent << "value: ";
    Printer<int16_t>::stream(s, indent + "  ", v.value);
    s << indent << "confidence: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.confidence);
  }
};
#endif

} // namespace message_operations
} // namespace ros

#endif // ETSI_MSGS_MESSAGE_YAWRATE_H
