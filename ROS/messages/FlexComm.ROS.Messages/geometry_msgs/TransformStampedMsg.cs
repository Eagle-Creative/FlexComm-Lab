using System;

namespace FlexComm.ROS.Messages.geometry_msgs
{
    [Serializable]
    public class TransformStamped
    {
        public std_msgs.Header header;
        public string child_frame_id;
        public Transform transform;
    }
}
