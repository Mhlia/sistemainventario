from datetime import datetime

def fecha_actual(request): #Procesor para obtener la fecha actual
    return {
        'fecha': datetime.today().strftime('%d/%m/%Y')
    }