import asyncio
from session_setup import create_api_session
from ajera import AjeraClient

async def main():
    print("main")
    async with AsyncAjeraClient() as client:
        projects = await client.list_projects()
        limit = asyncio.Semaphore(5)

        async def totals(project_key: int):
            async with limit:
                return await client.get_project_totals(project_key)
        for total in await asyncio.gather(
            *(totals(project.project_key) for project in projects)
        ):
            print(total.projecT_key, total.totals)


if __name__ == "__main__":
    asyncio.run(main())