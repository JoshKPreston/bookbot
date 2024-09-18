
def main():
  book_path = "./books/frankenstein.txt"
  text = get_book_text(book_path)

  word_count = count_words(text)
  # print(f"{word_count} words found")

  char_count = count_chars(text)
  # print(f"{char_count} chars found")
  
  print('--- Begin report of books/frankenstein.txt ---')
  print(f"{word_count} words found in the document\n")
  char_list = []
  for c in char_count:
    if c.isalpha():
      char_list.append({
        'name': c,
        'num': char_count[c]
      })

  char_list.sort(reverse=True, key=sort_on)
  for c in char_list:
    print(f"The {c['name']} character was found {c['num']} times")
  
  print('--- End report ---')




def get_book_text(path):
  with open(path) as f:
    return f.read()

def count_words(text):
  return len(text.split())

def count_chars(text):
  text = text.lower()
  dict = {}
  for char in text:
    if char in dict:
      dict[char] += 1
    else:
      dict[char] = 1
  return dict

def sort_on(dict):
  return dict['num']



main()