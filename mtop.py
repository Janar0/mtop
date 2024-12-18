#!/usr/bin/env python3
import argparse
import psutil
import subprocess
import time
import sys
from blessed import Terminal
import shutil

def get_gpu_usage():
    if shutil.which("nvidia-smi"):
        try:
            output = subprocess.check_output(
                ["nvidia-smi", "--query-gpu=utilization.gpu", "--format=csv,noheader,nounits"],
                stderr=subprocess.DEVNULL
            ).decode('utf-8').strip()
            gpu_util = int(output)
            return gpu_util
        except:
            pass

    if shutil.which("rocm-smi"):
        try:
            output = subprocess.check_output(
                ["rocm-smi", "--showuse"],
                stderr=subprocess.DEVNULL
            ).decode('utf-8', errors='ignore')
            for line in output.splitlines():
                line = line.strip()
                if "GPU use:" in line:
                    # Пример строки: "GPU[0]: GPU use: 45%"
                    parts = line.split(":")
                    if len(parts) >= 3 and "GPU use" in parts[1]:
                        usage_part = parts[-1].strip()
                        if usage_part.endswith('%'):
                            val_str = usage_part[:-1].strip()
                            return int(val_str)
        except:
            pass

    return None

def draw_bar(value, width=30, char='█'):
    filled = int(value * width / 100)
    bar_str = char * filled + ' ' * (width - filled)
    return bar_str

def print_stats(cpu, mem, gpu, graph_mode=False, term_width=80):
    if graph_mode:
        bar_width = max(10, term_width - 20)

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
        print(f"CPU: {cpu}%")
        print(f"MEM: {mem}%")
        if gpu is not None:
            print(f"GPU: {gpu}%")
        else:
            print("GPU: N/A")

def main():
    parser = argparse.ArgumentParser(
        description="mtop - упрощенный монитор ресурсов (CPU, MEM, GPU)",
        epilog="Примеры:\n  mtop             # Один вывод без графики\n  mtop -g          # Один вывод с графикой\n  mtop -r          # Непрерывный режим без графики\n  mtop -r -g       # Непрерывный режим с графикой\n\nДля помощи: 'mtop --help'"
    )
    parser.add_argument('-g', '--graph', action='store_true', help='Отображать данные в виде графиков')
    parser.add_argument('-r', '--run', action='store_true', help='Запустить в непрерывном режиме')
    parser.add_argument('-i', '--interval', type=float, default=1.0, help='Интервал обновления в секундах')
    
    try:
        args = parser.parse_args()
    except SystemExit:
        sys.exit(1)

    term = Terminal()

    graph_mode = args.graph
    continuous = args.run

    if not continuous:
        # Один раз: добавим задержку при измерении CPU
        cpu = psutil.cpu_percent(interval=0.5)
        mem = psutil.virtual_memory().percent
        gpu = get_gpu_usage()

        if graph_mode:
            print_stats(cpu, mem, gpu, graph_mode=True, term_width=term.width)
        else:
            print_stats(cpu, mem, gpu, graph_mode=False, term_width=term.width)
        sys.exit(0)
    else:
        # Непрерывный режим
        try:
            with term.fullscreen(), term.cbreak(), term.hidden_cursor():
                # Первый замер CPU с задержкой для корректных показаний
                cpu = psutil.cpu_percent(interval=0.5)
                while True:
                    # Последующие замеры без задержки, так как есть постоянный поток данных
                    # Но можно оставить небольшую задержку, если хотите всегда более сглаженные данные:
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