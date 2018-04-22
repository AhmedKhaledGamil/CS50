# Questions

## What is pneumonoultramicroscopicsilicovolcanoconiosis?

maximum length for a word 45 characters.

## According to its man page, what does `getrusage` do?

 It's an index to time before and after.

## Per that same man page, how many members are in a variable of type `struct rusage`?

14.

## Why do you think we pass `before` and `after` by reference (instead of by value) to `calculate`, even though we're not changing their contents?

Because it's prototype defined to wait for a pointer not a value.

## Explain as precisely as possible, in a paragraph or more, how `main` goes about reading words from a file. In other words, convince us that you indeed understand how that function's `for` loop works.

It iterates through a character by character in the file, if it is a alphabetical character or apostrophy , it will be stored in an array of characters
and incrementing the index by one but if the index exceeded 45 it will not recognise it as a word, also same case if it is found a digit in between characters.
If it read a space or anyother thing it will check if the index is more than 0 so it have a word and then check if it is misspelled or not.

## Why do you think we used `fgetc` to read each word's characters one at a time rather than use `fscanf` with a format string like `"%s"` to read whole words at a time? Put another way, what problems might arise by relying on `fscanf` alone?

You won't be able to distnguish between characters , digits, marks or spaces.

## Why do you think we declared the parameters for `check` and `load` as `const` (which means "constant")?

Because they will only get one value and won't change through the entire program.
