using System;

namespace FlexComm.ROS.Messages.geometry_msgs
{
    [Serializable]
    public class PoseStamped
    {
        public std_msgs.Header header;
        public Pose pose;
    }
}
