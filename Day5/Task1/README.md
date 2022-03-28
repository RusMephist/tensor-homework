# Day 5

| Task | Link                                                                              |
| :--: | --------------------------------------------------------------------------------- |
|  1   | [Progress dd](https://github.com/RusMephist/tensor-homework/tree/main/Day5/Task1) |

## Task 1

### Commands

```bash
mkdir /tmp/temp-prog-volume
docker run --device-write-bps /dev/nvme0n1:5mb -v /tmp/temp-prog-volume:/var/log --rm -d -it dd:latest
docker run -v /tmp/temp-prog-volume:/var/log --rm -d -it mon:latest
```

### Screenshots

![alt text](https://github.com/RusMephist/tensor-homework/blob/main/images/Screenshot_20220328_112039.png?raw=true)
