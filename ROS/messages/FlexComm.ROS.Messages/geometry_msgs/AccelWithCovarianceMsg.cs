using System;

namespace FlexComm.ROS.Messages.geometry_msgs
{
    [Serializable]
    public class AccelWithCovariance
    {
        public Accel accel;
        public double[] covariance;
    }
}
