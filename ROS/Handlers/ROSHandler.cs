using UnityEngine;
using UnityEngine.Events;

namespace FlexComm.ROS.Handlers
{
    /// <summary>
    /// Generic Unity MonoBehaviour handler for ROS messages of type T.
    /// Handles deserialization, UnityEvent invocation, and application to the scene.
    /// </summary>
    public abstract class ROSHandler<T> : MonoBehaviour where T : class, new()
    {
        [Header("Events")]
        public UnityEvent<T> OnMessageReceived = new UnityEvent<T>();

        /// <summary>
        /// Call this when a JSON ROS message is received.
        /// </summary>
        public virtual void HandleIncoming(string json)
        {
            T msg = DeserializeMessage(json);
            OnMessageReceived.Invoke(msg);
            ApplyMessage(msg);
        }

        /// <summary>
        /// Convert message object to JSON. Override if needed.
        /// </summary>
        public virtual string SerializeMessage(T msg)
        {
            return JsonUtility.ToJson(msg);
        }

        /// <summary>
        /// Convert JSON to message object. Override if needed.
        /// </summary>
        public virtual T DeserializeMessage(string json)
        {
            return JsonUtility.FromJson<T>(json);
        }

        /// <summary>
        /// Apply the message to the scene or system. Override in subclasses.
        /// </summary>
        public virtual void ApplyMessage(T msg) { }
    }
}
