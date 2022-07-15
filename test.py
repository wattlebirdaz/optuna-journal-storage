import os
from journal import JournalStorage
from optuna.storages import InMemoryStorage


def cleanup():
    os.system("rm -rf ./openlock")
    os.system("rm ./operation_logs")


def test1():
    cleanup()
    s = JournalStorage()
    s.create_new_study()


if __name__ == "__main__":
    test1()
