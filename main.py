def main():
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(f"{len(file_contents.split())} words found in the document")
    dict = {}
    for x in file_contents:
      x = x.lower()
      dict[x] = dict.get(x,0) + 1
    
    list_char = [{x : y} for x,y in dict.items()]
    list_char.sort(reverse=True, key=lambda x: list(x.values())[0])

    for dictionary in list_char:
        for key, value in dictionary.items():
            if key.isalpha():  # Check if key is alphabetic
                print(f"The {key} charachter was found {value} times")

main()