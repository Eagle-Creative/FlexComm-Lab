using System;

namespace FlexComm.ROS.Messages.geometry_msgs
{
    [Serializable]
    public class PolygonStamped
    {
        public std_msgs.Header header;
        public Polygon polygon;
    }
}
