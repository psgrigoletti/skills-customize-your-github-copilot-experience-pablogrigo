# 📘 Assignment: Organizando arquivos com Python

## 🎯 Objective

Nesta atividade de até 60 minutos, crie um script que organiza arquivos de uma pasta em subpastas por extensão. Você vai praticar `pathlib`, `shutil` e tratamento de erros usando apenas a biblioteca padrão do Python.

## 📝 Tasks

### 🛠️ Listar e classificar arquivos

#### Descrição

Comece com uma função que percorra os itens diretamente dentro de uma pasta de origem e classifique os arquivos pela extensão. Não percorra subpastas.

#### Requisitos

O programa concluído deve:

- Usar `pathlib.Path.iterdir()` para listar os itens da pasta
- Contar apenas arquivos, ignorando subpastas
- Normalizar extensões para letras minúsculas, para que `.TXT` e `.txt` pertençam à mesma categoria
- Classificar arquivos sem extensão na categoria `sem-extensao`
- Exibir a quantidade de arquivos encontrada em cada categoria

### 🛠️ Copiar arquivos para pastas por extensão

#### Descrição

Peça ao usuário o caminho da pasta de origem e o caminho da pasta de destino. Para cada arquivo da pasta de origem, crie na pasta de destino uma subpasta com o nome da categoria e copie o arquivo para ela.

#### Requisitos

O programa concluído deve:

- Criar a pasta de destino e as subpastas necessárias quando ainda não existirem
- Usar `shutil.copy2()` para preservar os metadados básicos dos arquivos
- Manter os arquivos originais intactos
- Organizar arquivos sem extensão dentro da pasta `sem-extensao`

### 🛠️ Tratar erros e apresentar um resumo

#### Descrição

Prepare o script para entradas e operações que podem falhar. Ao final, mostre um resumo do que aconteceu durante a organização.

#### Requisitos

O programa concluído deve:

- Informar claramente se a pasta de origem não existir ou não for uma pasta
- Não sobrescrever um arquivo de mesmo nome que já exista no destino; registrar esse arquivo como ignorado
- Tratar erros de sistema de arquivos durante a cópia, informar o arquivo afetado e continuar com os próximos arquivos
- Exibir as quantidades de arquivos copiados, ignorados e com falha
- Testar o script com arquivos `.txt`, `.CSV` e sem extensão, além de uma subpasta e de um arquivo já existente no destino
