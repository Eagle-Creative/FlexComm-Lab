using System;

namespace FlexComm.ROS.Messages.geometry_msgs
{
    [Serializable]
    public class TwistWithCovariance
    {
        public Twist twist;
        public double[] covariance;
    }
}
