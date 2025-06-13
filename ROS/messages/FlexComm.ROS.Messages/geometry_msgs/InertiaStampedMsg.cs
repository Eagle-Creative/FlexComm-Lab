using System;

namespace FlexComm.ROS.Messages.geometry_msgs
{
    [Serializable]
    public class InertiaStamped
    {
        public std_msgs.Header header;
        public Inertia inertia;
    }
}
