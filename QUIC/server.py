import asyncio
from aioquic.asyncio import serve
from aioquic.quic.configuration import QuicConfiguration
from aioquic.quic.events import QuicEvent, StreamDataReceived

class MyQuicProtocol(asyncio.Protocol):
    def __init__(self):
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport

    def quic_event_received(self, event: QuicEvent):
        if isinstance(event, StreamDataReceived):
            # Handle incoming data from the client
            data = event.data
            # Process the received data as needed

    def connection_lost(self, exc):
        # Handle connection lost event
        pass

async def run_quic_server():
    try:
        configuration = QuicConfiguration(is_client=False)
        configuration.load_cert_chain(certfile="certs/server.crt", keyfile="certs/server.key")
        await serve(
            "localhost",
            3074,
            configuration=configuration,
            create_protocol=MyQuicProtocol,
        )
    except FileNotFoundError:
        print("Server certificate and key files not found.")

# Run the QUIC server
asyncio.run(run_quic_server())