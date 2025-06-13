using System;

namespace FlexComm.ROS.Messages.sensor_msgs
{
    [Serializable]
    public class CameraInfo
    {
        public Header header;
        public int height;
        public int width;
        public string distortion_model;
        public double[] D;
        public double[] K;
        public double[] R;
        public double[] P;
        public int binning_x;
        public int binning_y;
        public RegionOfInterest roi;
    }
}
