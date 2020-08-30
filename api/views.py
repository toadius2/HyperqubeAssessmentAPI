from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
import psutil as p


# Create your views here.

def homePage(request):
    return HttpResponse("hello world")


def size(byte):
    # this the function to convert bytes into more suitable reading format.
    # Suffixes for the size
    for x in ["B", "KB", "MB", "GB", "TB"]:
        if byte < 1024:
            return f"{byte:.2f}{x}"
        byte = byte / 1024


# Function to get info about Disk Usage.
def disk(request):
    res = ""
    res += "-" * 50 + "Disk Information" + "-" * 50 + "\n"
    res += "Partitions on Drive:" + "\n"
    par = p.disk_partitions()
    # getting all of the disk partitions
    for x in par:
        res += "Drive: " + str(x.device) + "\n"
        res += " File system type: " + str(x.fstype) + "\n"
        dsk = p.disk_usage(x.mountpoint)
        res += " Total Size: " + str(size(dsk.total)) + "\n"
        res += " Used: " + str(size(dsk.used)) + "\n"
        res += " Free: " + str(size(dsk.free)) + "\n"
        res += " Percentage: " + str(dsk.percent) + "%\n"

    return HttpResponse("<pre>"+res+"<pre>")


#Function to Get memory/Ram usage.
def memory(request):
    res = ""
    res += "-"*50 + "Memory Information" + "-"*50 + "\n"

    #Getting the Memory/Ram Data.
    mem = p.virtual_memory()
    res += "Total Memory: " + str(size(mem.total)) + "\n"
    res += "Available Memory:" + str(size(mem.available)) + "\n"
    res += "Used Memory: "+ str(size(mem.used)) + "\n"
    res += "Percentage: " + str(mem.percent) + "% \n"

    # Getting the Swap Memory Data.
    # It is the Hard disk/ SSD space Which is used up as main memory when the main memory is not sufficient.
    res += "-"*48 + "Swap Memory Information" + "-"*47 + "\n"

    swmem = p.swap_memory()
    res += "Total Memory: " + str(size(swmem.total)) + "\n"
    res += "Available Memory:" + str(size(swmem.free)) + "\n"
    res += "Used Memory: " + str(size(swmem.used)) + "\n"
    res += "Percentage: " + str(swmem.percent) + "%\n"

    return HttpResponse("<pre>" + res + "<pre>")


#Function to get CPU information.

def cpu(request):
    res = ""
    res += "-"*50 + "CPU Information" + "-"*50 + "\n"
    #Getting the logical and physical core count.

    res += "Logical/Total Core Count: " + str(p.cpu_count(logical=True)) + "\n"

    res += "Physical Core Count: " + str(p.cpu_count(logical=False)) + "\n"

    #Getting the CPU Frequencies.
    fre=p.cpu_freq()

    res += "Maximum Frequency:" + str(fre.max) + "Mhz" + "\n"

    res += "Minimum Frequency:" + str(fre.min) + "Mhz" + "\n"

    res += "Current Frequency: " + str(fre.current) + "Mhz" + "\n"

    #Getting the CPU Usage.

    for x, percentage_usage in enumerate(p.cpu_percent(percpu=True)):

        res += "Core " + str(x) + ":" + str(percentage_usage) + "%" + "\n"

        res += "Total CPU Usage:" + str(p.cpu_percent()) + "%\n"

    return HttpResponse("<pre>" + res + "<pre>")