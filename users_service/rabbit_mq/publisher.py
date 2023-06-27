import asyncio

import aio_pika

from users_service_config import RABBIT_MQ_ADDRESS


async def publish_email_data(email) -> None:
    connection = await aio_pika.connect_robust(RABBIT_MQ_ADDRESS, )

    async with connection:
        routing_key = "mails_queue"

        channel = await connection.channel()

        await channel.default_exchange.publish(
            aio_pika.Message(body=email.encode()),
            routing_key=routing_key,
        )
