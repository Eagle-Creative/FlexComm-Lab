using System;

namespace FlexComm.ROS.Messages.geometry_msgs
{
    [Serializable]
    public class PoseWithCovariance
    {
        public Pose pose;
        public double[] covariance;
    }
}
