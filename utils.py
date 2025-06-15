import pdfplumber
import re

def extrair_dados(path_pdf):
    resultados = []
    with pdfplumber.open(path_pdf) as pdf:
        for page in pdf.pages:
            texto = page.extract_text()
            if texto:
                linhas = texto.split('\n')
                for linha in linhas:
                    match = re.match(r"(\d{9}) (.+?) (\d{2},\d) (\d{2},\d)(\d{2}/\d{2}/\d{4}) (.+?) (\d+º)(\d{2},\d+)", linha)
                    if match:
                        resultados.append({
                            "inscricao": match.group(1),
                            "nome": match.group(2),
                            "nota_objetiva": match.group(3),
                            "nota_redacao": match.group(4),
                            "nascimento": match.group(5),
                            "situacao": match.group(6),
                            "classificacao": match.group(7),
                            "nota_final": match.group(8)
                        })
    return resultados
