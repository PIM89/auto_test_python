import subprocess


def checkout_negative(cmd, text):
    result = subprocess.run(cmd, shell=True, encoding="utf-8", stdout=subprocess.PIPE)
    if text in result.stdout and result.returncode == 0:
        return False
    else:
        return True


folder_in = "/home/zerg/tst"
folder_out = "/home/zerg/out"
folder_ext = "/home/zerg/folder1"


def test_negative_step1():
    assert checkout_negative("cd {}; 7z e arx3.7z -o{}".format(folder_out, folder_ext),
                             "ERROR: "), "test_negative_step1 fail"


def test_negative_step2():
    assert checkout_negative("cd {}; 7z t arx3.7z".format(folder_out), "ERROR: "), "test_negative_step2 fail"
