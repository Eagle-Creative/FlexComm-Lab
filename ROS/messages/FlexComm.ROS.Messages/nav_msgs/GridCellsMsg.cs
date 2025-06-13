using System;

namespace FlexComm.ROS.Messages.nav_msgs
{
    [Serializable]
    public class GridCells
    {
        public std_msgs.Header header;
        public float cell_width;
        public float cell_height;
        public geometry_msgs.Point[] cells;
    }
}
