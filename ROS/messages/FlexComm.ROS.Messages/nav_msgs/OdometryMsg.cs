using System;

namespace FlexComm.ROS.Messages.nav_msgs
{
    [Serializable]
    public class Odometry
    {
        public std_msgs.Header header;
        public string child_frame_id;
        public geometry_msgs.PoseWithCovariance pose;
        public geometry_msgs.TwistWithCovariance twist;
    }
}
