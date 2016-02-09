import markovify
import random
import sys

if __name__ == '__main__':

    # python3 markov.py undergrads.txt
    if len(sys.argv) != 2:
        sys.exit('USAGE: python3 {} input_file.txt'.format(sys.argv[0]))

    text = None
    with open(sys.argv[1], 'r') as f:
        text = f.read()

    model = markovify.Text(text)
    tags = ['bro', 'grad bro', 'pledge bro']
    sentences = bros = None

    # Generate at least one sentence/bro combo
    while not(sentences and bros):
        try:
            sentences = [
                sentence for sentence in
                [model.make_sentence() for i in range(random.randint(3, 5))]
                if not any([tag in sentence.lower() or 'sent from' in sentence.lower() for tag in tags])
            ]
            bros = [
                sentence for sentence in
                [model.make_short_sentence(60) for i in range(random.randint(2, 3))]
                if any([sentence.lower().startswith(tag) for tag in tags])
            ]
        except:
            continue

    print('\n' + ' '.join(sentences) + '\n\n' + '\n'.join(bros) + '\n')
