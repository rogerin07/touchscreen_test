import subprocess
import random
import time

MAX_X = 1079
MAX_Y = 2339

def ensure_screen_on():
    """Garante que a tela está ligada e desbloqueada"""
    subprocess.run("adb shell input keyevent KEYCODE_WAKEUP".split())
    subprocess.run("adb shell input keyevent KEYCODE_MENU".split())

def tap_random():
    x = random.randint(0, MAX_X)
    y = random.randint(0, MAX_Y)
    print(f"Clicando em ({x}, {y})")
    subprocess.run(f"adb shell input tap {x} {y}".split())

def main():
    ensure_screen_on()
    print("Iniciando toques automáticos. Pressione Ctrl+C para sair.")
    try:
        while True:
            tap_random()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nInterrompido pelo usuário.")

if __name__ == "__main__":
    main()
