from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)
    fileDados = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }
    for dados in instance._data:
        if dados["nome_do_arquivo"] == fileDados["nome_do_arquivo"]:
            return None
    instance.enqueue(fileDados)
    print(fileDados)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
