import markdown
from os import path

class Translator:
  def __init__(self, translation_table, default_lang):
    self.translation_table = translation_table
    self.default_lang = default_lang

  def t(self, key, lang=None):
    if lang is None:
      lang = self.default_lang
    
    if key not in self.translation_table:
      return f"(missing key: {key})"

    translations = self.translation_table[key]
    if lang in translations:
      return translations[lang]
  
    if lang != self.default_lang and self.default_lang in translations:
      return translations[self.default_lang]

    return f"(empty key: {key})"


def parse_language_file(file):
  with open(file, encoding="utf-8") as f:
    data = f.read().strip().split("\n")

  translation_table = {}
  
  def parse_block(block, mode):
    block_string = "\n".join(block).strip()
    if mode == "md":
      result = markdown.markdown(block_string)
      #print(f"parsed:\n\n{block_string}\n\nto:\n\n{result}\n\n")
      return result
    return block_string

  prefix = ""
  current_mode = "md"
  current_section_key = None
  current_translations = {}
  current_translation = None
  current_block = []
  for line in data:
    if line.startswith("$$$"):
      prefix = f"{line[3:].strip()}/"
    elif line.startswith("$$"):
      if current_translation is not None:
        current_translations[current_translation] = parse_block(current_block, current_mode)
      if current_section_key is not None:
        translation_table[current_section_key] = current_translations
      section_key = line[2:].strip()
      current_mode = "md"
      if section_key.startswith(":"):
        current_mode, section_key = section_key[1:].split(" ", maxsplit=1)
      current_section_key = f"{prefix}{section_key}"
      current_translations = {}
      current_translation = None
      current_block = []
    elif line.startswith("$"):
      if current_translation is not None:
        current_translations[current_translation] = parse_block(current_block, current_mode)
      current_translation = line[1:].strip()
      current_block = []
    elif current_translation is not None:
      current_block.append(line)

  if current_translation is not None:
    current_translations[current_translation] = parse_block(current_block, current_mode)

  if current_section_key is not None:
    translation_table[current_section_key] = current_translations

  for key in translation_table:
    if len(translation_table[key]) != 2:
      print(f"not 2 translations for {key}")

  return translation_table

def load_language_table():
  language_file = path.join(path.dirname(__file__), "translation_file.md")
  return parse_language_file(language_file)

def load_translator(default_lang="en"):
  return Translator(load_language_table(), default_lang)

