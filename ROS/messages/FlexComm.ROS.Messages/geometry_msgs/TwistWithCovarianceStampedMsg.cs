using System;

namespace FlexComm.ROS.Messages.geometry_msgs
{
    [Serializable]
    public class TwistWithCovarianceStamped
    {
        public std_msgs.Header header;
        public TwistWithCovariance twist;
    }
}
