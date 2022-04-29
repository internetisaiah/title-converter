# This program tests the main.py function
# Learn more here: https://www.github.com/analog-isaiah/title-converter

def test():
    # imports and variables
    import sys
    import main
    main_result = ""
    test_variable = ".NET C# G# ML.NET ASP.NET C++ F++ This Is A TEST !@$"
    passing_test = "dotnet-csharp-gsharp-mlnet-aspnet-cpp-fpp-this-is-a-test"
    
    # run main.title_converter() with test varialbe
    main_result = main.title_converter(test_variable)

    # test whether main.title_converter() matches the test requirments
    if main_result != passing_test:
        sys.exit(1)

test()