using System;

namespace FlexComm.ROS.Messages.geometry_msgs
{
    [Serializable]
    public class Inertia
    {
        public double m;
        public Vector3 com;
        public double ixx;
        public double ixy;
        public double ixz;
        public double iyy;
        public double iyz;
        public double izz;
    }
}
