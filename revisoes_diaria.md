# Revisões
## 1ª Revisão
    - Uso do GitHub ou outro repositório sempre em projetos
        - na máquina a instalação do git (pacote de gestão do versionamento)
        - uso pode ser dinâmico:
            1) baixar na máquina pessoal e combinar com VS Code
            2) uso na Web direto no site do GitHub (logado)
            3) uso integrado com outras ferramentas Web (Replit, Google Colab)
    
    - Momento de usar 1ª vez VS Code (desktop)
        1) clonar projeto/repositório
        2) criar e ativar venv
        3) instalar os pacotes necessários do requirements.txt
    
    - Momento de usar demais vezes VS Code (desktop)
        1) puxar as atualizações do projeto
        2) ativar venv
        3) depois estabilizar a programação do código
        
## 2ª Revisão
    Na programação Python, em geral, há alguns recursos muito importantes:
        1) manipulação de strings
            split
            replace
            upper ou lower
        2) manipulação de listas
            len    - tamanho da lista
            append - adicionar
            remove - remover
            in     - verificar se algo está na lista
            sort   - ordenar
        3) manipulação de arquivos texto (plain text)
            .dat
            .csv
            .json
            .xml

            arquivo -> está em memória secundária (ssd, hd, flash)
                nome
                extensão
                tipo
                tamanho
                endereço

            variável -> prima do arquivo, só que em memória principal (RAM)
                nome
                tipo
                tamanho
                endereço

            Na manipulação de arquivos em programas, um ARQUIVO precisa de uma VARIÁVEL
            em memória principal o representando. Aqui, na disciplina, PROCURADOR

            Operações:
                - abrir ou open -> associar o procurador a um endereço de arquivo
                    - leitura - read - r
                    - escrita nova - write - w
                    - escrita adição - append - a
                - fechar a conexão do procurador com o arquivo
                - percorrer o procurador
                    - ler
                        - linha a linha
                    - escrever
                        - linha a linha
