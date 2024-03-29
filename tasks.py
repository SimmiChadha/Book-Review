import asyncio

async def send_confirmation_email(review_id:int):
    # simulate sending an email 
    await asyncio.sleep(5)
    print(f'confimration email sent for review id :{review_id}')