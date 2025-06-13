using System;

namespace FlexComm.ROS.Messages.geometry_msgs
{
    [Serializable]
    public class PoseWithCovarianceStamped
    {
        public std_msgs.Header header;
        public PoseWithCovariance pose;
    }
}
