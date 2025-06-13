using System;

namespace FlexComm.ROS.Messages.geometry_msgs
{
    [Serializable]
    public class Accel
    {
        public Vector3 linear;
        public Vector3 angular;
    }
}
