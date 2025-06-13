using System;

namespace FlexComm.ROS.Messages.sensor_msgs
{
    [Serializable]
    public class Image
    {
        public Header header;
        public int height;
        public int width;
        public string encoding;
        public byte is_bigendian;
        public int step;
        public byte[] data;
    }
}
