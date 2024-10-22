import subprocess

def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, encoding="utf-8", stdout=subprocess.PIPE)
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False

def test_step1():
    assert checkout("cd /home/zerg/tst; 7z a ../out/arx2", "Everything is Ok"), "test_step1 fail"

def test_step2():
    assert checkout("cd /home/zerg/out; 7z e ../out/arx2.7z -o/home/zerg/folder1 -y", "Everything is Ok"), "test_step2 fail"

def test_step3():
    assert checkout("cd /home/zerg/out; 7z t arx2.7z", "Everything is Ok"), "test_step3 fail"