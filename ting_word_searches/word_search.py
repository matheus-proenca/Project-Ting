def exists_word(word, instance):
    data = []
    ocorrencias = []
    for fileData in instance._data:
        for i in range(len(fileData["linhas_do_arquivo"])):
            length = fileData["linhas_do_arquivo"][i].lower()
            if length.find(word) > -1:
                ocorrencias.append({"linha": i + 1})
        if len(ocorrencias) != 0:
            data.append(
                {
                    "palavra": word,
                    "arquivo": fileData["nome_do_arquivo"],
                    "ocorrencias": ocorrencias,
                }
            )
    return data


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
