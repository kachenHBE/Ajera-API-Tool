"""
Filename: main.py
Description: 
Author: Kai Achen
Last Updated: 10/06/2026
Inputs: 
Outputs: 
"""

import os
import asyncio
from session_setup import create_api_session
from excel_input import main as excel_input_main
from ajera import AsyncAjeraClient


async def main():
    print("main")
    new_tuples = excel_input_main()
    print("excel_input success")
    print(new_tuples)
    """async with AsyncAjeraClient() as client:
        projects = await client.list_projects()
        limit = asyncio.Semaphore(5)

        async def totals(project_key: int):
            async with limit:
                return await client.get_project_totals(project_key)
        for total in await asyncio.gather(
            *(totals(project.project_key) for project in projects)
        ):
            print(total.project_key, total.totals)"""


if __name__ == "__main__":
    asyncio.run(main())