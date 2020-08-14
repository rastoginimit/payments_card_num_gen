import sys

class Generator:
    def __init__(self, iin, card_len):
        self.iin      = str(iin)
        self.card_len = str(card_len)
    def gen_cards(self, count=None, start_seq=0):
        '''
        Validates the IIN, Card Length and Starting Sequence Number
        Generates required number of card numbers and retrun them in a list
        '''
        cards      = list()
        iin        = self.iin
        card_len   = self.card_len
        
        if(not (iin.isnumeric() and len(iin)==6)):
            print("IIN : ", iin, "is invalid. IIN has to be a 6 digit numberic value")
            sys.exit()
        
        if(not (card_len.isnumeric() and int(card_len)>=13 and int(card_len)<=19)):
            print("Card length : ", card_len, "is invalid. The total digits in a card number can only be between 13 and 19, both inclusive")
            sys.exit()
        card_len = int(card_len)
        
        rem_digits = card_len - 1 - len(iin)
        max_seq    = 10**rem_digits - 1 

        start_seq  = str(start_seq)
        if(not (start_seq.isnumeric() and int(start_seq)<=max_seq)):
            print("Starting Sequence : ", start_seq, "is invalid. For the given IIN and card length, the start sequnce has to be less than", max_seq)
            sys.exit()
        start_seq  = int(start_seq)

        total   = max_seq if count is None else int(count)
        counter = 0
        while(counter < total and start_seq <= max_seq):
            #prefix the starting seqeunce with 0s
            new_digits = str(start_seq).zfill(rem_digits) 
            
            # card number without the last checksum digit
            tmp_card   = iin + new_digits
            
            #calculate the checksum digit
            rvrs_card  = [int(ch) for ch in tmp_card][::-1]
            digitsmod  = (sum(rvrs_card[1::2]) + sum(sum(divmod(d*2,10)) for d in rvrs_card[0::2])) % 10
            chksum     = str(10 - digitsmod if digitsmod > 0 else 0)
            
            #suffix the checksum digit to get the valid card number
            card       = tmp_card + chksum
            cards.append(card)
            start_seq += 1
            counter   += 1
        return cards