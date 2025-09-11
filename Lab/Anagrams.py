text_1 = input("Enter a text: ")
text_2 = input("Emter a text: ")

textx_1 = "".join(sorted(list(text_1.upper().replace(" ", ""))))
textx_2 = "".join(sorted(list(text_2.upper().replace(" ", ""))))
if len(textx_1) > 0 and textx_1 == textx_2:
    print("Anagrams")
else:
    print("Not anagrams")