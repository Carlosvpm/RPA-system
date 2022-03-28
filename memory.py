
from datetime import datetime
from platform import platform
import psutil
from size import get_size
from sms import send_sms
import platform




def get_memory():
    uname = platform.uname()
    svmem = psutil.virtual_memory()
    print(f'{svmem.percent}%')
    if svmem.percent > 50:
        return send_sms(f"WARNING: \n Consumo de memória ultrapassou os 50%. \n - Ocorreu em: {datetime.now().strftime('%d-%m-%Y ás %H:%M')} \n - Especificações da máquina: \n Sistema: {uname.system}\n Nome da máquina: {uname.node} \n Release: {uname.release} \n Versão: {uname.version} \n   \n Total: {get_size(svmem.total)} \n Disponível: {get_size(svmem.available)} \n Usados: {get_size(svmem.used)} \n Porcentagem: {svmem.percent}% \n Uso total da CPU: {psutil.cpu_percent()}% ")

