## ♦ ♥  Jogo 21  ♠ ♣  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/maiarenan/TP-Eng-Software-2/actions/workflows/main.yml"><img alt="Python application test" src="https://github.com/maiarenan/TP-Eng-Software-2/actions/workflows/main.yml/badge.svg"></a> <a href="https://github.com/maiarenan/TP-Eng-Software-2/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/maiarenan/TP-Eng-Software-2"></a>
### Membros do Grupo

Rodrigo Braz, Renan Maia, Diego Tomaz e Lorrayne Somerlatte

### Sistema Desenvolvido

Nesta versão simplificada do jogo de cartas Blackjack, há um jogador e a casa. O jogador recebe uma mão inicial com duas cartas e o objetivo é alcançar um total de pontos o mais próximo possível de 21, sem ultrapassá-lo. Se o jogador ultrapassar 21 pontos, ele perde automaticamente.

Após receber as duas cartas iniciais, o jogador tem a opção de solicitar mais cartas (chamadas de "hit") para tentar melhorar sua mão. O jogador pode pedir quantas cartas desejar, porém, deve ter cuidado para não ultrapassar 21 pontos.

Quando o jogador decide parar de pedir cartas (chamado de "stand"), é a vez da casa jogar. A casa deve continuar tirando cartas até atingir um total de pontos igual ou superior a 17. Se a casa ultrapassar 21 pontos, o jogador vence. Caso contrário, a mão do jogador e a mão da casa são comparadas para determinar o vencedor.

Se o jogador tiver uma mão com mais pontos do que a casa, sem ultrapassar 21 pontos, o jogador vence. Se a casa tiver uma mão com mais pontos ou se ambos tiverem o mesmo número de pontos, a casa vence.

Essa versão simplificada do Blackjack permite ao jogador experimentar a emoção do jogo, tentando obter uma mão o mais próximo possível de 21 pontos, enquanto enfrenta o desafio de decidir quando parar de pedir cartas e arriscar o resultado final.

Ademais, anexamos um [**`documento`**](https://github.com/maiarenan/TP-Eng-Software-2/blob/main/docs/21%20python.pdf) que contém os requisitos explicados de forma mais detalhada e, também, diagramas UML do projeto.

### Tecnologias Utilizadas

- Como linguagem de programação principal utilizamos Python.

- Para testes, utilizamos o Pytest.

- Mais informações sobre os requisitos e o diagrama de classes podem ser encontrados na pasta "docs".
- Para avaliação da qualidade do código, utilizamos o [Lizard](https://github.com/terryyin/lizard).

### Lizard
O relatório do Lizard é composto, fundamentalmente, por:

>`NLOC`: Número de linhas de código. Essa métrica se refere à quantidade de linhas em cada função. Em geral, funções menores são mais fáceis de entender e manter. </br>
>`CCN`: Complexidade ciclomática. Essa métrica indica a quantidade de caminhos independentes através do código-fonte de uma função. Valores altos podem indicar funções complexas que podem ser difíceis de entender e testar.</br>
>`token`: Número de tokens no código. Um token pode ser um identificador, uma palavra-chave, um separador, um literal ou um operador.</br>
>`PARAM`: Número de parâmetros da função. Funções com muitos parâmetros podem ser mais difíceis de entender e usar corretamente.</br>
>`length`: Comprimento da função em linhas de código.</br>
>`location`: Localização do arquivo e linha onde a função é definida.</br>

O [**`relatório`**](https://github.com/maiarenan/TP-Eng-Software-2/blob/main/relatorio_lizard.txt)  sobre o Jogo 21 mostrou que, em geral, a complexidade ciclomática e o número de linhas de código são baixos, o que remete a um código relativamente simples e direto. Ademais, no resumo é indicado que nenhum limite foi excedido (*complexidade ciclomática > 15 ou comprimento > 1000 ou NLOC > 1000000 ou contagem de parâmetros > 100*), o que é um bom indicativo da qualidade do código.

Além disso, o relatório apontou que as três funções mais complexas do código são: `main`, `perguntar_jogador_proxima_jogada` e `definir_vencedor` e, conforme descrição do TP, medidas de melhoria de código foram tomadas, de acordo com os *commits* [**41b58d5**](https://github.com/maiarenan/TP-Eng-Software-2/commit/41b58d55debceb7b0f86f5cfe0d22b07a13b8174), [**5903b50**](https://github.com/maiarenan/TP-Eng-Software-2/commit/5903b507b23d91a393d3e73abd40e46f07a11595), [**4da4f01**](https://github.com/maiarenan/TP-Eng-Software-2/commit/4da4f01b0766615b8499adec17e267342e9974d9), [**0132174**](https://github.com/maiarenan/TP-Eng-Software-2/commit/0132174a8c9fad952b676afa4298e02aba430714) e [**968ce9e**](https://github.com/maiarenan/TP-Eng-Software-2/commit/968ce9e68b3055b9a971c98c76529f57bd92810e).

### Execução
No console:</br>
Para executar o jogo basta efetuar o comando "python .\main.py" e seguir as instruções em tela para jogar. </br>
Para executar os testes, digite o comando "pytest" e o pytest executará todos os testes disponíveis na aplicação.
