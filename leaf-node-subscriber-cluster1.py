import asyncio
from nats.aio.client import Client as NATS

async def subscribe():
    nc = NATS()

    # Connect to the NATS server (leaf node)
    await nc.connect("nats://app:app_password@127.0.0.1:4225")

    async def message_handler(msg):
        subject = msg.subject
        data = msg.data.decode()
        print(f"Received a message in LEAF Nodes on '{subject}': {data}")

    # Subscribe to the "leafnode-updates" subject
    await nc.subscribe("updates", cb=message_handler)

    # Keep the subscriber running
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("Closing connection...")
        await nc.close()

if __name__ == "__main__":
    print('Leaf Node: NATS Subscriber')
    asyncio.run(subscribe())