using System;

namespace FlexComm.ROS.Messages.geometry_msgs
{
    [Serializable]
    public class Wrench
    {
        public Vector3 force;
        public Vector3 torque;
    }
}
