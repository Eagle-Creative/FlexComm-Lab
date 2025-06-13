using System;

namespace FlexComm.ROS.Messages.geometry_msgs
{
    [Serializable]
    public class TwistStamped
    {
        public std_msgs.Header header;
        public Twist twist;
    }
}
