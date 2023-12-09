import os
import shutil
from threading import Thread


def copy_dir(source, destination):
    total_files = 0
    total_dirs = 0

    for root, dirs, files in os.walk(source):
        dest_dir = os.path.join(destination, os.path.relpath(root, source))
        os.makedirs(dest_dir, exist_ok=True)

        for file in files:
            source_file = os.path.join(root, file)
            dest_file = os.path.join(dest_dir, file)
            shutil.copy2(source_file, dest_file)
            total_files += 1

        total_dirs += 1

    print(f"Скопировано файлов: {total_files}")
    print(f"Скопировано директорий: {total_dirs}")


def main():
    source_dir = input("Введите путь к исходной директории: ")
    destination_dir = input("Введите путь к новой директории: ")
    copy_thread = Thread(target=copy_dir, args=(source_dir, destination_dir))
    copy_thread.start()
    copy_thread.join()


if __name__ == '__main__':
    main()
