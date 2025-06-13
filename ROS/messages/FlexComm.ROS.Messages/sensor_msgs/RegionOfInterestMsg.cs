using System;

namespace FlexComm.ROS.Messages.sensor_msgs
{
    [Serializable]
    public class RegionOfInterest
    {
        public int x_offset;
        public int y_offset;
        public int height;
        public int width;
        public bool do_rectify;
    }
}
