# mtop

`mtop` — простой монитор системных ресурсов (CPU, MEM, GPU) для Linux. Поддерживает как текстовый вывод, так и отображение данных в виде текстовых баров.

## Особенности

- Показывает загрузку CPU, память и GPU (если доступны `nvidia-smi` для NVIDIA или `rocm-smi` для AMD).
- Работает в двух режимах:
  - Однократный вывод (по умолчанию).
  - Непрерывный режим (`-r`) с периодическим обновлением данных.
- Графический режим (`-g`) с текстовыми барами.

## Установка

   ```bash
   git clone https://example.com/your-repo/mtop.git
   cd mtop
  /install.sh
