"""
FlexComm Test REST Server Example
Copyright (c) 2025 Jonas S.I. Rieder, Eagle Creative

This script is an example server provided for public use as a free external testing tool. It is intended for demonstration and testing purposes only, and is not part of the commercial FlexComm Unity Asset Package.

This software is provided "as is" without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.

By using this script, you agree to the terms and conditions outlined in the Unity Asset Store End User License Agreement (EULA) and any additional terms specified by Eagle Creative.

Unauthorized distribution, modification, or resale of this script or its contents is strictly prohibited.

For support or inquiries, please contact Eagle Creative at info@eagle-creative.com.
"""

# -----------------------------------------------------------------------------
# FlexComm Test REST Server - Overview
# -----------------------------------------------------------------------------
# This script implements a simple REST server using FastAPI for testing message
# publishing and subscribing. It is designed for demonstration and testing only.
#
# How it works:
# - The server allows clients to publish messages to topics, retrieve (subscribe)
#   messages from topics, update or delete messages, and check server health.
# - All data is stored in memory (not persistent).
# - Endpoints:
#   * POST   /publish/{topic}         - Publish a message to a topic
#   * GET    /publish/{topic}         - Retrieve (subscribe) messages from a topic
#   * PUT    /publish/{topic}/{idx}   - Update a specific message in a topic
#   * PUT    /publish/{topic}         - Update the latest message in a topic
#   * DELETE /publish/{topic}/{idx}   - Delete a specific message in a topic
#   * DELETE /publish/{topic}         - Delete the latest message in a topic
#   * GET    /health                  - Health check endpoint
#
# To run: python rest_server.py
#
# Dependencies: fastapi, uvicorn
#
# Required Python Packages:
#   pip install fastapi uvicorn
#
# Optionally, for CORS support (already included above):
#   pip install fastapi[all]
# -----------------------------------------------------------------------------

# -*- coding: utf-8 -*-
# Syntax highlighting: Python 3

from fastapi import FastAPI, HTTPException, Request, APIRouter
from fastapi.responses import JSONResponse
from typing import Dict, List
import uvicorn
import json
import traceback
import asyncio
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI app instance
app = FastAPI(title="FlexComm Test REST Server")

# Enable CORS (Cross-Origin Resource Sharing) for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory message storage: {topic: [messages]}
messages: Dict[str, List[dict]] = {}

# Create a router for publish/subscribe endpoints
router = APIRouter(prefix="/publish")

# Endpoint: Publish a message to a topic
@router.post("/{topic}")
async def publish_message(topic: str, request: Request):
    try:
        raw_bytes = await request.body()  # Get raw request body
        print(f"[DEBUG] Raw bytes received: {raw_bytes}")
        if not raw_bytes:
            raise ValueError("Empty body")
        try:
            body = raw_bytes.decode("utf-8")  # Decode bytes to string
        except Exception as e:
            print(f"[ERROR] UTF-8 decode failed: {e}")
            raise HTTPException(status_code=400, detail="Body is not valid UTF-8")
        print(f"[DEBUG] Decoded body: {body}")
        try:
            body_json = json.loads(body)  # Try to parse as JSON
            print(f"[DEBUG] Parsed JSON: {body_json}")
        except json.JSONDecodeError:
            print(f"[DEBUG] Not valid JSON, using as plain string payload.")
            body_json = body  # Use as plain string if not JSON
    except Exception as e:
        print(f"[ERROR] Exception in publish_message: {e}\n{traceback.format_exc()}")
        raise HTTPException(status_code=400, detail=f"Invalid or missing body (expected byte[] encoded JSON or string): {e}")
    msg = {"payload": body_json, "topic": topic}
    if topic not in messages:
        messages[topic] = []
    messages[topic].append(msg)  # Store message in topic
    return {"status": "published", "topic": topic, "count": len(messages[topic])}

# Endpoint: Subscribe to a topic (retrieve messages)
@router.get("/{topic}")
async def subscribe_topic(topic: str, timeout: int = 20):
    try:
        waited = 0
        poll_interval = 0.5
        while waited < timeout:
            if topic in messages and messages[topic]:
                msgs = messages[topic][:]
                messages[topic] = []  # Clear messages after delivery
                return {"status": "delivered", "topic": topic, "messages": msgs}
            await asyncio.sleep(poll_interval)
            waited += poll_interval
        # Timeout, no messages
        return {"status": "no_messages", "topic": topic, "messages": []}
    except Exception as e:
        print(f"[ERROR] Exception in subscribe_topic: {e}\n{traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")

# Endpoint: Update a specific message in a topic
@router.put("/{topic}/{msg_idx}")
async def update_message(topic: str, msg_idx: int, request: Request):
    try:
        if topic not in messages or msg_idx >= len(messages[topic]):
            raise HTTPException(status_code=404, detail="Message not found")
        try:
            body = await request.json()  # Expect JSON body
        except Exception as e:
            print(f"[ERROR] JSON decode failed in update_message: {e}")
            raise HTTPException(status_code=400, detail="Invalid JSON body")
        messages[topic][msg_idx]["payload"] = body  # Update message
        return {"status": "updated", "topic": topic, "msg_idx": msg_idx}
    except HTTPException:
        raise
    except Exception as e:
        print(f"[ERROR] Exception in update_message: {e}\n{traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")

# Endpoint: Update the latest message in a topic
@router.put("/{topic}")
async def update_latest_message(topic: str, request: Request):
    try:
        if topic not in messages or not messages[topic]:
            raise HTTPException(status_code=404, detail="No messages to update")
        raw_bytes = await request.body()
        print(f"[DEBUG] Raw bytes received (PUT /{{topic}}): {raw_bytes}")
        if not raw_bytes:
            raise HTTPException(status_code=400, detail="Empty body")
        try:
            body = raw_bytes.decode("utf-8")
        except Exception as e:
            print(f"[ERROR] UTF-8 decode failed in update_latest_message: {e}")
            raise HTTPException(status_code=400, detail="Body is not valid UTF-8")
        print(f"[DEBUG] Decoded body (PUT /{{topic}}): {body}")
        try:
            body_json = json.loads(body)
            print(f"[DEBUG] Parsed JSON (PUT /{{topic}}): {body_json}")
        except json.JSONDecodeError:
            print(f"[DEBUG] Not valid JSON in update_latest_message, using as plain string payload.")
            body_json = body
        messages[topic][-1]["payload"] = body_json  # Update latest message
        return {"status": "updated", "topic": topic, "msg_idx": len(messages[topic])-1}
    except HTTPException:
        raise
    except Exception as e:
        print(f"[ERROR] Exception in update_latest_message: {e}\n{traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")

# Endpoint: Delete a specific message in a topic
@router.delete("/{topic}/{msg_idx}")
async def delete_message(topic: str, msg_idx: int):
    try:
        if topic not in messages or msg_idx >= len(messages[topic]):
            raise HTTPException(status_code=404, detail="Message not found")
        messages[topic].pop(msg_idx)  # Remove message
        return {"status": "deleted", "topic": topic, "msg_idx": msg_idx}
    except HTTPException:
        raise
    except Exception as e:
        print(f"[ERROR] Exception in delete_message: {e}\n{traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")

# Endpoint: Delete the latest message in a topic
@router.delete("/{topic}")
async def delete_latest_message(topic: str):
    try:
        if topic not in messages or not messages[topic]:
            raise HTTPException(status_code=404, detail="No messages to delete")
        messages[topic].pop()  # Remove latest message
        return {"status": "deleted", "topic": topic, "msg_idx": len(messages[topic])}
    except HTTPException:
        raise
    except Exception as e:
        print(f"[ERROR] Exception in delete_latest_message: {e}\n{traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")

# Register the router with the app
app.include_router(router)

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok"}

# Run the server if this script is executed directly
if __name__ == "__main__":
    uvicorn.run(
        "rest_server:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
