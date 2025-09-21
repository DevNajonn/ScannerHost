import subprocess


port = 0
while(port < 255):

        porta = str(port)

        comando = "ping -n 1 192.168.0." + porta


        try:
            

            saida = subprocess.check_output(comando, shell=True, text=True)

            if "Recebidos = 1" in saida or "Received = 1" in saida:
                print(f"192.168.0.{port} Esta ativo" )
            else:
                print(f"192.168.0.{port} Não esta ativo")

            

        except subprocess.CalledProcessError as e:
                print("Nao respondeu:")
                print(e.output)


        port = port + 1