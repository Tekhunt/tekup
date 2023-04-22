import pusher
import os
from dotenv import load_dotenv

load_dotenv()

pusher_client = pusher.Pusher(
    app_id=str(os.getenv("APP_ID")),
    key=str(os.getenv("KEY")),
    secret=str(os.getenv("SECRET")),
    cluster=str(os.getenv("CLUSTER")),
    ssl=bool(str(os.getenv("SSL"))),
)


pusher_client.trigger("my-channel", "my-event", {"message": "hello world"})
