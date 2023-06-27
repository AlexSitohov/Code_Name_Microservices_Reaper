import asyncio

import aio_pika


async def publish_email_data(email) -> None:
    connection = await aio_pika.connect_robust(
        "amqps://nuzlkbxa:hgvTbt9REcgTejxLf1DPNafsfB0icCmm@stingray.rmq.cloudamqp.com/nuzlkbxa",
    )

    async with connection:
        routing_key = "mails_queue"

        channel = await connection.channel()

        await channel.default_exchange.publish(
            aio_pika.Message(body=email.encode()),
            routing_key=routing_key,
        )
