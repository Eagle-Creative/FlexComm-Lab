using System;

namespace FlexComm.ROS.Messages.nav_msgs
{
    [Serializable]
    public class MapMetaData
    {
        public std_msgs.Time map_load_time;
        public float resolution;
        public int width;
        public int height;
        public geometry_msgs.Pose origin;
    }
}
