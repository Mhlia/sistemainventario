from datetime import datetime

def fecha_actual(request):
    return {
        'fecha': datetime.today().strftime('%d/%m/%Y')
    }