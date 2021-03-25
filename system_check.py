import psutil
import shutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage
