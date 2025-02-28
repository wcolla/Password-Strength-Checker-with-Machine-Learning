# Como Desenvolver um Classificador de Força de Senhas Mais Eficiente: Técnicas e Lições

# Introdução
A avaliação da força de senhas é um desafio crítico para a segurança digital. Algoritmos tradicionais costumam depender de regras simplistas ou técnicas genéricas de processamento de texto. Este artigo descreve a evolução de um classificador de força de senhas por meio de técnicas de machine learning adaptadas ao contexto de segurança, destacando melhorias e aprendizados técnicos.

# 1. Substituição do TF-IDF por Features Específicas para Senhas
Problema Identificado:
A abordagem inicial utilizava TF-IDF, técnica comum em análise de texto, para vetorizar senhas. No entanto, senhas não seguem padrões linguísticos, tornando essa técnica pouco eficaz para capturar características críticas.

Solução Implementada:
Substituiu-se o TF-IDF por features específicas, extraindo:

Comprimento da senha: Correlacionado diretamente com a segurança.

Quantidade de dígitos, letras maiúsculas, minúsculas e caracteres especiais: Diversidade como indicador de complexidade.

Entropia: Cálculo da aleatoriedade via fórmula de Shannon (ex: "aaaaa" tem baixa entropia, "A1b@C2d#" tem alta).

2. Balanceamento de Classes
Problema Detectado:
Conjuntos de dados de senhas frequentemente apresentam desbalanceamento (ex: excesso de senhas "Weak"), prejudicando a detecção de classes minoritárias.

Solução Adotada:
Utilizou-se o parâmetro class_weight='balanced' no Random Forest para atribuir pesos automáticos às classes, garantindo maior atenção a senhas fortes durante o treinamento.

3. Otimização Sistemática de Hiperparâmetros
Problema Inicial:
O modelo original utilizava configurações padrão do Random Forest, potencialmente subótimas.

Solução Aplicada:
Implementou-se uma busca sistemática de hiperparâmetros com GridSearchCV, testando combinações de:

Número de árvores (n_estimators).

Profundidade máxima das árvores (max_depth).

Divisão mínima de nós (min_samples_split).

Resultado: Identificação da configuração com maior F1-Score, balanceando precisão e recall.

4. Validação Robustecida
Melhorias Implementadas:

Aumento do conjunto de teste de 5% para 20% dos dados, assegurando avaliação mais confiável.

Adoção de métricas detalhadas (classification_report), permitindo análise por classe.

5. Entropia como Medida de Aleatoriedade
Inovação Incorporada:
Integrou-se o cálculo de entropia para identificar padrões repetitivos, com base na fórmula de Shannon.

Casos de Uso:

Senha "123456": Entropia baixa (repetição de padrões).

Senha "G7#kL2!q": Entropia alta (aleatoriedade).

6. Resultados e Aplicabilidade
Comparação de Desempenho:

Acurácia Original: ~85% (com TF-IDF e 5% de teste).

Acurácia Aprimorada: ~93% (com features específicas e balanceamento).

7. Recomendações para Futuros Desenvolvimentos
Integração de Listas de Senhas Comuns: Detecção de padrões conhecidos (ex: senhas de dicionário).

Modelos Híbridos: Combinação de regras heurísticas e machine learning para maior precisão.

Explicabilidade do Modelo: Uso de técnicas como SHAP ou LIME para interpretar decisões (ex: "Senha fraca devido à falta de caracteres especiais").

Conclusão
A substituição de abordagens genéricas por features específicas do domínio (como entropia) e a otimização sistemática de hiperparâmetros resultaram em um modelo mais preciso e adaptado ao contexto de segurança. O projeto demonstra a importância de alinhar técnicas de machine learning às particularidades do problema, com impacto direto na eficácia de sistemas de autenticação.
