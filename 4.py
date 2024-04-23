"""
4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode
ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é
descobrir qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas,
qual interruptor controla cada lâmpada?

Resposta:

Ligo o primeiro interruptor, deixo ele ligado por um tempo, desligo ele.
Ligo o segundo interruptor, deixo ele.

Vou até a sala da primeira lâmpada, temos 3 casos:

Se a lâmpada estiver apagada e quente, interruptor 1.
Se a lâmpada estiver acessa, interruptor 2.
Se a lâmpada estiver apagada e fria, interruptor 3.

Sabendo qual o interruptor da lâmpada 1, deixa o interruptor dela desligado.

Ligo 1 dos interruptores que eu não sei de qual lâmpada é.

Vou até a sala da segunda lâmpada:

Se a lâmpada estiver acessa, é o interruptor que deixei ligado.
Se a lâmpada estiver apagada, é o interruptor que deixei desligado.

E consequentemente o interruptor da lâmpada 3 é o oposto da lâmpada 2.
"""