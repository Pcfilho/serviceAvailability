from scipy.stats import binom
import pandas as pd
import matplotlib.pyplot as plt

# Parâmetros para o caso sem replicação (n = k = 1)
n_base = 1
k_base = 1
p_base = 0.5
availability_no_replication = binom.cdf(k_base-1, n_base, p_base)

# Valores específicos para n, k, e p para comparação
params = [
    {'n': 2, 'k': 1, 'p': 0.5},
    {'n': 2, 'k': 2, 'p': 0.5},
    {'n': 3, 'k': 1, 'p': 0.5},
    {'n': 3, 'k': 2, 'p': 0.5},
    {'n': 3, 'k': 3, 'p': 0.5}
]

# Lista para armazenar os resultados
results = []

# Calcular disponibilidade para cada conjunto de parâmetros
for param in params:
    n = param['n']
    k = param['k']
    p = param['p']
    
    # CDF da binomial é a probabilidade de k ou menos sucessos, então para k ou mais sucessos usamos 1 - cdf(k-1)
    availability = 1 - binom.cdf(k-1, n, p)
    results.append({
        'n': n,
        'k': k,
        'p': p,
        'availability': availability,
        'improvement': availability / availability_no_replication
    })

# Convertendo os resultados em um DataFrame do pandas para facilitar a manipulação e visualização
df = pd.DataFrame(results)

# Plotando os resultados
plt.figure(figsize=(10, 6))

# Plot para cada conjunto de parâmetros
for index, row in df.iterrows():
    plt.bar(f'n={row["n"]}, k={row["k"]}', row['availability'], label=f'p={row["p"]}')

plt.axhline(y=availability_no_replication, color='r', linestyle='--', label='No Replication (n=k=1)')

plt.xlabel('Configurations (n, k)')
plt.ylabel('Availability')
plt.title('Service Availability for Different Values of n, k, and p')
plt.legend()
plt.tight_layout()
plt.show()
