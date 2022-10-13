
from dataclasses import dataclass
from dataclasses import dataclass


@dataclass
class TestNbbo():
    stored_share = {
        'symbol': str,
        'exchange': str,
        'bid': int,
        'offer': int,
        }
    

    def put_into_dict(self, out_line):
        output = {
            'symbol': out_line[1],
            'exchange': out_line[2],
            'bid': out_line[3],
            'offer': out_line[4].strip('\n')
        }
        return output
    
    def compare_bid_offer(self, stored_share, current_share):
        if current_share['bid'] > stored_share['bid']:
            stored_share['bid'] = current_share['bid']
        if current_share['offer'] < stored_share['offer']:
            stored_share['offer'] = current_share['offer']
        return f"{stored_share['bid']} @ {stored_share['offer']}"
        
    def process_contents(self, contents, stored_share):
        if contents.startswith('Q'):
            processed_line = contents.split('|')
            current_share = self.put_into_dict(processed_line)
            symbol = current_share['symbol']
            if stored_share['symbol'] != symbol:
                print("no_calculate")
                self.update_share(current_share)
            elif stored_share['symbol'] == symbol:
                print('calculate')
                print(self.compare_bid_offer(stored_share, current_share))
                

    def update_share(self, current_share):
        self.stored_share = current_share
        return self.stored_share
        
    def read_txt_file(self, filename):
        with open('input.txt', 'r') as filename:
            contents = filename.readlines()
            for line in contents:
                self.process_contents(line, self.stored_share)
            filename.close()


            




  
nbbo = TestNbbo()
nbbo.read_txt_file("input.txt")
