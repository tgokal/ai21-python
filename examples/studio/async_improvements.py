import asyncio

from ai21 import AsyncAI21Client
from ai21.models import ImprovementType

client = AsyncAI21Client()


async def main():
    response = await client.improvements.create(
        text="Affiliated with the profession of project management,"
        " I have ameliorated myself with a different set of hard skills as well as soft skills.",
        types=[ImprovementType.FLUENCY],
    )

    print(response.improvements[0].original_text)
    print(response.improvements[0].suggestions)
    print(response.improvements[0].suggestions[0])
    print(response.improvements[0].improvement_type)
    print(response.improvements[1].start_index)
    print(response.improvements[1].end_index)


asyncio.run(main())
