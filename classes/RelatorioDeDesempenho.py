import time
from memory_profiler import memory_usage

class RelatorioDeDesempenho:
    def __init__(self, arquivo_log="desempenho_teste.txt"):
        self.arquivo_log = arquivo_log

    def medir_desempenho(self, func):
        """
        Função decoradora que mede o tempo de execução e o uso de memória de funções de teste.
        Registra os resultados em um arquivo de log.
        """
        def wrapper(*args, **kwargs):
            start_time = time.time()  # Inicia o tempo
            mem_before = memory_usage()[0]  # Memória antes da execução
            result = func(*args, **kwargs)  # Executa a função
            mem_after = memory_usage()[0]  # Memória depois da execução
            end_time = time.time()  # Finaliza o tempo

            # Calcula tempo e uso de memória
            execution_time = end_time - start_time
            memory_used = mem_after - mem_before

            # Log no arquivo de desempenho
            with open(self.arquivo_log, 'a') as log_file:
                log_file.write(f"Função: {func.__name__}\n")
                log_file.write(f"Tempo de Execução: {execution_time:.6f} segundos\n")
                log_file.write(f"Uso de Memória: {memory_used:.2f} MiB\n\n")

            return result
        return wrapper
