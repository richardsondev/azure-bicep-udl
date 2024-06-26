# Azure Bicep User Defined Language (UDL) for Notepad++

This repository provides a User Defined Language (UDL) definition for Notepad++ to enable syntax highlighting for Azure Bicep files (.bicep).

## What is Bicep?

Bicep is a Domain Specific Language (DSL) for deploying and managing Azure resources. It provides declarative syntax and simplifies the authoring experience compared to raw ARM templates.

## Why use this UDL?

While VS Code with the official Bicep extension offers the best Bicep development experience, this UDL allows you to have basic syntax highlighting in Notepad++ if you prefer a lightweight editor or have specific reasons for using it.

## Installation and Usage

1.  **Download the `Bicep-UDL.xml` file:** You can either clone this repository or directly download the `src/Bicep-UDL.xml` file.

2.  **Open Notepad++:** Launch the application.

3.  **Open User Defined Language Dialog:** Go to *Language* \> *Define your language...*.

4.  **Import the UDL:** Click the *Import...* button in the "User Defined Language" dialog.

5.  **Select the XML file:** Choose the downloaded `Bicep-UDL.xml` file.

6.  **Close the Dialog:** Close the "User Defined Language" dialog.

7.  **Open a Bicep file:** Open a `.bicep` file. The syntax highlighting should now be applied.

## Features

This UDL provides highlighting for:

*   **Keywords:** `metadata`, `targetScope`, `resource`, `module`, `param`, `var`, `output`, `for`, `in`, `if`, `existing`, `import`, `as`, `type`, `with`, `using`, `extends`, `func`, `assert`, `extension`, `and`, `or`, `not`
*   **Literals:** `true`, `false`, `null`
*   **Operators:** `=`, `+`, `-`, `*`, `/`, `%`, `&`, `|`, `^`, `!`, `~`, `<`, `>`, `<=`, `>=`, `==`, `!=`, `??`, `:`, `?`, `in`
*   **Numbers:** Integer and decimal numbers.
*   **Strings:** Single-quoted strings with basic escape sequence support.
*   **Comments:** Single-line (`//`) and multi-line (`/* ... */`) comments.
*   **Brackets and Parentheses:** `{}`, `[]`, `()`
*   **Directives:** `#` prefixed directives

## Work in Progress and Limitations

**This UDL is a work in progress.** Notepad++'s UDL system has limitations compared to the more advanced textmate grammars or Language Server Protocol (LSP) used in VS Code. Therefore, this UDL has the following limitations:

*   **Complex String Interpolation:** The more complex string interpolation (`${...}`) and verbatim strings (`'''`) are not fully supported. Basic string highlighting is provided, but nested expressions within strings might not be highlighted correctly.
*   **Advanced Regex:** The original Bicep grammar uses complex regular expressions that are difficult or impossible to fully replicate in Notepad++ UDLs.
*   **No Semantic Analysis:** This UDL only provides syntax highlighting based on lexical analysis. It does not provide semantic features like code completion, validation, or go-to-definition.

**Contributions are welcome!** If you find any issues or have improvements, please feel free to open a pull request or submit an issue.

## Future Improvements (Potential)

*   Improved string highlighting.
*   More complete operator support.
*   Better handling of edge cases.

## Alternatives

For the best Bicep development experience, it is highly recommended to use:

*   **VS Code with the official Bicep extension:** This provides full language support, including syntax highlighting, code completion, validation, and more.

## License

This project is licensed under the [MIT License](LICENSE).
