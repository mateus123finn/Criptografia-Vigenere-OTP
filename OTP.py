import uuid
class OneTime:

    # Inicializa e Salva uma chave de 128 bits num arquivo de chave .key
    def __init__(self):
        self.key = uuid.uuid4().int
        with open("./OTP/OTP.key","wb") as f:
            f.write(self.key.to_bytes(16,'big'))

        print("Chave Salva em ./OTP/OTP.key")

    # Função que de acordo com a chave inicializada com a classe, realiza a Criptografia por One Time Pad
    def criptografar(self, path):
        arquivo_raw = open(path,"rb")
        arquivo_codificado = open("./OTP/"+path+".OTP","wb")

        texto = arquivo_raw.read(16)

        while(texto != b''):

            codificado = int.from_bytes(texto,'big') ^ self.key
            arquivo_codificado.write(codificado.to_bytes(16,'big'))
            texto = arquivo_raw.read(16)

        arquivo_raw.close()
        arquivo_codificado.close()

    # Função que de acordo com o camino do arquivo contendo a chave de Decriptação, realiza a Decriptografia do Texto em One Time Pad
    def decriptografar(self,path ,padrao_path):
        arquivo_codificado = open(path,"rb")
        raw_path = path[:-4]
        arquivo_raw = open(raw_path,"wb")

        with open(padrao_path, "rb") as f:
            padrao = int.from_bytes(f.read(16),'big')

        texto = arquivo_codificado.read(16)

        while(texto != b''):

            decodificado = int.from_bytes(texto,'big') ^ padrao
            arquivo_raw.write(decodificado.to_bytes(16,'big'))
            texto = arquivo_codificado.read(16)

        arquivo_codificado.close()
        arquivo_raw.close()





