## Тест-кейс #1: Проверка отображения счётчиков с нулевыми значениями

### Предусловие
Бэкенд возвращает нулевые значения счётчиков. 

### Шаги тестирования
| № шага | Шаг                                                                 | Ожидаемый результат                                             |
|--------|---------------------------------------------------------------------|------------------------------------------------------------------|
| 1      | Проверить, что единицы измерения соответствуют ожидаемым. | В качестве единиц измерения используются литры для объёма воды, килограммы для выброса CO<sub>2</sub> и килловатт-часы для электроэнергии.                      |
| 2      | Проверить значения счётчиков.          | Значения всех счётчиков корректно отображаются и равны нулю.     |
| 3      | Проверить отображение изображений счётчиков. | Изображения всех счётчиков отображаются с затемнением.                      |
| 4      | Получить скриншоты счётчиков.                                         | Скриншоты счётчиков успешно созданы.      |

## Тест-кейс #2: Проверка отображения счётчиков с отрицательными значениями

### Предусловие
Бэкенд возвращает отрицательные значения счётчиков. 

### Шаги тестирования
| № шага | Шаг                                                                 | Ожидаемый результат                                             |
|--------|---------------------------------------------------------------------|------------------------------------------------------------------|
| 1      | Проверить, что единицы измерения соответствуют ожидаемым. | В качестве единиц измерения используются литры для объёма воды, килограммы для выброса CO<sub>2</sub> и киловатт-часы для электроэнергии.                      |
| 2      | Проверить значения счётчиков.          | Значения всех счётчиков корректно отображаются и равны нулю (т.к. значения невалидны).     |
| 3      | Проверить отображение изображений счётчиков. | Изображения всех счётчиков отображаются с затемнением.                      |
| 4      | Получить скриншоты счётчиков.                                         | Скриншоты счётчиков успешно созданы.      |

## Тест-кейс #3: Проверка отображения счётчиков со значениями, лежащими в диапазоне от 1 до 999

### Предусловие
Бэкенд возвращает значения счётчиков, лежащие в диапазоне от 1 до 999. 

### Шаги тестирования
| № шага | Шаг                                                                 | Ожидаемый результат                                             |
|--------|---------------------------------------------------------------------|------------------------------------------------------------------|
| 1      | Проверить, что единицы измерения соответствуют ожидаемым. | В качестве единиц измерения используются литры для объёма воды, килограммы для выброса CO<sub>2</sub> и киловатт-часы для электроэнергии.                      |
| 2      | Проверить значения счётчиков.          | Значения всех счётчиков корректно отображаются и равны получаемым от бэкенда значениям.     |
| 3      | Проверить отображение изображений счётчиков. | Изображения всех счётчиков отображаются без затемнения.                      |
| 4      | Получить скриншоты счётчиков.                                         | Скриншоты счётчиков успешно созданы.      |

## Тест-кейс #4: Проверка отображения счётчиков со значениями, лежащими в диапазоне от 1000 до 999 999

### Предусловие
Бэкенд возвращает значения счётчиков, лежащие в диапазоне от 1000 до 999 999. 

### Шаги тестирования
| № шага | Шаг                                                                 | Ожидаемый результат                                             |
|--------|---------------------------------------------------------------------|------------------------------------------------------------------|
| 1      | Проверить, что единицы измерения соответствуют ожидаемым. | В качестве единиц измерения используются кубические метры для объёма воды, тонны для выброса CO<sub>2</sub> и мегаватт-часы для электроэнергии.                      |
| 2      | Проверить значения счётчиков.          | Значения всех счётчиков корректно отображаются и равны значениям, полученным от бэкенда, округлённым и приведённым к виду с одним знаком после запятой. Если знак после запятой ненулевой, то символ запятой присутствует на счётчике.     |
| 3      | Проверить отображение изображений счётчиков. | Изображения всех счётчиков отображаются без затемнения.                      |
| 4      | Получить скриншоты счётчиков.                                         | Скриншоты счётчиков успешно созданы.      |

## Тест-кейс #5: Проверка отображения счётчиков со значениями, большими или равными 1 000 000

### Предусловие
Бэкенд возвращает значения счётчиков больше или равные 1 000 000. 

### Шаги тестирования
| № шага | Шаг                                                                 | Ожидаемый результат                                             |
|--------|---------------------------------------------------------------------|------------------------------------------------------------------|
| 1      | Проверить, что единицы измерения соответствуют ожидаемым. | В качестве единиц измерения используются кубические метры для объёма воды, тонны для выброса CO<sub>2</sub> и мегаватт-часы для электроэнергии.                      |
| 2      | Проверить значения счётчиков.          | Значения всех счётчиков корректно отображаются и равны значениям, полученным от бэкенда, округлённым и приведённым к виду с одним знаком после запятой. Если знак после запятой ненулевой, то символ запятой присутствует на счётчике.     |
| 3      | Проверить отображение изображений счётчиков. | Изображения всех счётчиков отображаются без затемнения.                      |
| 4      | Получить скриншоты счётчиков.                                         | Скриншоты счётчиков успешно созданы.      |