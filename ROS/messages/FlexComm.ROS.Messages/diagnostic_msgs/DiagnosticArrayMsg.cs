using System;

namespace FlexComm.ROS.Messages.diagnostic_msgs
{
    [Serializable]
    public class DiagnosticArray
    {
        public std_msgs.Header header;
        public DiagnosticStatus[] status;
    }
}
