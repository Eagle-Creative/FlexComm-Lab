using System;

namespace FlexComm.ROS.Messages.sensor_msgs
{
    [Serializable]
    public class BatteryState
    {
        public float voltage;
        public float current;
        public float charge;
        public float capacity;
        public float design_capacity;
        public float percentage;
        public int power_supply_status;
        public int power_supply_health;
        public int power_supply_technology;
        public bool present;
        public float[] cell_voltage;
        public float[] cell_temperature;
        public string location;
        public string serial_number;
    }
}
