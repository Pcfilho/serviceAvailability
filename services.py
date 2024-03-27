from scipy.special import binom

# Função para calcular a disponibilidade do serviço
def availability(n, k, p):
    if k == 1:
        return 1 - (1 - p) ** n
    elif k == n:
        return p ** n
    else:
        return sum(binom(n, x) * p ** x * (1 - p) ** (n - x) for x in range(k, n + 1))

# Parâmetros para a simulação
n_values = [1, 2, 3, 4, 5]
k_values = [1, 2, 3, 4, 5]
p_values = [0.5, 0.7, 0.9]

# Criar um DataFrame para armazenar os resultados
results = pd.DataFrame(columns=["n", "k", "p", "availability"])

# Calcular a disponibilidade para diferentes valores de n, k e p
for n in n_values:
    for k in range(1, n+1):
        for p in p_values:
            results = results.append({"n": n, "k": k, "p": p, "availability": availability(n, k, p)}, ignore_index=True)

# Mostrar os resultados em uma tabela
print(results)

# Visualizar os resultados em gráficos com cores diferentes para cada linha de k
for p in p_values:
    plt.figure(figsize=(10, 6))
    colors = ['blue', 'green', 'red', 'purple', 'orange']
    for i, k in enumerate(k_values):
        # Filtrar os resultados para cada valor de p e k
        filtered_results = results[(results['p'] == p) & (results['k'] == k)]
        if not filtered_results.empty:
            plt.plot(filtered_results['n'], filtered_results['availability'], label=f"k={k}", color=colors[i % len(colors)])
    plt.title(f"Disponibilidade do Serviço com p={p}")
    plt.xlabel("Número de Servidores (n)")
    plt.ylabel("Disponibilidade")
    plt.legend()
    plt.grid(True)
    plt.show()
