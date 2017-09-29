def calc_hamming_dist(str1, str2):
  diff = 0
  val = int(str1, 16) ^ int(str2, 16)
  while(val != 0):
    diff += 1
    val &= val-1
  return diff

def break_repeating_key_XOR(hex_text):
  keysize = 2
  key_hamming_val = []
  hex_len = len(hex_text)
  print 'hex_len: ' + str(hex_len)

  for b in xrange(2, 40):
    hamming_vals = 0
    pos = 0
    counter = 0
    while(pos + 2*keysize <= hex_len):
        key1 = hex_text[pos:pos+keysize]
        pos += keysize
        key2 = hex_text[pos:pos+keysize]
        pos += keysize
        hamming_vals += calc_hamming_dist(key1, key2)
        counter += 1
    hamming_vals = float(hamming_vals/float(counter))
    key_hamming_val.append((float(hamming_vals/float(keysize)), keysize))
    keysize += 1

  print 'hamming_val length: ' + str(len(key_hamming_val))
  key_hamming_val.sort()
  for a in xrange(2, 38):
    blocks1 = []
    blocks2 = []
    count = 0
    key = ''

    min_hamming, keysize_guess = key_hamming_val[a]
    #for x in range(keysize_guess):
        #blocks2.append('')
    while count <= hex_len:
        blocks1.append(hex_text[count:count+keysize_guess])
        count += keysize_guess
    print str(min_hamming) + ', ' + str(keysize_guess)
    zzz = 0
    for x in blocks1:
        zzz += len(x)
    #print blocks1

    for x in range(keysize_guess):
        count = 0
        in_str = ''
        while count < len(blocks1):
            try:
                in_str += (blocks1[count])[x]
            except IndexError:
                break
            count += 1
        #print in_str
        blocks2.insert(x, in_str)
    zzz = 0
    for x in blocks2:
        zzz += len(x)
    #print blocks2

    for y in blocks2:
        if (len(y) % 2) != 0:
            y = '0' + y
        (score, words, key_guess) = get_max_single_char_xor(y)
        #print ' ' + str(key_guess)
        key += chr(key_guess)

    print key + ' (' + str(len(key)) + ')'

break_repeating_key_XOR("ex6.txt")