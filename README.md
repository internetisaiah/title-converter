# title-converter tool

This `title-converter` tool takes a string and converts it into the [approved format](#formatting-rules):

`this-is-a-title-in-the-proper-format`

## Approved Format

|Formatting Rule|Example|
|------|-------|
|All lowercase letters|_Change this:_</br>This Is My TITLE</br></br>_To this:_</br>this is my title|
|Replace [unique tech words](#unique-tech-words)|_Change this:_</br>i love c++</br></br>_To this:_</br>i love cpp|
|No special characters|_Change this:_</br>this: is my title!</br></br>_To this:_</br>this is my title|
|Replace spaces with dashes|_Change this:_</br>this is my title</br></br>_To this:_</br>this-is-my-title|

## Unique Tech Words

|Original|Replacement|
|--------|-----------|
|A#|`asharp`|
|C#|`csharp`|
|C++|`cpp`|
|F#|`fsharp`|
|J#|`jsharp`|
|J++|`jpp`|
|M#|`msharp`|
|.NET|`dotnet`|
|Q#|`qsharp`|
|R++|`rpp`|
|X#|`xsharp`|
|X++|`xpp`|
|xBase++|`xbasepp`|
|Z++|`zpp`|

## Improvements

If you find a bug or have a suggestion, feel free to reach out!
