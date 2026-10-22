import psutil

print ( " --- Monitorizando el Sistema Local ---" )

# 1. Uso de CPU
# interval =1 significa que mide durante 1 segundo
cpu_uso = psutil.cpu_percent(interval=1)

print(f" Uso actual de CPU : { cpu_uso } %")