from TikTokApi import TikTokApi
import asyncio
import os

ms_token = os.environ.get("ms_token", None)


async def trending_videos():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=5)
        async for video in api.trending.videos(count=1):
            print(video)
            print(video.as_dict)


if __name__ == "__main__":
    asyncio.run(trending_videos())