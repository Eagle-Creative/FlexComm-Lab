using System;

namespace FlexComm.ROS.Messages.std_msgs
{
    [Serializable]
    public class MultiArrayDimension
    {
        public string label;
        public uint size;
        public uint stride;
    }
}
