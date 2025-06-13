import asyncio
import websockets
import json
from django.core.management.base import BaseCommand
from alerts.models import Alert
from alerts.views import send_mail
from asgiref.sync import sync_to_async


class Command(BaseCommand):
  help = 'Start the price listener for alerts'
  
  async def price_listener(self):
    uri = "wss://stream.binance.com:9443/ws/btcusdt@ticker"
    async with websockets.connect(uri) as websocket:
      while True:
        data = await websocket.recv()
        price_data = json.loads(data)
        current_price = float(price_data['c'])
        await self.check_alerts(current_price)
        await asyncio.sleep(60)

  async def check_alerts(self, current_price):
    alerts = await sync_to_async(list)(Alert.objects.filter(target_price__lte=current_price, status='created'))
    for alert in alerts:
      send_mail(alerts.user.email, alert.cryptocurrency, alert.target_price)
      alert.status = 'triggered'
      alert.save()

  def handle(self, *args, **kwargs):
    asyncio.run(self.price_listener())
