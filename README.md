# Socket Communication, HTTP GET Request, and ICMP Packet with Scapy in Python

This document showcases examples of Python scripts performing the following network-related tasks:  
1. **Socket Communication**: Basic client-server communication using sockets.  
2. **HTTP GET Request**: Fetching data from a public API using the `requests` library.  
3. **ICMP Packet with Scapy**: Sending ICMP packets for network testing and checking for responses.

---

## Table of Contents
1. [Socket Communication](#socket-communication)
   - [Project Overview](#project-overview)
   - [Prerequisites](#prerequisites)
   - [Setup](#setup)
   - [Usage](#usage)
   - [How It Works](#how-it-works)
   - [Example Output](#example-output)
   - [Notes](#notes)
2. [HTTP GET Request](#http-get-request)
   - [Project Overview](#project-overview-1)
   - [Prerequisites](#prerequisites-1)
   - [Setup](#setup-1)
   - [Usage](#usage-1)
   - [How It Works](#how-it-works-1)
   - [Example Output](#example-output-1)
   - [Notes](#notes-1)
3. [ICMP Packet with Scapy](#icmp-packet-with-scapy)
   - [Project Overview](#project-overview-2)
   - [Prerequisites](#prerequisites-2)
   - [Setup](#setup-2)
   - [Usage](#usage-2)
   - [How It Works](#how-it-works-2)
   - [Example Output](#example-output-2)
   - [Notes](#notes-2)

---

## Socket Communication

### Project Overview

This project contains:
1. A **server** script that listens for incoming client connections on a specified host and port.
2. A **client** script that connects to the server, sends a message, and prints the response received from the server.

---

### Prerequisites

To run this project, you need:
- Python 3.6 or later installed on your system.
- Basic knowledge of Python and networking.

---

### Setup

1. Clone or download this repository.
2. Create a `.env` file in the project directory for the client script with the following environment variables:
   ```env
   CLIENT_HOST=127.0.0.1
   CLIENT_PORT=12345
   ```
3. Install Python dependencies if needed (e.g., `dotenv` for environment variable management).

---

### Usage

#### Running the Server
1. Open a terminal and navigate to the project directory.
2. Run the server script:
   ```bash
   python server.py
   ```
   The server will start listening on `127.0.0.1:12345`.

#### Running the Client
1. Open another terminal and navigate to the project directory.
2. Run the client script:
   ```bash
   python client.py
   ```
3. The client will send a message to the server and display the server's response.

---

### How It Works

1. **Server**:
   - Creates a socket and binds it to a host and port (`127.0.0.1:12345` by default).
   - Listens for incoming connections using the `socket.listen()` method.
   - Accepts a connection, receives data, and echoes it back to the client.

2. **Client**:
   - Reads the host and port from environment variables.
   - Creates a socket and connects to the server.
   - Sends a predefined message (`"Hello, Server!"`).
   - Receives and prints the echoed response from the server.

---

### Example Output

#### Server
```bash
Server listening on 127.0.0.1:12345
Connection established with ('127.0.0.1', 54321)
Received data: Hello, Server!
```

#### Client
```bash
Received data: Hello, Server!
```

---

### Notes

1. Ensure both the server and client scripts are running on the same machine or adjust the `CLIENT_HOST` in `.env` for a remote server.
2. The server host and port are hardcoded (`127.0.0.1:12345`). You can modify these in the server script as needed.
3. This is a basic implementation for educational purposes and does not handle advanced networking scenarios like timeouts, concurrency, or error handling.

---

## HTTP GET Request

### Project Overview

This script demonstrates how to use the `requests` library in Python to perform a basic **HTTP GET request** to fetch data from a public API.

The script:
1. Sends a GET request to the URL `https://jsonplaceholder.typicode.com/posts/1`.
2. Checks the response status.
3. Prints the response data in JSON format if successful or an error message otherwise.

---

### Prerequisites

To run this script, you need:
- Python 3.6 or later installed on your system.
- The `requests` library installed. You can install it using pip:
  ```bash
  pip install requests
  ```

---

### Setup

1. Clone or download this repository.
2. Ensure Python dependencies are installed (use the pip command above if needed).

---

### Usage

1. Run the script:
   ```bash
   python req.py
   ```
2. The script will print the response data or an error message based on the response status.

---

### How It Works

1. **HTTP GET Request**:
   - The script uses the `requests.get()` method to send a GET request to the URL.
   - Checks the status code of the response to determine success (`200`).
   - If successful, it parses the response as JSON using `.json()` and prints it.
   - If the request fails, it prints an error message with the response status code.

---

### Example Output

#### Successful Request
```json
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}
```

#### Failed Request
```bash
Request failed with status code 404
```

---

### Notes

1. The example uses the `https://jsonplaceholder.typicode.com` API, a public REST API for testing purposes.
2. The script does not handle advanced HTTP scenarios like headers, authentication, or timeouts.
3. To test with a different API endpoint, replace the URL in the `requests.get()` call.


## ICMP Packet with Scapy

### Project Overview

This script demonstrates how to use Python's `scapy` library to craft and send an **ICMP (Internet Control Message Protocol)** packet to a target IP address. The script checks for a response, useful for network testing or a basic ping implementation.

---

### Prerequisites

To run this script, you need:
1. Python 3.6 or later installed on your system.
2. The `scapy` library installed. Install it using pip:
   ```bash
   pip install scapy
   ```
3. **Root permissions**: The Scapy library requires elevated privileges to run properly, as it directly accesses network interfaces.

---

### Setup

1. Clone or download this repository.
2. Create a `.env` file in the project directory and define the target IP address:
   ```env
   TARGET_IP=8.8.8.8
   ```

---

### Usage

1. Run the script with elevated privileges (e.g., using `sudo` on Linux):
   ```bash
   sudo python icmp_test.py
   ```
2. The script will send an ICMP packet to the target IP and display whether a response was received.

---

### How It Works

1. **Crafting the Packet**:
   - The `scapy` library is used to create an ICMP packet.
   - The `IP` layer specifies the destination IP address (from the `TARGET_IP` environment variable).
   - The `ICMP()` function is used to create the ICMP payload.

2. **Sending and Receiving**:
   - The `sr1()` function sends the crafted packet and waits for a single response.
   - A timeout of 2 seconds is specified to prevent indefinite blocking.

3. **Response Handling**:
   - If a response is received, the script prints the source IP address of the response.
   - If no response is received, an appropriate message is displayed.

---

### Example Output

#### Successful Response
```bash
Response received from 8.8.8.8
```

#### No Response
```bash
No response received
```

---

### Notes

1. **Root Permissions**:
   - Scapy requires root privileges to send and receive raw packets. Use `sudo` or run the script as an administrator.

2. **Target IP**:
   - Update the `TARGET_IP` variable in the `.env` file to test against a specific host.
   - Ensure the target allows ICMP traffic (some hosts block ping requests).

3. **Timeout**:
   - The default timeout for waiting for a response is 2 seconds. Modify this value in the `sr1()` function if needed.

---