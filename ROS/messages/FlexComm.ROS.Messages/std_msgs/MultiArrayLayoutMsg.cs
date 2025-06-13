using System;

namespace FlexComm.ROS.Messages.std_msgs
{
    [Serializable]
    public class MultiArrayLayout
    {
        public MultiArrayDimension[] dim;
        public uint data_offset;
    }
}
