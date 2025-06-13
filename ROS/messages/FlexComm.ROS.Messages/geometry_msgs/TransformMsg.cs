using System;

namespace FlexComm.ROS.Messages.geometry_msgs
{
    [Serializable]
    public class Transform
    {
        public Vector3 translation;
        public Quaternion rotation;
    }
}
