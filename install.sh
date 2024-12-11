#!/usr/bin/env bash
set -e

echo "Определяем дистрибутив..."

if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS_ID=$ID
    OS_ID_LIKE=$ID_LIKE
else
    echo "Невозможно определить дистрибутив. Установите psutil и blessed вручную."
    exit 1
fi

# Проверяем по ID и ID_LIKE
if [ "$OS_ID" = "arch" ] || [ "$OS_ID" = "manjaro" ] || [[ "$OS_ID_LIKE" =~ "arch" ]]; then
    echo "Arch/Manjaro-система обнаружена. Устанавливаем зависимости..."
    sudo pacman -Sy --noconfirm python-psutil python-blessed
elif [ "$OS_ID" = "ubuntu" ] || [ "$OS_ID" = "debian" ] || [[ "$OS_ID_LIKE" =~ "debian" ]]; then
    echo "Debian/Ubuntu обнаружен. Устанавливаем зависимости..."
    sudo apt update
    sudo apt install -y python3-psutil python3-blessed
else
    echo "Ваш дистрибутив не поддержан автоматически. Установите psutil и blessed через пакетный менеджер."
    echo "Например, для Fedora: sudo dnf install python3-psutil python3-blessed"
    exit 1
fi

echo "Копируем mtop в /usr/local/bin/..."
sudo cp mtop.py /usr/local/bin/mtop
sudo chmod +x /usr/local/bin/mtop

echo "Установка завершена! Используйте 'mtop' или 'mtop -g' для запуска."
