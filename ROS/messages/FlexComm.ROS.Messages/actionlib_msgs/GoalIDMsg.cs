using System;

namespace FlexComm.ROS.Messages.actionlib_msgs
{
    [Serializable]
    public class GoalID
    {
        public std_msgs.Time stamp;
        public string id;
    }
}
