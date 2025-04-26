# README

## NATS Cluster and Leaf Node Setup

This project demonstrates how to set up a NATS cluster with three nodes, a leaf node, and run Python subscribers and publishers.

---

### Prerequisites

1. **Install NATS Server**:
   - Download and install the NATS server from [NATS.io](https://nats.io/download/).

2. **Install Python Dependencies**:
   - Ensure Python 3.7+ is installed.
   - Install the required Python library:
     ```bash
     pip install -r requirements.txt
     ```

---

### NATS Server Configuration

1. **Cluster Node Configurations**:
   - Create configuration files for each cluster node:
     - `nats-node1.conf`
     - `nats-node2.conf`
     - `nats-node3.conf`

   Example for `nats-node2.conf`:
   ```text
   server_name: "nats-server-2"
   port: 4223
   cluster {
     name: "nats-cluster"
     port: 6223
     routes: [
       "nats://127.0.0.1:6222",
       "nats://127.0.0.1:6224"
     ]
   }
   leafnodes {
     port: 7425
   }
   accounts: {
     SYS: {
       users: [
         { user: "sys", password: "password" }
       ]
     },
     APP: {
       users: [
         { user: "app", password: "app_password" }
       ]
     }
   }

   system_account: SYS
   ```

2. **Leaf Node Configuration**:
   - Create a `leafnode.conf` file for the leaf node:
     ```text
     accounts: {
       APP: {
         users: [
           { user: "app", password: "app_password" }
         ]
       }
     }

     leafnodes {
       remotes: [
         {
           url: "nats://127.0.0.1:6222"
           credentials: { user: "app", password: "app_password" }
         }
       ]
     }
     ```

---

### Starting the NATS Cluster and Leaf Node

1. **Start the Cluster Nodes**:
   - Open three separate terminals and run:
     ```bash
     nats-server -c nats-node1.conf
     ```
     ```bash
     nats-server -c nats-node2.conf
     ```
     ```bash
     nats-server -c nats-node3.conf
     ```

2. **Start the Leaf Node**:
   - Open a terminal and run:
     ```bash
     nats-server -c leafnode.conf
     ```

3. **Verify the Setup**:
   - Use the `nats` CLI or monitoring tools to confirm all nodes are running and connected.

---

### Running the Python Scripts

1. **Run the NATS Subscriber**:
   - Start the subscriber for the main NATS cluster:
     ```bash
     python nats-subscriber.py
     ```

2. **Run the Publisher**:
   - Start the publisher to send messages:
     ```bash
     python nats-publisher.py
     ```
3. **Run Leaf Node Subscriber**:
   - Start the LEAF Node subscriber for LEAF Node:
     ```bash
     python leafnode-subscriber.py
     ```
4. **Verify Messages**:
   - Check the output of the subscriber scripts to ensure messages are being received.

---

### Notes

- Ensure the NATS server and leaf node are running before starting the Python scripts.
- Modify the server URLs and credentials in the Python scripts if needed.
- Use `Ctrl+C` to stop the scripts gracefully.