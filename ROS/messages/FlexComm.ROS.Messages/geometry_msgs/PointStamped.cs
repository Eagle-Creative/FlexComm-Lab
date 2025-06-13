using System;

namespace FlexComm.ROS.Messages.geometry_msgs
{
    [Serializable]
    public class PointStamped
    {
        public std_msgs.Header header;
        public Point point;
    }
}
