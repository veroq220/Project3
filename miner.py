import hashlib
import requests
import json

# Задаем адрес пула и адрес кошелька для получения вознаграждения
POOL_URL = "pool.hashvault.pro:443"
WALLET_ADDRESS = "46yMqjCATstfj2EZpTNq2rE9UkCfPkkfpbzGMYKBzf6Z7YPCrAgGRiqVjhVQZ4zW2oPqRx89hujwXbDf5GFNmeduLuMiY8z"

# Функция, которая производит добычу
def mine():

    # Получаем работу от пула
    response = requests.get(POOL_URL)
    job = json.loads(response.text)

    # Извлекаем данные из полученной работы
    block_number = job["block_number"]
    difficulty = job["difficulty"]
    block_hash = job["block_hash"]
    nonce = 0

    # Выполняем цикл поиска правильного nonce
    while True:
        # Собираем сообщение для хеширования
        message = str(block_number) + WALLET_ADDRESS + str(nonce)

        # Вычисляем хеш сообщения
        hash = hashlib.new('cryptonight')
        hash.update(message.encode('utf-8'))
        digest = hash.digest()

        # Проверяем, удовлетворяет ли хеш сложности
        if int.from_bytes(digest, byteorder='little') < difficulty:
            # Если нашли правильный nonce, отправляем результат на сервер пула
            data = {"block_number": block_number, "nonce": nonce, "result": digest.hex(), "wallet_address": WALLET_ADDRESS}
            response = requests.post(POOL_URL, data=json.dumps(data))
            print(response.text)
            break

        # Если не нашли правильный nonce, пробуем следующий
        nonce += 1

if __name__ == "__main__":
    mine()