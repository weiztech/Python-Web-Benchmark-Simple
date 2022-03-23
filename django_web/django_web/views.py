import asyncio
from django.http import JsonResponse

async def api(request):
    await asyncio.sleep(2)
    return JsonResponse({'hello': 'world'})
