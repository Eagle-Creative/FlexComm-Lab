using System;

namespace FlexComm.ROS.Messages.geometry_msgs
{
    [Serializable]
    public class QuaternionStamped
    {
        public std_msgs.Header header;
        public Quaternion quaternion;
    }
}
