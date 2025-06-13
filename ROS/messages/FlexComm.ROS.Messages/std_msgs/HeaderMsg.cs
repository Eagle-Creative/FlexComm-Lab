using System;

namespace FlexComm.ROS.Messages.std_msgs
{
    [Serializable]
    public class Header
    {
        public uint seq;
        public Time stamp;
        public string frame_id;
    }
}
