
# ♦ ♥  Jogo 21  ♠ ♣

## Membros do Grupo

**Rodrigo Braz**

**Renan Maia**

**Diego Tomaz**

**Lorrayne Somerlatte**

## Sistema Desenvolvido

Nesta versão simplificada do jogo de cartas Blackjack, há um jogador e a casa. O jogador recebe uma mão inicial com duas cartas e o objetivo é alcançar um total de pontos o mais próximo possível de 21, sem ultrapassá-lo. Se o jogador ultrapassar 21 pontos, ele perde automaticamente.

Após receber as duas cartas iniciais, o jogador tem a opção de solicitar mais cartas (chamadas de "hit") para tentar melhorar sua mão. O jogador pode pedir quantas cartas desejar, porém, deve ter cuidado para não ultrapassar 21 pontos.

Quando o jogador decide parar de pedir cartas (chamado de "stand"), é a vez da casa jogar. A casa deve continuar tirando cartas até atingir um total de pontos igual ou superior a 17. Se a casa ultrapassar 21 pontos, o jogador vence. Caso contrário, a mão do jogador e a mão da casa são comparadas para determinar o vencedor.

Se o jogador tiver uma mão com mais pontos do que a casa, sem ultrapassar 21 pontos, o jogador vence. Se a casa tiver uma mão com mais pontos ou se ambos tiverem o mesmo número de pontos, a casa vence.

Essa versão simplificada do Blackjack permite ao jogador experimentar a emoção do jogo, tentando obter uma mão o mais próximo possível de 21 pontos, enquanto enfrenta o desafio de decidir quando parar de pedir cartas e arriscar o resultado final.

## Tecnologias Utilizadas

- Como linguagem de programação principal utilizamos Python.

- Para testes, utilizamos o Pytest.

- Mais informações sobre os requisitos e o diagrama de classes podem ser encontrados na pasta "docs".
- Para avaliação da qualidade do código, utilizamos o [Lizard](https://github.com/terryyin/lizard).

### Lizard
O relatório do Lizard é composto, fundamentalmente, por:

>`NLOC`: Número de linhas de código. Essa métrica se refere à quantidade de linhas em cada função. Em geral, funções menores são mais fáceis de entender e manter. </b>
>`CCN`: Complexidade ciclomática. Essa métrica indica a quantidade de caminhos independentes através do código-fonte de uma função. Valores altos podem indicar funções complexas que podem ser difíceis de entender e testar.</b>
>`token`: Número de tokens no código. Um token pode ser um identificador, uma palavra-chave, um separador, um literal ou um operador.</b>
>`PARAM`: Número de parâmetros da função. Funções com muitos parâmetros podem ser mais difíceis de entender e usar corretamente.</b>
>`length`: Comprimento da função em linhas de código.</b>
>`location`: Localização do arquivo e linha onde a função é definida.</b>

O relatório sobre o Jogo 21 mostrou que, em geral, a complexidade ciclomática e o número de linhas de código são baixos, o que remete a um código relativamente simples e direto. Ademais, no resumo é indicado que nenhum limite foi excedido (*complexidade ciclomática > 15 ou comprimento > 1000 ou NLOC > 1000000 ou contagem de parâmetros > 100*), o que é um bom indicativo da qualidade do código.

Além disso, o relatório apontou que as três funções mais complexas do código são: `main`, `perguntar_jogador_proxima_jogada` e `definir_vencedor` e, conforme solicitado, medidas de melhoria de código foram tomadas, conforme *commits* `41b58d5, 5903b50, 4da4f01, 0132174 e 968ce9e`.

## Execução
