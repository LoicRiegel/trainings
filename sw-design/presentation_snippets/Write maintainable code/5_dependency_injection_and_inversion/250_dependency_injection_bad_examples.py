# Example 1: creation inside a function

class StripePaymentHandler: # do not show in slide
    def handle_payment():
        pass

def process_payment(amount: int) -> None:
    logging.info(f"Order total is ${amount/100:.2f}.")
    payment_handler = StripePaymentHandler()
    payment_handler.handle_payment(amount)
    logging.info("Order completed.")


# Example 2: creation in class init


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

