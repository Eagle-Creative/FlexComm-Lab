using System;

namespace FlexComm.ROS.Messages.sensor_msgs
{
    [Serializable]
    public class JointState
    {
        public Header header;
        public string[] name;
        public double[] position;
        public double[] velocity;
        public double[] effort;
    }
}
