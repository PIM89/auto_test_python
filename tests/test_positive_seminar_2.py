import subprocess

import pytest


def checkout_positive(cmd, text):
    result = subprocess.run(cmd, shell=True, encoding="utf-8", stdout=subprocess.PIPE)
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


folder_in = "/home/zerg/tst"
folder_out = "/home/zerg/out"
folder_ext = "/home/zerg/folder1"


@pytest.fixture(autouse=True, scope='module')
def before_step_tests():
    subprocess.run(
        'cd /home; mkdir zerg/ zerg/tst zerg/out zerg/folder1; echo test >> zerg/tst/test.txt; echo test2 >> zerg/tst/test2.txt',
        encoding='utf-8', shell=True)
    yield
    subprocess.run('cd /home/; rm -rf zerg/', encoding='utf-8', shell=True)


def test_step1():
    assert checkout_positive("cd /home/zerg/tst; 7z a ../out/arx2", "Everything is Ok"), "test_step1 fail"


def test_step2():
    assert checkout_positive("cd /home/zerg/out; 7z e ../out/arx2.7z -o/home/zerg/folder1",
                             "Everything is Ok"), "test_step2 fail"


def test_step3():
    assert checkout_positive("cd /home/zerg/out; 7z t arx2.7z", "Everything is Ok"), "test_step3 fail"


def test_step4():
    assert checkout_positive("cd {}; echo upgrade_file >> test.txt; cd {}; 7z u arx2.7z".format(folder_in, folder_out),
                             "Everything is Ok"), "test_step4 fail"


def test_step5():
    assert checkout_positive("cd {}; 7z d arx2.7z".format(folder_out),
                             "Everything is Ok"), "test_step5 fail"
