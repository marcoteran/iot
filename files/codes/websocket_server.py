import asyncio
import websockets

# define the WebSocket server details
HOST = '0.0.0.0'
PORT = 8765

async def handler(websocket, path):
    # handle WebSocket connections here
    message_count = 0
    while True:
        # receive data from the client
        message = await websocket.recv()

        # display the data in the terminal
        print(f"Received message: {message}")

        # increment the message count
        message_count += 1

        # check if the connection should be closed
        if message_count == 10:
            print("Closing connection after 10 messages")
            await websocket.close()
            break

async def main():
    # start the WebSocket server
    async with websockets.serve(handler, HOST, PORT):
        print(f"WebSocket server listening on {HOST}:{PORT}")

        # wait for 3 minutes before closing the server
        await asyncio.sleep(180)
        print("Closing WebSocket server")
        await server.close()

# start the event loop
asyncio.run(main())
