# Network Simulation with Packet Routing using BFS and DFS

## Project Overview

This project simulates a simple network of devices (Computers and Routers) connected by wires. It supports:

- Sending data packets from one device to another
- Finding routing paths using BFS or DFS algorithms
- Forwarding packets through routers to the destination
- Handling delivery failures and sending error packets back
- Thread-safe device state management and logging

---

## Features

- **Device Hierarchy:** `Device` base class with `Computer` and `Router` subclasses.
- **Path Finding:** Uses BFS or DFS to discover paths in the network graph.
- **Packet Transmission:** Packets carry data and traverse the network along computed paths.
- **Error Handling:** Routers send error packets if delivery fails.
- **Thread Safety:** Devices use locks to manage concurrent state changes safely.
- **Network Graph:** Dynamic undirected graph connecting devices.

---

## Installation

Make sure Python 3 is installed. This project uses only standard Python libraries; no external dependencies required.

---

## Usage

- Instantiate devices (`Computer` and `Router`)
- Connect devices using `connect_devices(device1, device2)`
- Use `computer.send_packet(destination, data, algorithm)` to send packets using BFS or DFS pathfinding.
- The system logs packet transmission steps, path discovery, and error handling.

---

## Example Code Snippet

```python
computer1 = Computer("Computer1")
computer2 = Computer("Computer2")
router1 = Router("Router1")
router2 = Router("Router2")

connect_devices(computer1, router1)
connect_devices(router1, router2)
connect_devices(router2, computer2)

# Send packet using BFS
computer1.send_packet(computer2, "Hello World!", algorithm="BFS")

# Send packet using DFS
computer1.send_packet(computer2, "Hello Again!", algorithm="DFS")
```
## Code Structure Highlights

- **Device Class:**  
  Base class for all network devices, handles on/off state and logging.

- **Computer Class:**  
  Sends and receives packets, finds routing paths using BFS/DFS.

- **Router Class:**  
  Forwards packets, manages error packets when delivery fails.

- **Packet Class:**  
  Holds packet information including source, destination, data, and path.

- **Network Graph:**  
  Represented as an adjacency list dictionary connecting devices.

---

## Notes

- The routing algorithms operate on a global `network` graph dictionary.

- Packets carry their computed path, and routers forward them accordingly.

- Error packets trace back to the sender if delivery fails.

- Locks ensure thread-safe operations on devices.
