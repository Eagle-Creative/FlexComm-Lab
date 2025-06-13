using System;

namespace FlexComm.ROS.Messages.nav_msgs
{
    [Serializable]
    public class OccupancyGrid
    {
        public std_msgs.Header header;
        public MapMetaData info;
        public sbyte[] data;
    }
}
