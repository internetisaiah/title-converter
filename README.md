# title-converter tool

This `title-converter` tool takes a string of characters and converts them into the [approved format](#approved-format).

### Table of Contents
1. [Tutorial](#tutorial)
2. [Approved Format](#approved-format)
3. [Word Replacements](#word-replacements)
4. [Suggest Improvements](#suggest-improvements)

## Tutorial

This is a simple script that can be used with **Windows**, **MacOS**, and **Linux** operating systems:

1. Open a terminal window.

2. Type `python3` to see if you have python installed. If you don't, simply follow the prompts on your screen.

3. To clone the repository, type the following, then press **Enter**:

    ```
    git clone https://github.com/analog-isaiah/title-converter.git
    ```
4. In your file explorer, you'll see a file named `title-converter.py`.

5. Copy and paste the file into your home directory.

    - In Windows this could be `C:\Users\yourNameHere>`
    - In Linux this could be `/home/yourNameHere`

6. In a terminal window, navigate to your home directory, then type `ls` to see if you've successfully copied over the `title-converter.py` file.

6. To use the tool, type:

    ```
    python3 ./title-converter.py
    ```

7. Add your title and press **Enter** to convert it to the [approved format](#approved-format).

## Approved Format

|Formatting Rule|Example|
|------|-------|
|All lowercase letters|_Change this:_</br>This Is My TITLE</br></br>_To this:_</br>this is my title|
|No special characters|_Change this:_</br>this: is my title!</br></br>_To this:_</br>this is my title|
|Replace spaces with dashes|_Change this:_</br>this is my title</br></br>_To this:_</br>this-is-my-title|
|[Replace unique words](#unique-tech-words)|_Change this:_</br>i love c++</br></br>_To this:_</br>i love cpp|

## Word Replacements

|Original|Replacement|
|--------|-----------|
|A#|`asharp`|
|ASP.NET|`aspnet`|
|C#|`csharp`|
|C++|`cpp`|
|F#|`fsharp`|
|J#|`jsharp`|
|J++|`jpp`|
|M#|`msharp`|
|ML.NET|`mlnet`|
|.NET|`dotnet`|
|Q#|`qsharp`|
|R++|`rpp`|
|X#|`xsharp`|
|X++|`xpp`|
|xBase++|`xbasepp`|
|Z++|`zpp`|

## Suggest Improvements

If you find a bug, have a suggestion, or want to add a word to the [list of replacements](#word-replacements), feel free to [create an issue](https://github.com/analog-isaiah/title-converter/issues/new/choose).
