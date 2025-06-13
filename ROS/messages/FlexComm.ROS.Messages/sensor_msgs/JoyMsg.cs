using System;

namespace FlexComm.ROS.Messages.sensor_msgs
{
    [Serializable]
    public class Joy
    {
        public Header header;
        public float[] axes;
        public int[] buttons;
    }
}
