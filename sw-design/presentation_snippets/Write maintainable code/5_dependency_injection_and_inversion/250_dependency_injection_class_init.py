# BEFORE


class Com:
    """Some part of the application which needs to communication
    via websocket.
    """

    def __init__(
        self,
        host: str = "localhost",
        port: str = "3000",
        # plus other params
    ) -> None:
        self.host = host
        self.port = port
        self.socketio_client = socketio.Client(
            reconnection=True,
            reconnection_attempts=10,
            reconnection_delay=1,
            reconnection_delay_max=60,
        )


def main():
    host= "localhost"
    port = "1000"
    com = Com(host, port)

# AFTER


class Com:
    """Some part of the application which needs to communication
    via websocket.
    """

    def __init__(
        self,
        host: str = "localhost",
        port: str = "3000",
        socketio_client: socketio.Client,
        # plus other params
    ) -> None:
        self.host = host
        self.port = port
        self.socketio_client = socketio_client


def main():
    host= "localhost"
    port = "1000"
    socketio_client = socketio.Client(
        reconnection=True,
        reconnection_attempts=10,
        reconnection_delay=1,
        reconnection_delay_max=60,
    )
    com = Com(host, port, socketio_client)
