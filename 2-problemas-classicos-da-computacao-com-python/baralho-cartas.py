import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits 
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':
#alimentando uma carta com valores
    uma_carta = Card('70', 'breads')
    print(uma_carta)

# criando uma instancia do deck e verificando seu tamanho
    deck = FrenchDeck()
    tamanho_deck = len(deck)
    print(f'Quantidade de Cartas: {tamanho_deck}')

# listando  algumas das cartas do deck
    carta = deck[2]
    print(f'escolha manual da carta: {carta}')

# funcao de escolha aleatoria
    from random import choice #!errado, nao importar biblioteca no meio do codigo
    carta = choice(deck)
    print(f'a carta escolhida aleatoriamente: {carta}')

# Explorando __getitem__ com o operador[]
    novo_deck = deck[:3]
    print(novo_deck)

    novo_deck = deck[12::13]
    print(novo_deck)

# Forma especial de busca atraves do __getitem__
    for card in deck:
        print(card)
    print('final deck!')

# Busca reversa no deck
    for card in reversed(deck):
        print(card)
    print('final deck!')

# Explorando metodo __contains__ em python
    print(Card('Q', 'hearts'))
    print(Card('13', 'beast'))

# Ordenacao com um sistema de classificacao    
    print('ordem de Classificacao por prioridade')
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    
    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]
    
    for card in sorted(deck, key=spades_high):
        print(card)
