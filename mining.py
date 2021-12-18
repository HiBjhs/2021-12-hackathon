import hashlib, json
 
class Block:
    def __init__(self, index, timestamp, prev_hash, transaction):
        self.index = index
        self.timestamp = timestamp
        self.prev_hash = prev_hash
        self.transaction = transaction
        self.diff = 10 #難易度 diff を追加
        self.now_hash = self.calc_hash()
        self.nonce = None #採掘時に計算する対象 nonce を追加
 
    def calc_hash(self):
        joined_data = {
            'index'       : self.index,\
            'timestamp'   : self.timestamp,\
            'prev_hash'   : self.prev_hash,\
            'transaction' : self.transaction,\
            'diff'        : self.diff
        }
        json_text = json.dumps(joined_data, sort_keys=True)
        return hashlib.sha256(json_text.encode('ascii')).hexdigest()

def check(self, nonce):
    nonce_joined = self.now_hash+str(nonce)
    calced = hashlib.sha256(nonce_joined.encode('ascii')).hexdigest()
    if calced[:self.diff:].count('0') == self.diff:
        return True
    else:
        return False

def mining(self, append_transaction):
    nonce = 0
    self.transaction.append(append_transaction)
    self.now_hash = self.calc_hash() #報酬の好きな取引を一つ入れた後にハッシュ値を再計算、このハッシュ値に nonce を足して上diff桁まで0が続くものを探していきます。
    while True:
        nonce_joined = self.now_hash+str(nonce)
        calced = hashlib.sha256(nonce_joined.encode('ascii')).hexdigest()
        if calced[:self.diff:].count('0') == self.diff: #見つかった場合は処理を抜ける。
            break
        nonce += 1
    return nonce
