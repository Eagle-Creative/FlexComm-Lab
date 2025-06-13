using System;

namespace FlexComm.ROS.Messages.geometry_msgs
{
    [Serializable]
    public class Pose
    {
        public Point position;
        public Quaternion orientation;
    }
}
