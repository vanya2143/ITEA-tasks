# Сделать скрипт, который будет делать GET запросы на следующие ресурсы:
#     "http://docs.python-requests.org/",
#     "https://httpbin.org/get",
#     "https://httpbin.org/",
#     "https://api.github.com/",
#     "https://example.com/",
#     "https://www.python.org/",
#     "https://www.google.com.ua/",
#     "https://regex101.com/",
#     "https://docs.python.org/3/this-url-will-404.html",
#     "https://www.nytimes.com/guides/",
#     "https://www.mediamatters.org/",
#     "https://1.1.1.1/",
#     "https://www.politico.com/tipsheets/morning-money",
#     "https://www.bloomberg.com/markets/economics",
#     "https://www.ietf.org/rfc/rfc2616.txt"
#
# Для каждого запроса должен быть вывод по примеру: "Resource 'google.com.ua',
# request took 0.23 sec, response status - 200."
# В реализации нет ограничений - можно использовать процессы, потоки, асинхронность.
# Любые вспомагательные механизмы типа Lock, Semaphore, пулы для тредов и потоков.


import aiohttp
import asyncio
from time import time


async def get_resp(session, url):
    async with session.get(url) as resp:
        return resp.status


async def req(url):
    async with aiohttp.ClientSession() as session:
        time_start = time()
        status_code = await get_resp(session, url)
        print(f"Resource '{url}', request took {time() - time_start:.3f}, response status - {status_code}")


if __name__ == '__main__':
    urls = [
        "http://docs.python-requests.org/",
        "https://httpbin.org/get",
        "https://httpbin.org/",
        "https://api.github.com/",
        "https://example.com/",
        "https://www.python.org/",
        "https://www.google.com.ua/",
        "https://regex101.com/",
        "https://docs.python.org/3/this-url-will-404.html",
        "https://www.nytimes.com/guides/",
        "https://www.mediamatters.org/",
        "https://1.1.1.1/",
        "https://www.politico.com/tipsheets/morning-money",
        "https://www.bloomberg.com/markets/economics",
        "https://www.ietf.org/rfc/rfc2616.txt"
    ]

    futures = [req(url) for url in urls]

    loop = asyncio.get_event_loop()
    t_start = time()
    loop.run_until_complete(asyncio.wait(futures))
    t_end = time()
    print(f"Full fetching got {t_end - t_start:.3f} seconds.")
