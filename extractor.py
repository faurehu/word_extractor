import sys

from nlp import get_tagged_words
from reader import read_file
from airtable import send_to_airtable

posDict = {
    "ADV": "Adverb",
    "ADJ": "Adjective",
    "NOUN": "Noun"
}

def main(args):

  text = read_file(args[1])
  wordList = get_tagged_words(text)

  # TODO construct visited words here by using fetch_from_airtable
  sentWords = []

  for i, word in enumerate(wordList):
      if word.text in sentWords:
          print("Skipped repeated word (%d/%d)" % (i+1, len(wordList)))
          continue

      print("Sending %s %s (%d/%d)" % (word.upos, word.text, i+1, len(wordList)))

      data = {
          "fields": {
            "Word": word.text.lower(),
            "POS": posDict[word.upos],
            "Source": args[1].split(".")[0]
          }
      }

      send_to_airtable(data)
      sentWords.append(word.text)

if __name__ == '__main__':
    main(sys.argv)
