from threading import Lock
from collections import deque

# کلاس مادر برای Device
class Device:
    def __init__(self, name):
        self.name = name
        self.is_on = True
        self.lock = Lock()

    def turn_on(self):
        with self.lock:
            self.is_on = True
            print(f"{self.name} is now ON.")

    def turn_off(self):
        with self.lock:
            self.is_on = False
            print(f"{self.name} is now OFF.")

    def log(self, packet, message):
        print(f"LOG: {self.name} - {message} for Packet ID: {packet.packet_id}")

    def __repr__(self):
        return self.name


# کلاس Computer که از Device ارث‌بری می‌کند
class Computer(Device):
    def __init__(self, name):
        super().__init__(name)

    def send_packet(self, destination, data, algorithm="BFS"):
        print(f"Sending packet from {self.name} to {destination.name} using {algorithm}")
        packet = Packet(self, destination, data)
        path = self.find_route(destination, algorithm)
        if path:
            packet.set_path(path)
            print(f"Path found: {path}")
            self.transmit_packet(packet)
        else:
            print("No route found.")
            self.log(packet, "No route available, transmission failed")

    def find_route(self, destination, algorithm="BFS"):
        if algorithm == "BFS":
            return self.bfs(destination)
        elif algorithm == "DFS":
            return self.dfs(destination)
        else:
            return None

    def bfs(self, destination):
        visited = set()
        queue = deque([(self, [])])

        while queue:
            current, path = queue.popleft()
            if current == destination:
                return path + [current]

            visited.add(current)
            for neighbor in network[current]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [current]))

        return None

    def dfs(self, destination):
        visited = set()
        stack = [(self, [])]

        while stack:
            current, path = stack.pop()
            if current == destination:
                return path + [current]

            visited.add(current)
            for neighbor in network[current]:
                if neighbor not in visited:
                    stack.append((neighbor, path + [current]))

        return None

    def transmit_packet(self, packet):
        print(f"Transmitting packet {packet.packet_id} along the path: {packet.path}")
        current = packet.path.pop(0)
        while packet.path:
            next_device = packet.path.pop(0)
            if isinstance(next_device, Router):
                next_device.forward_packet(packet, self)
            elif isinstance(next_device, Computer) and next_device == packet.destination:
                self.log(packet, f"Successfully delivered to {next_device.name} with data: {packet.data}")
                break

    def receive_error_packet(self, packet):
        self.log(packet, "Failed to deliver")

# کلاس Router که از Device ارث‌بری می‌کند
class Router(Device):
    def __init__(self, name):
        super().__init__(name)

    def forward_packet(self, packet, sender):
        if not packet.path:
            self.log(packet, "No further route, sending error back")
            error_packet = Packet(packet.destination, sender, f"Error: Delivery failed for Packet ID {packet.packet_id}")
            error_packet.set_path(self.find_reverse_route(sender))
            self.send_error_packet(error_packet)
        else:
            self.log(packet, f"Forwarding to {packet.path[0]}")
            next_device = packet.path.pop(0)
            if isinstance(next_device, Router):
                next_device.forward_packet(packet, sender)
            elif isinstance(next_device, Computer):
                next_device.log(packet, "Packet delivered successfully")

    def send_error_packet(self, error_packet):
        self.log(error_packet, "Sending error packet")
        current = error_packet.path.pop(0)
        while error_packet.path:
            next_device = error_packet.path.pop(0)
            if isinstance(next_device, Router):
                next_device.forward_packet(error_packet, self)
            elif isinstance(next_device, Computer):
                next_device.receive_error_packet(error_packet)

    def find_reverse_route(self, destination):
        # جستجوی مسیر برگشتی ساده با استفاده از BFS
        visited = set()
        queue = deque([(self, [])])

        while queue:
            current, path = queue.popleft()
            if current == destination:
                return path + [current]

            visited.add(current)
            for neighbor in network[current]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [current]))

        return None


# کلاس Wire که دو دستگاه را به هم متصل می‌کند
class Wire:
    def __init__(self, device1, device2):
        self.device1 = device1
        self.device2 = device2

    def connects(self, device):
        return device in [self.device1, self.device2]


# کلاس Packet که اطلاعات بسته را نگه‌داری می‌کند
class Packet:
    def __init__(self, source, destination, data):
        self.packet_id = id(self)
        self.source = source
        self.destination = destination
        self.data = data
        self.path = []

    def set_path(self, path):
        self.path = path.copy()

    def __repr__(self):
        return f"Packet({self.source.name} -> {self.destination.name}, ID: {self.packet_id})"


# ساختار شبکه (گراف) که دستگاه‌ها را به هم متصل می‌کند
network = {}

def connect_devices(device1, device2):
    if device1 not in network:
        network[device1] = []
    if device2 not in network:
        network[device2] = []
    
    network[device1].append(device2)
    network[device2].append(device1)


# نمونه‌سازی کامپیوترها و مسیریاب‌ها
computer1 = Computer("Computer1")
computer2 = Computer("Computer2")
router1 = Router("Router1")
router2 = Router("Router2")

# اتصال دستگاه‌ها به یکدیگر
connect_devices(computer1, router1)
connect_devices(router1, router2)
connect_devices(router2, computer2)

# ارسال بسته با استفاده از BFS
computer1.send_packet(computer2, "Hello World!", algorithm="BFS")

# ارسال بسته با استفاده از DFS
computer1.send_packet(computer2, "Hello Again!", algorithm="DFS")

#test for pushhhhh
