## Баг-репорт

### Баг #1. Отображение отрицательного значения счетчиков при получении отрицательных данных от бэкенда.

- **Тип:** нефункциональный
- **Приоритет:** средний
- **Серьёзность:** незначительная
- **Ответственный за исправление:** бэкенд/микрофронтенд

#### Воспроизведение:
1. **Шаги воспроизведения:** Получение отрицательных значений от бэкенда.
2. **Ожидаемый результат:** Полученные отрицательные значения не отражаются на счётчиках, значения выражены неотрицательными числами, присутствует затемнение.
3. **Фактический результат:** Полученные от бэкенда отрицательные значения отображаются на счётчиках, затемнение отсутствует.

### Баг #2. Отсутствует замена и пересчёт единиц измерения из килограммов в тонны и из киловаттов в мегаватты.

- **Тип:** нефункциональный
- **Приоритет:** средний
- **Серьёзность:** незначительная
- **Ответственный за исправление:** микрофронтенд

#### Воспроизведение:
1. **Шаги воспроизведения:** Получение от бэкенда значения счётчиков, равных или превышающих 1 000 000.
2. **Ожидаемый результат:** При проверке отображения значений счётчиков, равных или превышающих 1 000 000, происходит замена единиц измерения (килограммы в тонны, киловатты в мегаватты).
3. **Фактический результат:** Значения счётчиков, равных или превышающих 1 000 000, отображаются без замены единиц измерения (килограммы в тонны, киловатты в мегаватты).

### Баг #3. Наложение строк при подсчёте значения счетчика сэкономненной электроэнергии.

- **Тип:** нефункциональный
- **Приоритет:** средний
- **Серьезность:** незначительная
- **Ответственный за исправление:** микрофронтенд

#### Воспроизведение:
1. **Шаги воспроизведения:** Получение от бэкенда значения счётчиков, равных или превышающих 1 000 000.
2. **Ожидаемый результат:** Имеющаяся текстовая информация читаема и хорошо различима.
3. **Фактический результат:** Произошло наложение строки с названием единиц измерения с пояснительной строкой <em>"было сэкономлено"</em>. при отображении значения счётчика сэкономленной электроэнергии, равному или превышающему 1 000 000.