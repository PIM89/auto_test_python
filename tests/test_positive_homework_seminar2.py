import subprocess

import pytest


def checkout_positive(cmd, text):
    result = subprocess.run(cmd, shell=True, encoding="utf-8", stdout=subprocess.PIPE)
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


@pytest.fixture(autouse=True, scope='module')
def before_step_tests():
    subprocess.run('cd /home; mkdir zerg/ zerg/tst/ zerg/tst/folder zerg/out zerg/folder1;\
                    echo test >> zerg/tst/test.txt;\
                    echo test2 >> zerg/tst/folder/test2.txt',
                   encoding='utf-8', shell=True)
    yield
    subprocess.run('cd /home/; rm -rf zerg/', encoding='utf-8', shell=True)


folder_in = "/home/zerg/tst"
folder_out = "/home/zerg/out"
folder_ext = "/home/zerg/folder1"


# Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и разархивирования с путями (x).

def test_7z_listing_arch():
    res_arch = checkout_positive("cd {}; 7z a ../out/arx2".format(folder_in), "Everything is Ok")
    res_view_file1 = checkout_positive("cd {}; 7z l arx2.7z".format(folder_out), "test.txt")
    res_view_file2 = checkout_positive("cd {}; 7z l arx2.7z".format(folder_out), "test2.txt")
    assert res_arch and res_view_file1 and res_view_file2, "test_7z_listing_arch fail"

def test_7z_check_path():
    res_view_file2 = checkout_positive("cd {}; 7z l arx2.7z".format(folder_out), "folder/test2.txt")
    assert res_view_file2, "test_7z_check_path fail"

# Доработать проект, добавив тест команды расчёта хеша (h). Проверить, что хеш совпадает с рассчитанным командой crc32.

def test_7z_hash():
    res_crc32 = subprocess.run("cd {}; crc32 arx2.7z".format(folder_out), shell=True, encoding="utf-8", stdout=subprocess.PIPE)
    res_compare_hash = checkout_positive("cd {}; 7z h arx2.7z".format(folder_out), res_crc32.stdout.upper())
    assert res_compare_hash, "test_7z_hash fail"
