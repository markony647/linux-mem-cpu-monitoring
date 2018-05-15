# linux-mem-cpu-monitoring

This is utility that measures CPU and Memory metrics written in Python.
The service is running inside Docker container and measures metrics from you host macine.


### Install

Build from Dockerfile:

    docker build -t gl_task -f Dockerfile .
    
    
### Run

Run the image:

    docker run --pid=host -v /proc/:/app/proc:ro -it gl_task /bin/bash
    
### Use monitor script

Inside the docker container run following command to get CPU or MEM usage:

    python mem_cpu_monitor.py cpu
    python mem_cpu_monitor.py mem
