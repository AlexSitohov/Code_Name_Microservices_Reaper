import asyncio

import aio_pika

from confirm_email import send_email


async def main() -> None:
    connection = await aio_pika.connect_robust(
        "amqps://nuzlkbxa:hgvTbt9REcgTejxLf1DPNafsfB0icCmm@stingray.rmq.cloudamqp.com/nuzlkbxa",
    )

    queue_name = "mails_queue"

    async with connection:
        # Creating channel
        channel = await connection.channel()

        # Will take no more than 10 messages in advance
        await channel.set_qos(prefetch_count=10)

        # Declaring queue
        queue = await channel.declare_queue(queue_name)

        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    print(message.body.decode())
                    raw_data: str = message.body.decode()
                    split_data = raw_data.split(':')
                    await send_email(split_data[0], split_data[1], split_data[2])

                    if queue.name in message.body.decode():
                        break


if __name__ == "__main__":
    asyncio.run(main())
