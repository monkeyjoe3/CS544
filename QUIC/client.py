import asyncio
from aioquic.asyncio import connect
from aioquic.quic.configuration import QuicConfiguration

async def run_quic_client():
    # Create a QUIC configuration
    configuration = QuicConfiguration(is_client=True)

    # Connect to the server
    async with connect("example.com", 443, configuration=configuration) as client:
        # Perform the handshake
        await client.handshake()

        # Send data to the server
        stream = client.get_stream()
        await stream.send("Hello, server!")

        # Receive data from the server
        data = await stream.receive()
        print("Received data from server:", data)

asyncio.run(run_quic_client())