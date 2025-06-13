using System;

namespace FlexComm.ROS.Messages.diagnostic_msgs
{
    [Serializable]
    public class DiagnosticStatus
    {
        public byte level;
        public string name;
        public string message;
        public string hardware_id;
        public KeyValue[] values;
    }
}
