# exit(777)  # для запрета запуска кода, иначе перепишет результаты
import functions
import os
import pandas as pd
from datetime import datetime
from binance import Client
from my_config.trade_config import Config  # Файл конфигурации торгового робота
from my_config.Config import My_Config  # Файл конфигурации торгового робота


def get_candles(ticker, timeframes, ts_start, ts_end):
    """Функция получения свечей с Binance."""
    for timeframe in timeframes:
        data = []
        for kline in client.get_historical_klines_generator(ticker, timeframe, str(ts_start), str(ts_end)):
            normal_date = datetime.fromtimestamp(kline[0] / 1000).strftime(
                '%Y-%m-%d %H:%M:%S')  # преобразование timestamp в дату формата YYYY-MM-DD
            item = normal_date, float(kline[1]), float(kline[2]), float(kline[3]), float(kline[4]), float(kline[5])

            print(ticker, timeframe, normal_date)
            data.append(item)

        df = pd.DataFrame(data)

        df.columns = ["datetime", "open", "high", "low", "close", "volume"]
        df.to_csv(os.path.join("csv", f"{ticker}_{timeframe}.csv"), index=False, encoding='utf-8', sep=',')
        print(f"{ticker} {timeframe}:")
        print(df)


def get_all_historical_candles(portfolio, timeframes, start, end):
    for instrument in portfolio:
        get_candles(instrument, timeframes, start, end)


if __name__ == "__main__":
    # применение настроек из config.py
    client = Client(My_Config.KEY, My_Config.SECRET)  # создаем переменную и передаем туда наши ключи
    portfolio = Config.portfolio  # тикеры по которым скачиваем исторические данные
    timeframe_0 = Config.timeframe_0  # таймфрейм для обучения нейросети - вход
    timeframe_1 = Config.timeframe_1  # таймфрейм для обучения нейросети - выход
    start = datetime.strptime(Config.start,
                              '%Y-%m-%d').timestamp() * 1000  # с какой даты загружаем исторические данные с Binance
    if Config.end != "":
        end = datetime.strptime(Config.end, '%Y-%m-%d').replace(hour=23, minute=59, second=59).timestamp() * 1000
    else:
        end = datetime.today().replace(hour=23, minute=59, second=59).timestamp() * 1000

    # создаем необходимые каталоги
    functions.create_some_folders(timeframes=[timeframe_0, timeframe_1])

    # получения исторических данных
    get_all_historical_candles(  # запуск получения исторических данных с MOEX
        portfolio=portfolio,
        timeframes=[timeframe_0, timeframe_1],  # по каким таймфреймам скачиваем данные
        start=start,
        end=end,
    )
