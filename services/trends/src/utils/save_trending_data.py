import asyncio
from prisma import Prisma
from prisma.models import TrendingData
from trending_data import get_trending_data

async def trends(hashtags, db) -> None:
    
    await db.connect()

    for hashtag in hashtags:
        trending_data = get_trending_data(hashtag)            

        for data in trending_data:
            d = await TrendingData.prisma().create(
                data={
                    "hashtag": hashtag,
                    "postAuthorNickname": data["postAuthorNickname"],
                    "description": data["description"],
                    "musics": {
                        "create": {
                            "author": data["music_author"]
                        }
                    }
                },
            )
            print("Saved data: ", d.createdAt)
    await db.disconnect()


async def schedule_task(task, hashtags):
    db = Prisma(auto_register=True)
    while True:
        await asyncio.gather(
            asyncio.sleep(3600), # Sleep 1 hour
            task(hashtags, db)
        )

if __name__ == "__main__":
    asyncio.run(schedule_task(trends, ["iautocompleta"]))
        

