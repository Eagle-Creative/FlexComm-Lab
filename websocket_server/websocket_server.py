"""
FlexComm Test WebSocket Server Example
Copyright (c) 2025 Jonas S.I. Rieder, Eagle Creative

This script is an example WebSocket server provided for public use as a free external testing tool. It is intended for demonstration and testing purposes only, and is not part of the commercial FlexComm Unity Asset Package.

This software is provided "as is" without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.

By using this script, you agree to the terms and conditions outlined in the Unity Asset Store End User License Agreement (EULA) and any additional terms specified by Eagle Creative.

Unauthorized distribution, modification, or resale of this script or its contents is strictly prohibited.

For support or inquiries, please contact Eagle Creative at info@eagle-creative.com.
"""

# -----------------------------------------------------------------------------
# Required Python Packages:
#   pip install websockets
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# FlexComm Test WebSocket Server - Overview
# -----------------------------------------------------------------------------
# This script implements a simple WebSocket echo server using the 'websockets'
# library for testing and demonstration purposes.
#
# How it works:
# - The server listens for WebSocket connections on ws://0.0.0.0:8080
# - When a client connects, it is added to the set of connected clients.
# - Any message received from a client is echoed back to that client.
# - The server prints connection, message, and disconnection events to the console.
# - All connections and messages are handled asynchronously.
#
# To run: python websocket_server.py
#
# Dependencies: websockets
# -----------------------------------------------------------------------------

import asyncio
import websockets

# Set to keep track of connected clients
connected_clients = set()

# Handler for each client connection
async def echo(websocket):
    print(f"[CONNECTED] New client: {websocket.remote_address}", flush=True)
    connected_clients.add(websocket)
    try:
        # Listen for incoming messages from this client
        async for message in websocket:
            print(f"[RECEIVED] {message} from {websocket.remote_address}", flush=True)
            await websocket.send(message)  # Echo the message back
    except websockets.ConnectionClosed:
        print(f"[DISCONNECTED] {websocket.remote_address}", flush=True)
    finally:
        connected_clients.remove(websocket)

# Main server coroutine
async def main():
    # Start the WebSocket server on port 9001
    print("[SERVER] Starting WebSocket server...", flush=True)
    async with websockets.serve(echo, "0.0.0.0", 9001):
        print("[SERVER] Listening on ws://0.0.0.0:9001", flush=True)
        await asyncio.Future()  # run forever

# Entry point: run the server
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("[SERVER] Stopped", flush=True)
