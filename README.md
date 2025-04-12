# Unifil_Visualizacao_Dados
#
# 1 Introdução
  A presente atividade foi realizada com o objetivo de se estudar um conjunto de dados selecionado da base de dados do UCI Machine Learning Repository e aplicar os conceitos vistos na disciplina Visualização de Dados.
  Para o presente trabalho foi selecionada uma base de dados de estudantes  de duas escolas de nível médio de Portugal contendo 649 instâncias com 30 atributos ('school', 'sex', 'age', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu',
       'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime', 'studytime','failures', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery','higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences' e suas respectivas notas “'G1', 'G2', 'G3'” como variável target. 
A base de dados pode ser empregada para testar modelos de classificadores, assim como treinar modelos de regressão para estimativa de notas de outros alunos partir desses atributos.

# 2 - Metodologia

Para o tratamento dos dados da base obtida será empregado o Processo de Descobrimento de Conhecimento, conhecido como KDD (Knowledge Discovery in Database), que abrange as etapas de obtenção dos dados, pré-processamento, a mineração e o pós processamento, com a visualização dos dados para então obtermos alguma informação desse processo de descobrimento sobre a base de dados empregada.
Na primeira fase serão realizados o carregamento dos pacotes do Python (Plotly — gráficos dinâmicos, Seaborn e Matplotlib — visualização de correlações, Pandas & Scikit-learn — manipulação e padronização dos dados)  e, em seguida, a obtenção da base de dados de estudantes do Repositório da UCI. 
Na sequência, será realizada a análise exploratória que objetiva realizar o tratamento adequado para dados ausentes, repetidos, assim como realizar a limpeza dos dados, conversão de dados categóricos em numéricos e decodificação de dados categóricos em one hot enconded.
Por fim, ainda nessa fase, a transformação dos dados por normalização para melhor verificar correlações entre os atributos. 

(editar)
Na segunda fase será realizada a mineração de dados empregando modelos de agrupamento a fim de descobrir eventuais padrões e categorias importantes no conjunto de dados ou então empregar modelos que possibilitem a previsão de rótulos categóricos.
No presente estudo serão empregados dois tipos de modelos: 
1 - Modelos de clusterização (K-means, DBSCAN, Spectral) e 
2 - Modelos de classificação (Regressão Linear a Random Forest)
(editar)

# 3- Análise de resultados
Nessa parte foi realizada a análise exploratória do conjunto de dados e, também, as transformações necessárias para adequá-lo como conjunto de entrada para a matriz de correlação. Um das transformações foi a de criar novos atributos 
a partir de um atributo do tipo categórico (objetc) tais como  o atributo "school" se transformando em school_MS e school_GP, do tipo numérico binário sendo atribuido os valores 0 e 1 para cada atributo. Essa transformação é a denominada one hot encoding.
A base de dados original possui 649 registros e 30 atributos de tipos diversos cuja análise inicial não revelou dados nulos ou ausentes, tampouco duplicados, tiveram todos os seus atributos  convertidos para numéricos passando a ter agora 51 atributos.

Base de dados original                         

 0   school  -    649 non-null    object                                           

 1   sex     -    649 non-null    object       
 
 2   age     -    649 non-null    int64 
 
 3   address -    649 non-null    object       
 
 4   famsize -    649 non-null    object
 
 5   Pstatus -    649 non-null    object
 
 6   Medu    -    649 non-null    int64 
 
 7   Fedu    -    649 non-null    int64 
 
 8   Mjob    -    649 non-null    object
 
 9   Fjob    -    649 non-null    object
 
 10  reason   -   649 non-null    object
 
 11  guardian -   649 non-null    object
 
 12  traveltime-  649 non-null    int64 
 
 13  studytime -  649 non-null    int64 
 
 14  failures  -  649 non-null    int64 
 
 15  schoolsup -  649 non-null    object
 
 16  famsup    -  649 non-null    object
 
 17  paid      -  649 non-null    object
 
 18  activities - 649 non-null    object
 
 19  nursery   -  649 non-null    object
 
 20  higher    -  649 non-null    object
 
 21  internet  -  649 non-null    object
 
 22  romantic  -  649 non-null    object
 
 23  famrel    -  649 non-null    int64 
 
 24  freetime  -  649 non-null    int64 
 
 25  goout    -   649 non-null    int64 
 
 26  Dalc     -   649 non-null    int64 
 
 27  Walc    -    649 non-null    int64 
 
 28  health   -   649 non-null    int64 
 
 29  absences -   649 non-null    int64 
 
 30  G1      -    649 non-null    int64 
 
 31  G2      -    649 non-null    int64 
 
 32  G3      -    649 non-null    int64 
 
dtypes: int64(16), object(17)

Na sequência foram avaliadas a correlação dos dados cujo resultado pode ser verificado no gráfico, a seguir:

![image](https://github.com/user-attachments/assets/8f967c86-6fa2-45fb-bf02-843e36efadff)

A partir da matriz de correlação e das estatísticas descritivas, foram identificados os seguintes padrões:


    Correlações Positivas com o Desempenho (G1, G2, G3):

    higher_yes (≈ 0.34): Alunos que desejam cursar ensino superior apresentam melhores notas.

    school_GP (≈ 0.28): Estudantes da escola Gabriel Pereira tendem a obter desempenho superior.

    studytime (≈ 0.25): Mais horas de estudo semanal → melhores notas.

    Medu e Fedu (≈ 0.25 e 0.22): Maior escolaridade dos pais → melhor desempenho.

    reason_reputation: Motivo de escolha da escola por reputação também está associado a notas maiores.

 Correlações Negativas com o Desempenho:

    failures (≈ -0.39): Quanto mais reprovações anteriores, pior o desempenho atual.

    higher_no (≈ -0.34): Alunos sem intenção de cursar o ensino superior têm desempenho inferior.

    school_MS (≈ -0.28): Estudantes da escola Mousinho da Silveira apresentam menores notas.


Apesar dos valores de correlações entre as variáveis não apresentar valores maiores que 0,8 sinalizando uma correlação forte entre os atributos, os maiores valores encontrados foram na faixa de 0,25 a 0,40, sinalizando os atributos que mais influenciam 
diretamente  as notas G1, G2 e  G3. Da mesma forma os atributos com correlções entre -0,25 e -0,40 sinalizam correlações contrárias às notas.  

# 4 - Visualizações e interpretações

Foram realizadas 3 visualizações  por meio do pacote streamlit 
*gráfico de histogramas,
*gráfico de barras 
*gráfico de dispersão 

No gráfico de histograma procurou-se explorar visualizações de desempenho dos estudando por sexo e por escola para cada nota (G1, G2 ou G3) obtidas ao longo do periodo letivo.
Esse gráfico no mostra que estudantes da escola Gabriel Pereira possuem notas mais altas que os estudantes da escola Mousinho da Silveira, para ambos os sexos.

Já no gráfico de barra agrupadas procurou-se observar o comportamento do conjunto de notas ao longo do ano em função de outro atributo qualquer escolhido.
Nessa visualização podemos ver que as notas do sexo feminino são maiores do que as notas dos alunos do sexo masculino. Assim como alunos que mroam na área urbana possuem notas ligeiramente mais altas que alunos que residem na área rural.
Pode-se observar também que o desempenho dos estudantes é maior se a mãe trabalha na área da saúde ou como professora. Já esse desempenho é destacado apenas quando o pai possui emprego como professor.
Em todas as visualizações é possível perceber que as notas apresentam uma evolução crescente ao longo do ano sendo a nota G1 a mais baixa e a G3 a nota mais alta para qualqueroutro atributo anallisado em conjunto
Também é possível visualizar que a intenção de cursar ensino superior (`higher`) está fortemente relacionada ao bom desempenho.

Por último, o grafico de dispersão é possível escolher 4 atributos e ver como se correlacionam e tirarmos algumas conclusões
Quanto maior o tempo semanal de estudo (x) maior tende a ser a nota final-G3 (y)
Outra cosntatação é que estudantes que possuem mais reprovações anteriores-failures(x) tendem a ter notas mais baixas-G3 (y)
Outras associações podem ser obtidas e conclusões tiradas dessa combinação



# Referências Bibliográficas
Apostila da disciplina de Vis de Dados, UNIFIL, 2025, acesso em 31/03/2025;
Base de dados de Performance de estudantes, UCI Machine Learning Repository, Disponível em: https://archive.ics.uci.edu/dataset/320/student+performance, acesso em 31/03/2025.
Biblioteca Plotly Express, Disponível em: https://plotly.com/python/plotly-express/, acesso em 31/03/2025.
Biblioteca Streamlit,. Disponível em https://streamlit.io/ , acesso em 31/03/2025
HAN, Jiawei; KAMBER, Micheline; PEI, Jian. Data Mining: Concepts and Techniques. 3. ed. San Francisco: Morgan Kaufmann, 2011. Disponível em: http://hanj.cs.illinois.edu/bk3/ . Acesso em: 31/03/2025.

