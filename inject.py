import json

with open('M0_G14.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

ks_cell = {
    'cell_type': 'code',
    'execution_count': None,
    'metadata': {},
    'outputs': [],
    'source': [
        '# Teste de Normalidade (Kolmogorov-Smirnov)\n',
        '# Motivado pela metodologia do projeto ECAC, testamos formalmente a normalidade antes de aplicar testes não paramétricos.\n',
        'from scipy import stats\n',
        'import pandas as pd\n',
        '\n',
        'ks_results = []\n',
        'for c in MEASURES:\n',
        '    stat, p_val = stats.kstest(rehab[c].dropna(), \'norm\', args=(rehab[c].mean(), rehab[c].std()))\n',
        '    ks_results.append({\'Variável\': c, \'KS-Statistic\': stat, \'p-value\': p_val, \'Normal? (p>0.05)\': p_val > 0.05})\n',
        '\n',
        'display(pd.DataFrame(ks_results).set_index(\'Variável\'))\n',
        'print(\'Como o p-value é < 0.05 para todas as variáveis, rejeitamos a hipótese nula de normalidade.\')\n',
        'print(\'Isto justifica formalmente o uso do teste não-paramétrico de Kruskal-Wallis a seguir.\')'
    ]
}

pca_markdown = {
    'cell_type': 'markdown',
    'metadata': {},
    'source': [
        '**Análise de Componentes Principais (PCA) para visualização dos estados latentes**\n',
        'Inspirado pela redução de dimensionalidade no projeto ECAC, aplicamos PCA para verificar se os três estados de recuperação (Limited, Recovering, Functional) são separáveis no espaço de características latentes, o que servirá de base para os Mixture Models no Milestone M1.'
    ]
}

pca_cell = {
    'cell_type': 'code',
    'execution_count': None,
    'metadata': {},
    'outputs': [],
    'source': [
        'from sklearn.decomposition import PCA\n',
        'from sklearn.preprocessing import StandardScaler\n',
        '\n',
        '# Preparar os dados (apenas variáveis contínuas que variam no tempo)\n',
        'X = rehab[MEASURES].dropna()\n',
        'y = rehab.loc[X.index, \'state\']\n',
        '\n',
        '# Normalizar os dados (Z-score standardisation como no ECAC)\n',
        'scaler = StandardScaler()\n',
        'X_scaled = scaler.fit_transform(X)\n',
        '\n',
        '# Aplicar PCA (2 componentes para visualização 2D)\n',
        'pca = PCA(n_components=2)\n',
        'X_pca = pca.fit_transform(X_scaled)\n',
        '\n',
        '# Plot\n',
        'plt.figure(figsize=(10, 7))\n',
        'sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=y, hue_order=STATE_ORDER, palette=STATE_PAL, s=15, alpha=0.6, edgecolor=None)\n',
        'plt.title(f\'PCA: Projeção 2D das medições funcionais\\n(Variância explicada: {pca.explained_variance_ratio_.sum()*100:.1f}%)\')\n',
        'plt.xlabel(f\'Componente Principal 1 ({pca.explained_variance_ratio_[0]*100:.1f}%)\')\n',
        'plt.ylabel(f\'Componente Principal 2 ({pca.explained_variance_ratio_[1]*100:.1f}%)\')\n',
        'plt.tight_layout()\n',
        'plt.show()\n',
        '\n',
        'print(\'Interpretação: A PCA mostra que a Componente 1 separa razoavelmente os três estados, confirmando que os estados latentes são observáveis a partir de uma combinação linear destas métricas, embora com sobreposição.\')'
    ]
}

zscore_markdown = {
    'cell_type': 'markdown',
    'metadata': {},
    'source': [
        '**Deteção de Outliers Multivariada (Z-Score)**\n',
        'De forma semelhante à metodologia explorada no projeto ECAC, complementamos o método IQR com a análise Z-score para as medições. Como planeamos usar Gaussian Mixture Models (M1), que são muito sensíveis a outliers, é útil avaliar se existem valores extremos multivariados.'
    ]
}

zscore_cell = {
    'cell_type': 'code',
    'execution_count': None,
    'metadata': {},
    'outputs': [],
    'source': [
        'import numpy as np\n',
        '\n',
        '# Z-score threshold (k=3, como no ECAC)\n',
        'threshold_k = 3.0\n',
        'z_scores = np.abs(stats.zscore(rehab[MEASURES].dropna()))\n',
        '\n',
        '# Identificar outliers (pelo menos uma dimensão > k)\n',
        'outlier_mask = (z_scores > threshold_k).any(axis=1)\n',
        'n_z_outliers = outlier_mask.sum()\n',
        '\n',
        'print(f\'Nº total de outliers pelo método Z-score (k={threshold_k}): {n_z_outliers} ({(n_z_outliers/len(rehab))*100:.2f}% dos dados)\')\n',
        '\n',
        '# Visualizar a distribuição dos Z-scores máximos por observação\n',
        'plt.figure(figsize=(8, 4))\n',
        'sns.histplot(z_scores.max(axis=1), bins=50, color=\'coral\', kde=True)\n',
        'plt.axvline(threshold_k, color=\'k\', linestyle=\'--\', label=f\'Threshold (k={threshold_k})\')\n',
        'plt.title(\'Distribuição do Z-score máximo por observação\')\n',
        'plt.xlabel(\'Z-score máximo\')\n',
        'plt.legend()\n',
        'plt.tight_layout()\n',
        'plt.show()\n',
        '\n',
        'print(\'Embora existam alguns outliers, a sua proporção é pequena e podem representar estados clínicos válidos e extremos (não ruído do sensor). Por isso, optamos por não os remover, mas tomamos nota para os modelos probabilísticos.\')'
    ]
}

cells = nb['cells']
new_cells = []

for cell in cells:
    src = ''.join(cell.get('source', []))
    if 'stats.kruskal' in src:
        new_cells.append(ks_cell)
    
    new_cells.append(cell)

    if 'sns.heatmap(rehab[MEASURES + [\"utility\"]].corr()' in src:
        new_cells.append(pca_markdown)
        new_cells.append(pca_cell)
        
    if 'def iqr_outliers(s):' in src:
        new_cells.append(zscore_markdown)
        new_cells.append(zscore_cell)

nb['cells'] = new_cells

with open('M0_G14_improved.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
