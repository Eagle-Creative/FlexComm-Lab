# FlexComm-Lab

**FlexComm-Lab** is the official open-source companion toolkit to the [FlexComm Communication Framework for Unity](https://assetstore.unity.com/packages/tools/network/flexcomm-communication-framework-for-unity-XXXXX). It provides standalone tools, protocol simulators, and integration examples to support development, testing, and debugging of communication pipelines outside the Unity environment.

---

## 🔍 What is FlexComm-Lab?

FlexComm-Lab is designed to accelerate the development and validation of applications that use FlexComm for external device and service integration. It enables you to prototype and test MQTT, REST, UDP, TCP, and Serial communication independently—before integrating into Unity.

Whether you're building robotics systems, digital twins, industrial interfaces, or academic prototypes, FlexComm-Lab helps you streamline your communication pipeline and verify data exchange logic in isolation.

---

## ✨ Features

- ✅ **Standalone MQTT client** (supports v3.1.1 and v5.0)
- ✅ **UDP and TCP simulators** with test message broadcasting
- ✅ **REST test endpoints and client scripts**
- ✅ **Serial port tester** for COM communication (Windows/Linux/macOS)
- ✅ **Message validation and logging tools**
- ✅ **Example JSON schemas and data payloads**
- ✅ **Cross-platform Python and C# utilities**
- ✅ **Compatible with FlexComm’s internal message format (`FlexMessage`)**

---

## 📁 Repository Structure

```
FlexComm-Lab/
│
├── mqtt/                 # MQTT test clients and brokers
├── udp_tcp/              # UDP/TCP message simulators and listeners
├── rest/                 # Flask-based REST API simulator
├── serial/               # Serial communication scripts
├── messages/             # Example payloads and schema validators
├── tools/                # Miscellaneous helpers and CLI tools
└── docs/                 # Diagrams and integration examples
```

---

## 🚀 Getting Started

### Requirements

- Python 3.8+ (for REST and Serial tools)
- .NET Core / .NET Framework (for C# utilities)
- MQTT broker (e.g., [Mosquitto](https://mosquitto.org/download/)) for testing
- Unity project using [FlexComm](https://assetstore.unity.com/packages/tools/network/flexcomm-communication-framework-for-unity-XXXXX) (optional)

### Example: Start the REST test server

```bash
cd rest
pip install -r requirements.txt
python app.py
```

### Example: Send a test MQTT message

```bash
cd mqtt
python publish.py --topic test/topic --payload "{ \"message\": \"Hello from Lab\" }"
```

---

## 🧪 Use Cases

- ✅ Test FlexComm integration without launching Unity
- ✅ Simulate robot commands, sensor data, or REST API responses
- ✅ Debug message payloads, QoS, retained flags, and topic routing
- ✅ Validate serial devices and baud rate configurations
- ✅ Use as a foundation for integrating new protocols into FlexComm

---

## 📚 Documentation

See the [`docs/`](docs/) folder for:
- Architecture diagrams
- Protocol-specific guides
- Setup instructions for MQTT brokers and serial drivers
- JSON schema format for `FlexMessage`

---

## 🧠 Background

FlexComm-Lab is developed and maintained by [Eagle Creative](https://www.eagle-creative.com) to support [FlexComm](https://assetstore.unity.com/packages/tools/network/flexcomm-communication-framework-for-unity-XXXXX), a protocol-agnostic communication framework for Unity. FlexComm is the spiritual successor to the peer-reviewed [DTStacks](https://doi.org/10.1016/j.procir.2024.10.165) framework and has been used in multiple academic and industrial projects.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues, feature requests, or pull requests.

---

## 📬 Contact

For support or collaboration inquiries, contact:  
📧 info@eagle-creative.com  
🌐 https://www.eagle-creative.com
