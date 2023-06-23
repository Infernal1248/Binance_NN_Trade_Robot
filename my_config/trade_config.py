# конфигурационный файл для торговой стратегии

class Config:

    training_NN = {"ETHUSDT", "BTCUSDT"}  # тикеры по которым обучаем нейросеть
    portfolio = {"ETHUSDT", "BTCUSDT"}  # тикеры по которым торгуем и скачиваем исторические данные

    # доступные m1, 5m, 15m
    timeframe_0 = "1m"  # таймфрейм для обучения нейросети - вход и на этом же таймфрейме будем торговать
    timeframe_1 = "5m"  # таймфрейм для обучения нейросети - выход
    start = "2022-01-01"  # с какой даты берем данные с Binance
    end = "2023-06-21"  # по какую дату берем данные с Binance, если оставить пустым, то выбирает начало текущего дня

    # параметры для отрисовки картинок
    period_sma_slow = 64  # период медленной SMA
    period_sma_fast = 16  # период быстрой SMA
    draw_window = 128  # окно данных
    steps_skip = 16  # шаг сдвига окна данных
    draw_size = 128  # размер стороны квадратной картинки