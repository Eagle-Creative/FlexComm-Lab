using System;

namespace FlexComm.ROS.Messages.nav_msgs
{
    [Serializable]
    public class Path
    {
        public std_msgs.Header header;
        public geometry_msgs.PoseStamped[] poses;
    }
}
