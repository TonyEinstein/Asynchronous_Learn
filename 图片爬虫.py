import asyncio,aiohttp,aiofiles,requests
import os.path

from lxml import etree
async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            html = etree.HTML(await resp.content.read())
            res = html.xpath('//div[@class="thumb-container"]//img[@class="img-responsive big-thumb thumb-desktop"]/@src')
            for img_url in res:
                print(f"开始下载：{img_url}")
                file_name = img_url.rsplit('/',1)[1]
                async with session.get(img_url) as resp:
                    async with aiofiles.open('imgdir/'+file_name,'wb') as f:
                        await f.write(await resp.content.read())

async def main():
    if not os.path.exists("imgdir/"):
        os.makedirs("imgdir/")
    tasks = []
    # 这里设置页数
    for i in range(30):
        tasks.append(asyncio.create_task(
            download(f'https://wall.alphacoders.com/by_collection.php?id=655&quickload=1&page={i}')
        )
        )
    await asyncio.wait(tasks)

if __name__ == '__main__':
    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
    # loop = asyncio.get_event_loop()  # 可以防止报错
    # loop.run_until_complete(main())