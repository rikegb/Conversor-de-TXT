import json
import csv
import xml.etree.ElementTree as ET

def converter_formatos(caminho_arquivo_txt):
    # Abrir o arquivo e ler os dados
    with open(caminho_arquivo_txt, 'r') as file:
        linhas = file.readlines()

    # Extrair os dados do arquivo
    livros = []
    for linha in linhas:
        partes = linha.strip().split(", ")
        livro = {
            "Título": partes[0],
            "Autor": partes[1],
            "Ano de Publicação": partes[2],
            "Gênero": partes[3]
        }
        livros.append(livro)

    # Converter para JSON
    with open('livros.json', 'w') as json_file:
        json.dump(livros, json_file, indent=4)

    # Converter para CSV
    with open('livros.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=livros[0].keys())
        writer.writeheader()
        writer.writerows(livros)

    # Converter para XML
    root = ET.Element("livros")
    for livro in livros:
        livro_element = ET.SubElement(root, "livro")
        for key, value in livro.items():
            ET.SubElement(livro_element, key).text = str(value)

    tree = ET.ElementTree(root)
    tree.write("livros.xml", encoding='utf-8', xml_declaration=True)

# Exemplo de uso
caminho_arquivo_txt = "livros.txt"
converter_formatos(caminho_arquivo_txt)
