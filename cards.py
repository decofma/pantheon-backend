CARDS = {
    "Mitologia Grega": {
        "Deuses": [
            {"nome": "Zeus, Senhor dos Raios", "poder": 8, "efeito": "Tempestade Divina - Uma vez por turno, causa 3 pontos de dano extra a todas as criaturas inimigas.", "atributo": "Ataque"},
            {"nome": "Hera, Guardiã do Casamento", "poder": 6, "efeito": "Proteção Nupcial - Ao ser invocada, concede +2 de defesa a todos os deuses aliados neste turno.", "atributo": "Sabedoria"},
            {"nome": "Poseidon, Senhor dos Mares", "poder": 7, "efeito": "Maré Revolta - Redireciona 2 pontos de dano de um aliado para uma criatura inimiga.", "atributo": "Água"},
            {"nome": "Ares, Deus da Guerra", "poder": 7, "efeito": "Fúria de Batalha - Permite realizar um ataque adicional na fase de combate.", "atributo": "Ataque"},
            {"nome": "Atena, Deusa da Sabedoria", "poder": 6, "efeito": "Estratégia Divina - Reorganiza a mão ou o baralho para o próximo turno.", "atributo": "Sabedoria"},
            {"nome": "Apolo, Deus da Luz e Música", "poder": 6, "efeito": "Melodia Curativa - Restaura 3 pontos de vida a um aliado.", "atributo": "Cura"},
            {"nome": "Artemis, Deusa da Caça", "poder": 6, "efeito": "Chuva de Flechas - Ataca até 2 criaturas inimigas, causando 2 de dano a cada.", "atributo": "Ataque"}
        ],
        "Artefatos": [
            {"nome": "Cetro de Zeus", "custo_fe": 3, "efeito": "Concede +2 de poder a um deus aliado neste turno.", "atributo": "Magia"},
            {"nome": "Tridente de Poseidon", "custo_fe": 3, "efeito": "Permite redirecionar 2 pontos de dano de um aliado para uma criatura inimiga.", "atributo": "Água"},
            {"nome": "Escudo de Atena", "custo_fe": 2, "efeito": "Concede +3 de defesa a um deus ou criatura aliado durante um ataque.", "atributo": "Defesa"}
        ],
        "Eventos": [
            {"nome": "Fúria dos Céus", "custo_fe": 4, "efeito": "Causa 2 pontos de dano a todas as criaturas e deuses inimigos.", "atributo": "Natureza"},
            {"nome": "Ira dos Deuses", "custo_fe": 5, "efeito": "Todos os deuses aliados ganham +2 de poder e os inimigos sofrem 2 de dano direto.", "atributo": "Ataque"},
            {"nome": "Benção de Deméter", "custo_fe": 3, "efeito": "Restaura 4 pontos de vida a todos os deuses aliados.", "atributo": "Cura"},
            {"nome": "Eclipse Divino", "custo_fe": 3, "efeito": "Neutraliza as habilidades especiais dos deuses inimigos por um turno.", "atributo": "Magia"},
            {"nome": "Festa Olímpica", "custo_fe": 2, "efeito": "Todos os deuses aliados recebem +1 de poder e +1 de defesa neste turno.", "atributo": "Defesa"}
        ],
        "Criaturas": [
            {"nome": "Quimera", "poder": 5, "efeito": "Fogo do Abismo - Ao atacar, causa 2 pontos de dano extra.", "atributo": "Fogo"},
            {"nome": "Hidra de Lerna", "poder": 6, "efeito": "Ao ser atacada, pode regenerar 1 ponto de poder para cada “cabeça perdida” (até 3 vezes por turno).", "atributo": "Cura"},
            {"nome": "Cérbero", "poder": 7, "efeito": "Guardiã do Submundo - Impede ataques diretos aos deuses aliados enquanto estiver em campo.", "atributo": "Defesa"},
            {"nome": "Fênix Renascida", "poder": 5, "efeito": "Ao ser destruída, retorna com metade do poder no próximo turno.", "atributo": "Cura"},
            {"nome": "Minotauro", "poder": 6, "efeito": "Força Brutal - Ignora 2 pontos de defesa do inimigo durante o ataque.", "atributo": "Força"}
        ]
    },
    "Mitologia Romana": {
        "Deuses": [
            {"nome": "Júpiter, Rei dos Céus", "poder": 8, "efeito": "Tempestade Imperial - Causa 3 de dano extra a todas as criaturas inimigas.", "atributo": "Ataque"},
            {"nome": "Juno, Protetora do Estado", "poder": 6, "efeito": "Véu da Proteção - Concede +2 de defesa para todos os deuses aliados por um turno.", "atributo": "Defesa"},
            {"nome": "Neptune, Senhor dos Mares", "poder": 7, "efeito": "Maré da Guerra - Redireciona 2 pontos de dano de um aliado para uma criatura inimiga.", "atributo": "Água"},
            {"nome": "Mars, Deus da Guerra", "poder": 7, "efeito": "Caminho da Conquista - Permite um ataque extra na fase de combate.", "atributo": "Ataque"},
            {"nome": "Minerva, Deusa da Sabedoria", "poder": 6, "efeito": "Estratégia Imperial - Reorganiza a mão para o próximo turno.", "atributo": "Sabedoria"},
            {"nome": "Apollo, Deus da Luz", "poder": 6, "efeito": "Harmonia Celestial - Cura 3 pontos de vida de um aliado.", "atributo": "Cura"},
            {"nome": "Diana, Deusa da Caça", "poder": 6, "efeito": "Chuva de Flechas - Ataca até 2 criaturas inimigas, causando 2 de dano cada.", "atributo": "Ataque"}
        ],
        "Artefatos": [
            {"nome": "Relâmpago de Júpiter", "custo_fe": 3, "efeito": "Concede +2 de poder a um deus aliado por um turno.", "atributo": "Magia"},
            {"nome": "Tridente de Neptune", "custo_fe": 3, "efeito": "Redireciona 2 pontos de dano de uma criatura inimiga para outra.", "atributo": "Água"},
            {"nome": "Escudo de Minerva", "custo_fe": 2, "efeito": "Aumenta a defesa de um aliado em 3 pontos durante um ataque.", "atributo": "Defesa"}
        ],
        "Eventos": [
            {"nome": "Ira dos Deuses Romanos", "custo_fe": 4, "efeito": "Deuses aliados ganham +2 de poder e inimigos sofrem 2 de dano direto.", "atributo": "Ataque"},
            {"nome": "Banquete de Roma", "custo_fe": 3, "efeito": "Cura 4 pontos de vida para todos os aliados.", "atributo": "Cura"},
            {"nome": "Festival de Júpiter", "custo_fe": 3, "efeito": "Aumenta o poder de todos os deuses aliados em 1 ponto neste turno.", "atributo": "Defesa"},
            {"nome": "Queda de Roma", "custo_fe": 4, "efeito": "Reduz o poder de todos os deuses inimigos em 2 pontos por um turno.", "atributo": "Ataque"},
            {"nome": "Portento do Destino", "custo_fe": 3, "efeito": "Permite trocar uma carta da sua mão com a carta do topo do seu deck.", "atributo": "Sabedoria"}
        ],
        "Criaturas": [
            {"nome": "Lupa Capitolina", "poder": 5, "efeito": "Instinto de Sobrevivência - Ao entrar em jogo, reduz 2 pontos de dano em um aliado.", "atributo": "Defesa"},
            {"nome": "Gladiador Invencível", "poder": 6, "efeito": "Espírito de Combate - Ganha +2 de poder se atacar imediatamente após a invocação.", "atributo": "Ataque"},
            {"nome": "Centurião Imortal", "poder": 6, "efeito": "Disciplina Romana - Reduz 2 pontos de dano recebido a cada turno.", "atributo": "Defesa"},
            {"nome": "Falcão de Júpiter", "poder": 4, "efeito": "Vôo Aéreo - Pode atacar sem ser bloqueado por criaturas terrestres.", "atributo": "Agilidade"},
            {"nome": "Lânio Feroz", "poder": 7, "efeito": "Investida Selvagem - Ignora 2 pontos de defesa durante o ataque.", "atributo": "Força"}
        ]
    },
    "Mitologia Egípcia": {
        "Deuses": [
            {"nome": "Ra, Deus do Sol", "poder": 8, "efeito": "Chama Solar - Inflige 3 de dano extra a inimigos com atributos de trevas.", "atributo": "Fogo"},
            {"nome": "Ísis, Deusa da Magia e Fertilidade", "poder": 6, "efeito": "Encanto Místico - Cura 3 pontos de vida e remove um efeito negativo de um aliado.", "atributo": "Cura"},
            {"nome": "Osíris, Senhor do Além", "poder": 7, "efeito": "Ressurreição - Ao ser destruído, retorna com metade do poder no próximo turno.", "atributo": "Cura"},
            {"nome": "Set, Deus do Caos", "poder": 7, "efeito": "Tempestade de Caos - Embaralha a mão inimiga, causando 2 de dano para cada carta embaralhada.", "atributo": "Ataque"},
            {"nome": "Anúbis, Guardião dos Mortos", "poder": 6, "efeito": "Proteção do Além - Concede +3 de defesa a uma criatura aliada durante um ataque.", "atributo": "Defesa"},
            {"nome": "Hathor, Deusa do Amor e Alegria", "poder": 6, "efeito": "Encanto de Hathor - Restaura 3 pontos de vida a todos os aliados.", "atributo": "Cura"},
            {"nome": "Thoth, Deus da Sabedoria", "poder": 6, "efeito": "Escritura Divina - Permite descartar uma carta para comprar outra do deck.", "atributo": "Sabedoria"}
        ],
        "Artefatos": [
            {"nome": "Ankh do Destino", "custo_fe": 3, "efeito": "Reverte um efeito negativo e recupera 2 pontos de vida de um aliado.", "atributo": "Cura"},
            {"nome": "Cajado de Osíris", "custo_fe": 3, "efeito": "Concede +2 de poder e +1 de defesa a um deus aliado por um turno.", "atributo": "Ataque"},
            {"nome": "Máscara de Anúbis", "custo_fe": 2, "efeito": "Permite visualizar a mão do oponente por um turno e anular um efeito.", "atributo": "Magia"}
        ],
        "Eventos": [
            {"nome": "Benção do Nilo", "custo_fe": 3, "efeito": "Restaura 4 pontos de vida a todos os aliados e aumenta sua defesa em 1 neste turno.", "atributo": "Cura"},
            {"nome": "Maldição do Deserto", "custo_fe": 4, "efeito": "Causa 2 de dano a cada turno em todos os inimigos por 2 turnos.", "atributo": "Natureza"},
            {"nome": "Ascensão do Sol", "custo_fe": 3, "efeito": "Aumenta o poder de todos os deuses aliados em 2 pontos neste turno.", "atributo": "Fogo"},
            {"nome": "Sombra do Duat", "custo_fe": 3, "efeito": "Neutraliza os efeitos especiais dos deuses inimigos por um turno.", "atributo": "Magia"},
            {"nome": "Festival de Ísis", "custo_fe": 2, "efeito": "Permite que todos os aliados comprem uma carta extra no próximo turno.", "atributo": "Defesa"}
        ],
        "Criaturas": [
            {"nome": "Sphinx Sábia", "poder": 5, "efeito": "Enigma Antigo - Força o oponente a descartar uma carta ao atacar.", "atributo": "Sabedoria"},
            {"nome": "Escorpião Gigante", "poder": 4, "efeito": "Picada Venenosa - Causa 2 de dano extra ao atacar.", "atributo": "Ataque"},
            {"nome": "Crocodilo do Nilo", "poder": 6, "efeito": "Mordida Devastadora - Ignora 2 pontos de defesa inimiga ao atacar.", "atributo": "Força"},
            {"nome": "Benu, a Fênix Egípcia", "poder": 5, "efeito": "Renascimento Sagrado - Retorna com metade do poder se destruída.", "atributo": "Cura"},
            {"nome": "Gato Sagrado", "poder": 4, "efeito": "Agilidade Felina - Pode evitar um ataque direto uma vez por turno.", "atributo": "Agilidade"}
        ]
    },
    "Mitologia Hindu": {
        "Deuses": [
            {"nome": "Brahma, Criador do Universo", "poder": 7, "efeito": "Semeadura Cósmica - Permite comprar 1 carta extra ao ser invocado.", "atributo": "Magia"},
            {"nome": "Vishnu, Protetor do Cosmos", "poder": 8, "efeito": "Preservação Divina - Anula um ataque inimigo redirecionando o dano para outra criatura.", "atributo": "Defesa"},
            {"nome": "Shiva, O Destruidor e Transformador", "poder": 8, "efeito": "Dança da Destruição - Ao atacar, causa 3 de dano a todos os inimigos próximos.", "atributo": "Ataque"},
            {"nome": "Lakshmi, Deusa da Riqueza", "poder": 6, "efeito": "Benção da Prosperidade - Restaura 3 pontos de vida a todos os aliados.", "atributo": "Cura"},
            {"nome": "Parvati, Deusa da Fertilidade", "poder": 6, "efeito": "Cuidado Materno - Aumenta a defesa de um aliado em 3 pontos por um turno.", "atributo": "Defesa"},
            {"nome": "Ganesh, Removedor de Obstáculos", "poder": 5, "efeito": "Bênção de Ganesh - Permite ignorar custos adicionais em uma jogada.", "atributo": "Sabedoria"},
            {"nome": "Saraswati, Deusa do Conhecimento", "poder": 6, "efeito": "Inspiração Divina - Permite trocar uma carta da mão por outra do deck.", "atributo": "Sabedoria"}
        ],
        "Artefatos": [
            {"nome": "Chakra de Vishnu", "custo_fe": 3, "efeito": "Concede +2 de poder a um deus aliado e reflete 2 pontos de dano.", "atributo": "Magia"},
            {"nome": "Tridente de Shiva", "custo_fe": 3, "efeito": "Aumenta o poder de Shiva em 2 pontos e reduz 2 pontos de dano recebido por um turno.", "atributo": "Ataque"},
            {"nome": "Lótus Sagrado de Lakshmi", "custo_fe": 2, "efeito": "Restaura 2 pontos de vida a um aliado e concede um bônus de defesa.", "atributo": "Cura"}
        ],
        "Eventos": [
            {"nome": "Dança Cósmica de Shiva", "custo_fe": 4, "efeito": "Todos os inimigos sofrem 2 pontos de dano devido à dança caótica.", "atributo": "Ataque"},
            {"nome": "Benção de Brahma", "custo_fe": 3, "efeito": "Permite comprar 2 cartas adicionais e recuperar 2 pontos de vida.", "atributo": "Magia"},
            {"nome": "Iluminação Divina", "custo_fe": 3, "efeito": "Concede +2 de poder e +1 de defesa a todos os deuses aliados por um turno.", "atributo": "Cura"},
            {"nome": "Tempestade de Dharma", "custo_fe": 4, "efeito": "Reduz o poder dos inimigos em 2 pontos e bloqueia ações especiais por um turno.", "atributo": "Defesa"},
            {"nome": "Festival de Diwali", "custo_fe": 3, "efeito": "Restaura 3 pontos de vida a todos os aliados e permite uma jogada extra no próximo turno.", "atributo": "Cura"}
        ],
        "Criaturas": [
            {"nome": "Garuda, a Águia Divina", "poder": 6, "efeito": "Vôo Sagrado - Pode atacar sem ser bloqueado por criaturas terrestres.", "atributo": "Agilidade"},
            {"nome": "Nandi, o Touro Sagrado", "poder": 7, "efeito": "Investida Poderosa - Ignora 2 pontos de defesa ao atacar.", "atributo": "Força"},
            {"nome": "Rakshasa Selvagem", "poder": 5, "efeito": "Fúria Demoníaca - Ao atacar, causa 2 pontos de dano extra.", "atributo": "Ataque"},
            {"nome": "Apsara Encantadora", "poder": 4, "efeito": "Dança Celestial - Confunde o inimigo, forçando-o a descartar uma carta.", "atributo": "Magia"},
            {"nome": "Makara, Guardião das Águas", "poder": 6, "efeito": "Defesa Aquática - Ao ser atacado, reduz o dano recebido em 2 pontos.", "atributo": "Água"}
        ]
    },
    "Mitologia Nórdica": {
        "Deuses": [
            {"nome": "Odin, Pai dos Deuses", "poder": 8, "efeito": "Olhar de Sabedoria - Permite ver a mão do oponente e forçar o descarte de uma carta.", "atributo": "Sabedoria"},
            {"nome": "Thor, Deus do Trovão", "poder": 8, "efeito": "Impacto Trovão - Causa 3 pontos de dano extra a todas as criaturas inimigas.", "atributo": "Força"},
            {"nome": "Loki, O Astuto Trapaceiro", "poder": 6, "efeito": "Ilusão Enganadora - Permite trocar uma carta da sua mão com uma carta do adversário.", "atributo": "Sabedoria"},
            {"nome": "Freyja, Deusa do Amor e da Beleza", "poder": 6, "efeito": "Encanto de Freyja - Restaura 3 pontos de vida a um aliado.", "atributo": "Magia"},
            {"nome": "Tyr, Deus da Coragem", "poder": 7, "efeito": "Sacrifício Heroico - Ao atacar, pode assumir dano no lugar de um aliado.", "atributo": "Força"},
            {"nome": "Baldr, Deus da Luz", "poder": 7, "efeito": "Aura de Pureza - Torna um aliado imune a efeitos de eventos por um turno.", "atributo": "Defesa"},
            {"nome": "Frigg, Deusa da Fertilidade", "poder": 6, "efeito": "Bênção Materna - Aumenta a defesa de todos os deuses aliados em 2 pontos.", "atributo": "Natureza"}
        ],
        "Artefatos": [
            {"nome": "Mjölnir, Martelo de Thor", "custo_fe": 3, "efeito": "Concede +2 de poder a Thor e causa 2 de dano extra aos inimigos.", "atributo": "Ataque"},
            {"nome": "Gungnir, Lança de Odin", "custo_fe": 3, "efeito": "Aumenta o poder de Odin em 2 pontos e ignora 1 ponto de defesa inimigo.", "atributo": "Ataque"},
            {"nome": "Anel de Loki", "custo_fe": 2, "efeito": "Permite trocar uma carta da sua mão com o deck do adversário uma vez por turno.", "atributo": "Magia"}
        ],
        "Eventos": [
            {"nome": "Rugido do Valhalla", "custo_fe": 3, "efeito": "Concede +2 de poder e +1 de defesa a todos os aliados por um turno.", "atributo": "Defesa"},
            {"nome": "Tempestade de Gelo", "custo_fe": 4, "efeito": "Causa 2 de dano a todas as criaturas inimigas e reduz sua velocidade de ataque.", "atributo": "Natureza"},
            {"nome": "Banquete dos Aesir", "custo_fe": 3, "efeito": "Restaura 4 pontos de vida a todos os deuses aliados e aumenta sua defesa em 1 ponto.", "atributo": "Defesa"},
            {"nome": "Traição de Loki", "custo_fe": 4, "efeito": "Força o oponente a descartar uma carta aleatória da mão.", "atributo": "Magia"},
            {"nome": "Profecia de Norns", "custo_fe": 3, "efeito": "Permite ver as 3 próximas cartas do deck do oponente.", "atributo": "Sabedoria"}
        ],
        "Criaturas": [
            {"nome": "Jörmungandr, a Serpente do Mundo", "poder": 8, "efeito": "Envolvimento Devastador - Ao atacar, causa 3 de dano a todas as criaturas inimigas.", "atributo": "Ataque"},
            {"nome": "Fenrir, o Lobo Devastador", "poder": 8, "efeito": "Mordida Implacável - Ignora 2 pontos de defesa inimiga durante o ataque.", "atributo": "Força"},
            {"nome": "Einherjar Guerreiro", "poder": 6, "efeito": "Espírito de Valhala - Ganha +2 de poder se outro guerreiro aliado atacar no mesmo turno.", "atributo": "Força"},
            {"nome": "Valkyrie Veloz", "poder": 5, "efeito": "Voo Celestial - Pode atacar sem ser bloqueada por criaturas terrestres.", "atributo": "Agilidade"},
            {"nome": "Troll da Montanha", "poder": 5, "efeito": "Força Bruta - Se atacar sozinho, causa dano dobrado por um turno.", "atributo": "Força"}
        ]
    },
    "Mitologia Africana": {
        "Deuses": [
            {"nome": "Olodumare, Criador Supremo", "poder": 8, "efeito": "Palavra da Criação - Compra 1 carta extra e restaura 2 pontos de vida.", "atributo": "Sabedoria"},
            {"nome": "Shango, Deus do Trovão", "poder": 8, "efeito": "Raio Furioso - Causa 3 de dano extra a inimigos com atributos de trevas.", "atributo": "Ataque"},
            {"nome": "Oya, Deusa dos Ventos", "poder": 7, "efeito": "Rajada Tempestuosa - Altera a ordem de ataque dos inimigos, causando confusão.", "atributo": "Agilidade"},
            {"nome": "Obatala, Deus da Pureza", "poder": 7, "efeito": "Luz Purificadora - Remove efeitos negativos de um aliado e aumenta sua defesa em 2 pontos.", "atributo": "Defesa"},
            {"nome": "Yemoja, Mãe das Águas", "poder": 7, "efeito": "Maré Curativa - Restaura 4 pontos de vida a todos os aliados.", "atributo": "Água"},
            {"nome": "Oshun, Deusa do Amor e Fertilidade", "poder": 6, "efeito": "Encanto Afetuoso - Aumenta o poder de um aliado em 2 e cura 2 pontos de vida.", "atributo": "Cura"},
            {"nome": "Eshu, Guardião dos Caminhos", "poder": 6, "efeito": "Travessia Astuta - Permite trocar uma carta da sua mão com uma do adversário.", "atributo": "Magia"}
        ],
        "Artefatos": [
            {"nome": "Cajado de Shango", "custo_fe": 3, "efeito": "Concede +2 de poder a um deus aliado e adiciona 2 de dano extra.", "atributo": "Ataque"},
            {"nome": "Véu de Oshun", "custo_fe": 2, "efeito": "Concede +3 de defesa a um aliado durante um ataque.", "atributo": "Magia"},
            {"nome": "Colar de Yemoja", "custo_fe": 2, "efeito": "Restaura 2 pontos de vida a um aliado e aumenta sua resistência a ataques aquáticos.", "atributo": "Água"}
        ],
        "Eventos": [
            {"nome": "Tempestade de Shango", "custo_fe": 4, "efeito": "Causa 2 de dano a todos os inimigos e reduz sua defesa em 1 por turno.", "atributo": "Ataque"},
            {"nome": "Benção de Olodumare", "custo_fe": 3, "efeito": "Restaura 4 pontos de vida a todos os deuses e criaturas aliados.", "atributo": "Magia"},
            {"nome": "Vento de Oya", "custo_fe": 3, "efeito": "Reduz a velocidade de ataque dos inimigos em 1 ponto por um turno.", "atributo": "Agilidade"},
            {"nome": "Dança dos Ancestrais", "custo_fe": 3, "efeito": "Aumenta o poder de todas as criaturas aliadas em 2 pontos neste turno.", "atributo": "Defesa"},
            {"nome": "Caminho de Eshu", "custo_fe": 3, "efeito": "Permite trocar uma carta da sua mão com a carta do topo do deck do adversário.", "atributo": "Magia"}
        ],
        "Criaturas": [
            {"nome": "Leopardo Espreitador", "poder": 6, "efeito": "Agilidade Selvagem - Pode atacar sem ser bloqueado uma vez por turno.", "atributo": "Agilidade"},
            {"nome": "Crocodilo Ancestral", "poder": 7, "efeito": "Mordida Devastadora - Ignora 2 pontos de defesa ao atacar.", "atributo": "Força"},
            {"nome": "Mamba Venenosa", "poder": 5, "efeito": "Veneno Mortal - Causa 2 de dano extra ao atacar.", "atributo": "Ataque"},
            {"nome": "Griot Encantado", "poder": 4, "efeito": "Contador de Histórias - Ao ser invocado, permite que um aliado compre uma carta extra.", "atributo": "Sabedoria"},
            {"nome": "Anansi, a Aranha Astuta", "poder": 4, "efeito": "Teia Enganadora - Prende uma carta inimiga, impedindo seu uso no próximo turno.", "atributo": "Magia"}
        ]
    },
    "Mitologia Ocidental": {
        "Deuses/Entidades": [
            {"nome": "Arcanjo Miguel, Guardião Celestial", "poder": 8, "efeito": "Lâmina da Justiça - Causa 3 de dano extra a criaturas malignas.", "atributo": "Magia"},
            {"nome": "Arcanjo Gabriel, Mensageiro Divino", "poder": 7, "efeito": "Toque Inspirador - Permite que um aliado compre uma carta adicional.", "atributo": "Magia"},
            {"nome": "Arcanjo Rafael, Curador Celestial", "poder": 6, "efeito": "Cura Angelical - Restaura 4 pontos de vida a um aliado.", "atributo": "Cura"},
            {"nome": "São Jorge, o Valoroso", "poder": 7, "efeito": "Cavaleiro de Luz - Ganha +2 de poder se enfrentar criaturas demoníacas.", "atributo": "Ataque"},
            {"nome": "Rei Arthur, Líder Lendário", "poder": 8, "efeito": "Chamado da Távola - Fortalece todos os aliados, concedendo +1 de poder a cada um por um turno.", "atributo": "Sabedoria"},
            {"nome": "Merlin, o Encantador", "poder": 7, "efeito": "Magia Profética - Permite visualizar as 3 próximas cartas do deck e reorganizá-las.", "atributo": "Magia"},
            {"nome": "Santa Bárbara, a Protetora", "poder": 6, "efeito": "Muralha de Fé - Aumenta a defesa de um aliado em 3 pontos por um turno.", "atributo": "Defesa"}
        ],
        "Artefatos": [
            {"nome": "Excalibur, a Espada Sagrada", "custo_fe": 3, "efeito": "Concede +2 de poder a um deus aliado e tem chance de anular um ataque inimigo.", "atributo": "Magia"},
            {"nome": "Escudo de Camelot", "custo_fe": 2, "efeito": "Aumenta a defesa de um aliado em 3 pontos durante um ataque.", "atributo": "Defesa"},
            {"nome": "Cálice Sagrado", "custo_fe": 2, "efeito": "Restaura 2 pontos de vida a um aliado e remove efeitos negativos.", "atributo": "Cura"}
        ],
        "Eventos": [
            {"nome": "Julgamento Celestial", "custo_fe": 4, "efeito": "Causa 3 de dano a todas as criaturas inimigas e reduz suas defesas por um turno.", "atributo": "Defesa"},
            {"nome": "Batalha dos Santos", "custo_fe": 3, "efeito": "Concede +2 de poder e +1 de defesa a todos os deuses aliados neste turno.", "atributo": "Defesa"},
            {"nome": "Profecia de Merlin", "custo_fe": 3, "efeito": "Permite ver as 3 próximas cartas do deck e escolher uma para manter.", "atributo": "Sabedoria"},
            {"nome": "Milagre Divino", "custo_fe": 3, "efeito": "Restaura 5 pontos de vida a um aliado e remove efeitos negativos.", "atributo": "Cura"},
            {"nome": "Queda dos Hereges", "custo_fe": 4, "efeito": "Reduz o poder de todas as criaturas inimigas em 2 pontos por um turno.", "atributo": "Defesa"}
        ],
        "Criaturas": [
            {"nome": "Dragão Lendário", "poder": 8, "efeito": "Fogo Celestial - Ao atacar, causa 3 de dano extra e intimida inimigos.", "atributo": "Fogo"},
            {"nome": "Cavaleiro da Távola Redonda", "poder": 7, "efeito": "Valor Inabalável - Ganha +2 de poder se outro aliado atacar simultaneamente.", "atributo": "Força"},
            {"nome": "Fada Encantada", "poder": 4, "efeito": "Brilho Mágico - Pode confundir um inimigo, fazendo-o descartar uma carta.", "atributo": "Magia"},
            {"nome": "Lobo Fantasma", "poder": 5, "efeito": "Sombra Veloz - Pode atacar sem ser bloqueado uma vez por turno.", "atributo": "Agilidade"},
            {"nome": "Espírito Errante", "poder": 4, "efeito": "Presença Inquieta - Ao ser invocado, permite que um aliado recupere 2 pontos de vida.", "atributo": "Cura"}
        ]
    },
    "Mitologia Indígena Brasileira": {
        "Entidades": [
            {"nome": "Tupã, Deus do Trovão e da Criação", "poder": 8, "efeito": "Trovão Divino - Causa 3 pontos de dano extra a inimigos com atributo Sombra.", "atributo": "Ataque"},
            {"nome": "Guaraci, Deus do Sol", "poder": 8, "efeito": "Luz Radiante - Concede +2 de poder a todas as entidades aliadas por um turno.", "atributo": "Magia"},
            {"nome": "Jaci, Deusa da Lua", "poder": 7, "efeito": "Reflexo Místico - Restaura 3 pontos de vida a um aliado ou permite comprar 1 carta extra.", "atributo": "Magia"},
            {"nome": "Iara, Senhora das Águas", "poder": 7, "efeito": "Canto Hipnótico - Paralisa um inimigo, impedindo-o de atacar no próximo turno.", "atributo": "Água"},
            {"nome": "Caipora, Guardiã das Florestas", "poder": 7, "efeito": "Proteção Selvagem - Concede +2 de defesa a criaturas com atributo Natureza por um turno.", "atributo": "Natureza"},
            {"nome": "Anhangá, Espírito dos Animais", "poder": 7, "efeito": "Chamado da Selva - Se houver criaturas com atributo Natureza em campo, dá +2 de poder a uma entidade aliada.", "atributo": "Magia"},
            {"nome": "Iauaretê, Encantadora da Floresta", "poder": 6, "efeito": "Olhar Hipnótico - Força o oponente a descartar uma carta aleatória.", "atributo": "Magia"}
        ],
        "Artefatos": [
            {"nome": "Flauta dos Ventos", "custo_fe": 3, "efeito": "Melodia Ancestral - Concede +2 de poder a uma criatura aliada com atributo Agilidade neste turno.", "atributo": "Agilidade"},
            {"nome": "Tambor do Pajé", "custo_fe": 2, "efeito": "Ritual da Terra - Restaura 3 pontos de vida a todos os aliados.", "atributo": "Cura"},
            {"nome": "Chocalho Cerimonial", "custo_fe": 2, "efeito": "Ritual Harmônico - Permite visualizar a próxima carta do deck do adversário.", "atributo": "Sabedoria"}
        ],
        "Eventos": [
            {"nome": "Chuva de Bênçãos", "custo_fe": 3, "efeito": "Bênção da Terra - Restaura 4 pontos de vida a todos os aliados.", "atributo": "Cura"},
            {"nome": "Festa do Solstício", "custo_fe": 3, "efeito": "Ritual do Sol - Todas as entidades aliadas ganham +1 de poder e +1 de defesa neste turno.", "atributo": "Defesa"},
            {"nome": "Céu Incandescente", "custo_fe": 4, "efeito": "Fulgor Divino - Causa 2 pontos de dano em todas as cartas inimigas e, em seguida, concede +2 de poder aos aliados por um turno.", "atributo": "Magia"},
            {"nome": "Dança dos Espíritos", "custo_fe": 3, "efeito": "Ritual Ancestral - Para cada criatura aliada em campo, o oponente descarta 1 carta.", "atributo": "Sabedoria"},
            {"nome": "Vento das Almas", "custo_fe": 4, "efeito": "Sopro Ancestral - Reduz o poder dos inimigos em 2 pontos e aumenta a defesa dos aliados em 1 por um turno.", "atributo": "Agilidade"}
        ],
        "Criaturas": [
            {"nome": "Boto Encantado", "poder": 6, "efeito": "Encanto Fluvial - Ao atacar, tem 50% de chance de paralisar o inimigo por um turno.", "atributo": "Água"},
            {"nome": "Mapinguari, o Gigante da Selva", "poder": 8, "efeito": "Rugido da Selva - Ao atacar, causa 3 pontos de dano extra a todas as criaturas inimigas.", "atributo": "Força"},
            {"nome": "Caipora Menor", "poder": 5, "efeito": "Passos Silenciosos - Pode evitar um ataque inimigo uma vez por turno.", "atributo": "Natureza"},
            {"nome": "Jurupari, Espírito da Noite", "poder": 6, "efeito": "Sombra Noturna - Consegue desviar 2 pontos de dano ao ser atacado.", "atributo": "Magia"},
            {"nome": "Boiúna, a Serpente Gigante", "poder": 7, "efeito": "Enrolar Fatal - Ao atacar, envolve um inimigo, fazendo-o perder sua próxima ação.", "atributo": "Força"}
        ]
    }
}
