"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    f = open(file_path)
    whole_file = f.read().split()

    f.close()

    return whole_file

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """ 

    chains = {}
    next_word=[]

    for i in range(len(text_string)-2):
        n_gram = (text_string[i], text_string[i+1])
        next_word = [text_string[i+2]]
        if n_gram not in chains:
            chains[n_gram] = next_word
        else: 
            chains[n_gram] = chains[n_gram] + next_word         

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    keys = list(chains.keys())
    print(keys[0])
    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
