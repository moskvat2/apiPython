import os, paramiko, platform, time, pwinput

system = platform.system() # Identifica o tipo de sistema operacional

if system == 'Windows':
    pingCheck = "ping -n 1"
elif system == 'Linux':
    pingCheck = "ping -c 1"
else:
    print("\nSistema operacional desconhecido\n")
    response = 1


def executeCommand(ip, command, user, passwd):
    response = os.system(pingCheck + " " + ip)
    
    if response == 0:
        print("\nComunicação feita com sucesso: " + ip)

        # Conexão via SSH com envio de comando
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port=4022, username=user, password=passwd)
        
        stdin, stdout, stderr = ssh.exec_command(command)

        output = stdout.read().decode("utf-8")
        print("\n >>> Comando enviado com sucesso: " + output)

        ssh.close()
        
        time.sleep(3)
        return
    else:
        print("\n >>> Falha na comunicação com o endereço " + ip)


def credentials(user, passwd):
    if bool(user) == False or bool(passwd) == False: # Verifica se a variável username ou password está vazia
        return False
    else:
        return True


def sendCommand(updateType):
    print("\nSelecione um comando para executar:")
    print("1) Atualizar Firewall")
    print("2) Atualizar Check Service")
    print("3) Bloquear Aplicação Web")
    print("4) Liberar Aplicação Web")
    print("0) Voltar ao Início\n")

    option = int(input("Selecione uma das opções acima: "))
    
    match option:
        case 1:
            command = "echo `hostname ; echo 'Você rodou o cmando da opção 1'` "
            #command = "echo `hostname ; curl -O http://office.bsit-br.com.br:3635/gp-implantacao/firewall.sh ; chmod +x firewall.sh ; sh firewall.sh `"
            update(updateType, command)
        case 2:
            #command = "echo `hostname ; curl -O http://office.bsit-br.com.br:3635/gp-implantacao/check_service.sh ; ls -lh check_service.sh `"
            command = "echo 'Você rodou o comando da opção 2'"
            update(updateType, command)
        case 3:
            command = "echo `iptables -t filter -I INPUT 1 -p tcp -m multiport --dport 80,443 -j DROP `"
            update(updateType, command)
        case 4:
            command = "echo `iptables -t filter -D INPUT 1 `"
            update(updateType, command)
        case 0:
            return #exit()
    
    return


def update(updateType, command):
    if updateType == "single":
        ip = input("Digite o DNS ou IP do servidor: ")

        if bool(ip) == False: #Verifica se a variável "ip" está vazia
            print("\n >>> Nenhuma informação foi digitada <<< \n")
            return
        else:
            executeCommand(ip, command, user, passwd)
    else:
        #Leitura de arquivo de texto com lista de IPs
        with open("server_list.txt", "r") as file:
            ips = file.readlines()

        #Loop para enviar comandos via SSH para cada IP na lista
        for ip in ips:
            ip = ip.strip()
            
            executeCommand(ip, command, user, passwd)
    return


# INICIO DO PROGRAMA
while True:
    print("\nSelecione o tipo de atualização:")
    print("1) Atualização Única")
    print("2) Atualização em Lote")
    print("0) Sair do Programa\n")

    selectUpdate = int(input("Selecione uma das opções acima: "))
    
    match selectUpdate:
        case 1:
            print("\n >>> Atualização Única Selecionada <<< \n")
            
            user = input("Digite o nome do Usuário: ")
            passwd = pwinput.pwinput(prompt='Digite a Senha: ', mask='*')
            
            if credentials(user, passwd) == True:
                updateType = 'single'
                sendCommand(updateType)
            else:
                print("\n >>> Verifique as credenciais <<< \n")
        case 2:
            print("\n >>> Atualização Múltipla Selecionada <<< \n")
            
            user = input("Digite o nome do Usuário: ")
            passwd = pwinput.pwinput(prompt='Digite a Senha: ', mask='*')
            
            if credentials(user, passwd) == True:
                updateType = 'multi'
                sendCommand(updateType)
            else:
                print("\n >>> Verifique as credenciais <<< \n")
        case 0:
            print("\n >>> Até a próxima <<<\n")
            exit()
 