#!/usr/bin/env python3
import argparse
import psutil
import subprocess
import time
import shutil
import sys
from blessed import Terminal

def get_gpu_usage():
    try:
        output = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=utilization.gpu", "--format=csv,noheader,nounits"],
            stderr=subprocess.DEVNULL
        ).decode('utf-8').strip()
        gpu_util = int(output)
        return gpu_util
    except:
        return None

def draw_bar(value, width=30, char='█'):
    filled = int(value * width / 100)
    bar_str = char * filled + ' ' * (width - filled)
    return bar_str

def print_stats(cpu, mem, gpu, graph_mode=False, term_width=80):
    """
    Печатает статистику. Если graph_mode=True, то рисует бары.
    Иначе просто цифры.
    """
    if graph_mode:
        bar_width = max(10, term_width - 20)  # расширим длину баров

        print("CPU Usage:")
        bar_cpu = draw_bar(cpu, width=bar_width)
        print(f"[{bar_cpu}] {cpu:.1f}%\n")

        print("Memory Usage:")
        bar_mem = draw_bar(mem, width=bar_width)
        print(f"[{bar_mem}] {mem:.1f}%\n")

        print("GPU Usage:")
        if gpu is not None:
            bar_gpu = draw_bar(gpu, width=bar_width)
            print(f"[{bar_gpu}] {gpu}%")
        else:
            print("N/A")
    else:
        # Текстовый режим без баров
        print(f"CPU: {cpu}%")
        print(f"MEM: {mem}%")
        if gpu is not None:
            print(f"GPU: {gpu}%")
        else:
            print("GPU: N/A")

def main():
    parser = argparse.ArgumentParser(
        description="mtop - упрощенный монитор ресурсов (CPU, MEM, GPU)",
        epilog="Примеры:\n  mtop\n  mtop -g\n  mtop -r\n  mtop -r -g\n\nДля помощи: 'mtop --help'"
    )
    parser.add_argument('-g', '--graph', action='store_true', help='Отображать данные в виде графиков')
    parser.add_argument('-r', '--run', action='store_true', help='Запустить в непрерывном режиме')
    parser.add_argument('-i', '--interval', type=float, default=1.0, help='Интервал обновления в секундах')

    try:
        args = parser.parse_args()
    except SystemExit:
        sys.exit(1)

    term = Terminal()
    # Поведение в зависимости от аргументов:
    # - Без аргументов: один вывод и выход
    # - -g без -r: один вывод в графическом режиме
    # - -r без -g: непрерывный режим без графики
    # - -r -g: непрерывный режим с графикой

    graph_mode = args.graph
    continuous = args.run

    if not continuous:
        # Однократный вывод
        cpu = psutil.cpu_percent(interval=0)
        mem = psutil.virtual_memory().percent
        gpu = get_gpu_usage()

        # Простой вывод без очистки экрана, т.к. один раз
        if graph_mode:
            print_stats(cpu, mem, gpu, graph_mode=True, term_width=term.width)
        else:
            print_stats(cpu, mem, gpu, graph_mode=False, term_width=term.width)
        # Выходим
        sys.exit(0)
    else:
        # Непрерывный режим
        try:
            with term.fullscreen(), term.cbreak(), term.hidden_cursor():
                while True:
                    cpu = psutil.cpu_percent(interval=None)
                    mem = psutil.virtual_memory().percent
                    gpu = get_gpu_usage()

                    print(term.home + term.clear)
                    mode_str = "(graph mode)" if graph_mode else "(normal mode)"
                    print((f" mtop {mode_str} ").center(term.width, '='))
                    print()

                    print_stats(cpu, mem, gpu, graph_mode=graph_mode, term_width=term.width)

                    print()
                    print("Нажмите Ctrl+C для выхода")

                    time.sleep(args.interval)
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    main()
