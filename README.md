# Проект mtop: Продвинутое решение для мониторинга ресурсов

## Описание проекта

**mtop** — это высокоэффективное программное решение, разработанное на базе языка Python, которое обеспечивает мониторинг вычислительных ресурсов, таких как CPU, RAM и GPU. Проект создан для упрощения рутинных задач системного администрирования и значительного повышения продуктивности специалистов. Более того, mtop способствует снижению экологического воздействия за счёт рационального использования аппаратного обеспечения, что выделяет его среди аналогов.

Современные вычислительные системы нуждаются в постоянном контроле и анализе, что требует значительных затрат времени и ресурсов. **mtop** предоставляет удобный инструмент для снижения нагрузки на системных администраторов, минимизирует риск ошибок и оптимизирует использование аппаратных ресурсов. Применение Python обеспечивает высокую гибкость и производительность, что делает проект адаптивным к различным сценариям.

## Цели и задачи

### 1. Совершенствование мониторинга вычислительных систем

- Создание интуитивно понятного и высокофункционального интерфейса для визуализации ключевых метрик (CPU, RAM, GPU) в режиме реального времени.
- Автоматизация процессов управления системными ресурсами.
- Повышение точности оценки состояния систем благодаря стандартизированным алгоритмам анализа.

### 2. Снижение временных и когнитивных затрат специалистов

- Оптимизация администрирования за счёт использования мощных библиотек Python и модульной архитектуры.
- Универсальность инструмента, позволяющая адаптировать его под разнообразные условия эксплуатации.
- Стандартизация рабочих процессов, что уменьшает вероятность ошибок, связанных с человеческим фактором.

### 3. Вклад в экологическую устойчивость

- Уменьшение износа периферийных устройств и сокращение образования микропластика.
- Эффективное управление энергопотреблением, что способствует снижению углеродного следа.
- Поддержка удалённого администрирования, уменьшающего транспортные расходы и затраты времени.

## Ключевые функции

- **Визуализация данных:** Настраиваемое отображение информации о загрузке ресурсов для анализа и диагностики.
- **Гибкость параметров:** Возможность управления временными интервалами обновления и выбор режима отображения (графика или текст).
- **Модульная структура:** Удобство расширения функциональности и долгосрочная поддержка проекта.

## Установка

1. Скачайте репозиторий:

   ```bash
   git clone https://github.com/Janar0/mtop.git
   ```

2. Перейдите в папку проекта:

   ```bash
   cd mtop
   ```

3. Установите проект:

   ```bash
   sudo bash ./install.sh
   ```

4. Запустите утилиту:

   ```bash
   mtop
   ```

## Использование

**Описание командной строки:**

- `mtop` — один вывод без графики.
- `mtop -g` — один вывод с графикой.
- `mtop -r` — непрерывный режим без графики.
- `mtop -r -g` — непрерывный режим с графикой.

**Примеры использования:**

- Для запуска мониторинга выполните:

  ```bash
  mtop
  ```

- Для получения помощи по параметрам:

  ```bash
  mtop --help
  ```

[##Как создавался проект](creating.md)

## Лицензия

Проект распространяется под лицензией MIT. Подробности указаны в файле LICENSE.

**mtop** — ваш надёжный помощник в мониторинге ресурсов!

