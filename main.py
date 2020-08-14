from scripts.generator import Generator

g = Generator(iin=401795, card_len=16)
generated_cards = g.gen_cards(count=5, start_seq=102461)
print(generated_cards)