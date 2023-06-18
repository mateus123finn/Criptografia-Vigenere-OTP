class Vigenere:

    # Função que de acordo com o padrão passado por Parâmetro, realiza a Criptografia por Vigenére
    def criptografar(self,path,padrao:str):

        arquivo_raw = open(path, "rb")
        arquivo_codificado = open("./VGN/"+path+".VGN","wb")

        texto = arquivo_raw.read(1)
        padrao_pos = 0
        vetor_codificar = padrao.encode("cp850")

        while(texto != b''):
            novo_byte = (int.from_bytes(texto,'big') + vetor_codificar[padrao_pos]) % 256
            arquivo_codificado.write(novo_byte.to_bytes(1,'big'))
            padrao_pos = (padrao_pos+1)%len(padrao)
            texto = arquivo_raw.read(1)

        arquivo_raw.close()
        arquivo_codificado.close()

    # Função que de acordo com o padrão passado por Parâmetro, Decripta o arquivo por Vigenére
    def decriptografar(self,path,padrao:str):
        arquivo_codificado = open(path, "rb")
        raw_path = path[:-4]
        arquivo_raw = open(raw_path,"wb")

        texto = arquivo_codificado.read(1)
        padrao_pos = 0
        vetor_decodificar = padrao.encode("cp850")

        while(texto != b''):
            novo_byte = (int.from_bytes(texto,'big') - vetor_decodificar[padrao_pos])
            if(novo_byte < 0):
                novo_byte += 256
            arquivo_raw.write(novo_byte.to_bytes(1,'big'))
            padrao_pos = (padrao_pos+1)%len(padrao)
            texto = arquivo_codificado.read(1)

        arquivo_raw.close()
        arquivo_codificado.close()



