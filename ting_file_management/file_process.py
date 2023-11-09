from ting_file_management.file_management import txt_importer
import sys


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
    sys.stdout.write(f"{fileDados}\n")


def remove(instance):
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")
    path_file = instance.dequeue()["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")


def file_metadata(instance, position):
    if len(instance) <= position:
        return sys.stderr.write("Posição inválida")
    sys.stdout.write(f"{instance.search(position)}\n")
