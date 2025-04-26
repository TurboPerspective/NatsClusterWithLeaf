import asyncio
from nats.aio.client import Client as NATS

async def publish_message():
    nc = NATS()

    # Connect to the NATS server
    await nc.connect("nats://app:app_password@127.0.0.1:4222")

    try:
        while True:
            # Publish a message to the "updates" subject
            await nc.publish("updates", b"Hello, NATS!")
            print("Message published to 'updates'")
            await asyncio.sleep(1)  # Wait for 1 second
    except KeyboardInterrupt:
        print("Stopping publisher...")
    finally:
        # Close the connection
        await nc.close()

if __name__ == "__main__":
    print('Hello World: NATS Publisher')
    asyncio.run(publish_message())