using System;

namespace FlexComm.ROS.Messages.geometry_msgs
{
    [Serializable]
    public class WrenchStamped
    {
        public std_msgs.Header header;
        public Wrench wrench;
    }
}
