import requests

class Game():
    def __init__(self):
        self.deck_id: str
        self.isStart = 0
    async def shuffle(self, deck_count = 1):
        endPoint = f'https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count={deck_count}'
        res = requests.get(endPoint).json()
        self.deck_id = res['deck_id']

    async def getCard(self, count: int = 1) -> tuple[str, str]:
        if self.isStart == 0:
            endPoint = f'https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count={1}'
            res = requests.get(endPoint).json()
            self.deck_id = res['deck_id']
            self.isStart += 1
        endPoint = f'https://deckofcardsapi.com/api/deck/{self.deck_id}/draw/?count={count}'
        res = requests.get(endPoint).json()
        return (res['cards'][0]['image'], res['cards'][0]['value'])