using System;

namespace FlexComm.ROS.Messages.actionlib_msgs
{
    [Serializable]
    public class GoalStatus
    {
        public GoalID goal_id;
        public byte status;
        public string text;
    }
}
