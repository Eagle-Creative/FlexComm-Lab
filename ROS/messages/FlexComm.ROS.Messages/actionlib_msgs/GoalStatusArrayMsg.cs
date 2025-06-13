using System;

namespace FlexComm.ROS.Messages.actionlib_msgs
{
    [Serializable]
    public class GoalStatusArray
    {
        public std_msgs.Header header;
        public GoalStatus[] status_list;
    }
}
