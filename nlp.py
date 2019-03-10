import stanfordnlp
config = {
    'processors': 'tokenize,mwt,pos',
    'lang': 'fr',
    'tokenize_model_path': './stanfordnlp_resources/fr_gsd_models/fr_gsd_tokenizer.pt',
    'mwt_model_path': './stanfordnlp_resources/fr_gsd_models/fr_gsd_mwt_expander.pt',
    'pos_model_path': './stanfordnlp_resources/fr_gsd_models/fr_gsd_tagger.pt',
    'pos_pretrain_path': './stanfordnlp_resources/fr_gsd_models/fr_gsd.pretrain.pt',
    'lemma_model_path': './stanfordnlp_resources/fr_gsd_models/fr_gsd_lemmatizer.pt',
    'depparse_model_path': './stanfordnlp_resources/fr_gsd_models/fr_gsd_parser.pt',
    'depparse_pretrain_path': './stanfordnlp_resources/fr_gsd_models/fr_gsd.pretrain.pt'
}
nlp = stanfordnlp.Pipeline(**config)

def get_tagged_words(text):
  doc = nlp(text)

  nested = [sent.words for sent in doc.sentences]
  flat = [item for sublist in nested for item in sublist]
  return [x for x in flat if x.upos in ['ADJ', 'ADV', 'NOUN']]
