using System;

namespace FlexComm.ROS.Messages.geometry_msgs
{
    [Serializable]
    public class AccelWithCovarianceStamped
    {
        public std_msgs.Header header;
        public AccelWithCovariance accel;
    }
}
