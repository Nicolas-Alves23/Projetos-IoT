import serial
import subprocess

PORTA_SERIAL = 'COM5'  # Troque pela porta correta (ex: COM4)
BAUD_RATE = 115200

print("🔌 Aguardando sinal do ESP32...")

try:
    with serial.Serial(PORTA_SERIAL, BAUD_RATE, timeout=1) as ser:
        while True:
            linha = ser.readline().decode('utf-8').strip()
            if linha:
                print("📥 Recebido:", linha)

            if linha == "START":
                print("🚀 Rodando script de OCR...")
                subprocess.run(["python", "leitor_placa.py"])  # Executa o script
except Exception as e:
    print("⚠️ Erro na comunicação serial:", e)
