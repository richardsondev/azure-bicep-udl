# Azure Bicep User Defined Language for Notepad++

This repository provides a User Defined Language (UDL) definition for Notepad++ to enable syntax highlighting for Azure Bicep files (.bicep).

## Bicep Language

Bicep is a Domain Specific Language (DSL) for deploying and managing Azure resources. It provides declarative syntax and simplifies the authoring experience compared to raw ARM templates.

More information is available here: [What is Bicep?](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview?tabs=bicep)

## Background

While VS Code with the [official Bicep extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-bicep) offers the best Bicep development experience, this UDL allows you to have basic syntax highlighting in Notepad++ if you prefer a lightweight editor.

## Installation and Usage

1.  **Download the UDL file for your theme:** You can either clone this repository or directly save the XML file directly.
    * Light theme: [`Bicep-UDL.xml`](https://raw.githubusercontent.com/richardsondev/azure-bicep-udl/main/src/Bicep-UDL.xml)
    * Dark theme: [`Bicep-UDL_dark.xml`](https://raw.githubusercontent.com/richardsondev/azure-bicep-udl/main/src/Bicep-UDL_dark.xml) (thanks to [@IAmCorbin](https://github.com/IAmCorbin))
1.  **Open Notepad++:** Launch the application.
1.  **Open User Defined Language Dialog:** Go to *Language* \> *Define your language...*.
1.  **Import the UDL:** Click the *Import...* button in the "User Defined Language" dialog.
1.  **Select the XML file:** Choose the downloaded XML file.
1.  **Close the Dialog:** Close the "User Defined Language" dialog.
1.  **Open a Bicep file:** Open a `.bicep` file. The syntax highlighting should now be applied.

## Screenshots

| Light Theme | Dark Theme |
|-------------|------------|
| [<img src="./images/example.png" alt="Example Bicep with Syntax Highlighting in Notepad++ with Light theme" width="400" />](https://raw.githubusercontent.com/richardsondev/azure-bicep-udl/main/images/example.png) | [<img src="./images/example_dark.png" alt="Example Bicep with Syntax Highlighting in Notepad++ with Dark theme" width="400" />](https://raw.githubusercontent.com/richardsondev/azure-bicep-udl/main/images/example_dark.png) |
| [Bicep-UDL.xml](https://raw.githubusercontent.com/richardsondev/azure-bicep-udl/main/src/Bicep-UDL.xml) | [Bicep-UDL_dark.xml](https://raw.githubusercontent.com/richardsondev/azure-bicep-udl/main/src/Bicep-UDL_dark.xml) |

## Features

This UDL provides highlighting for:

*   **Keywords:** param, var, output, in, targetScope, resource, module, output, existing, import, as, type, with, using, extends, func, assert, extension
*   **Literals:** true, false, null, any
*   **Logical Operators:** and, or, not
*   **Built-in Functions:** for, if, concat, format, replace, split, uniqueString, resourceId, reference, json, int, bool, string, array, object, union, intersection, length, substring, range, toLower, base64
*   **Directives:** # prefixed directives such as `#disable-next-line`, `adminusername-should-not-be-literal`, `artifacts-parameters`, `decompiler-cleanup`, `explicit-values-for-loc-params`, and many more
*   **Additional Keywords:** resourceGroup, subscription, tenant, deployment, managementGroup, environment
*   **Operators:** `=`, `+`, `-`, `*`, `/`, `%`, `&`, `|`, `^`, `!`, `~`, `<`, `>`, `<=`, `>=`, `==`, `!=`, `??`, `:`, `?`
*   **Numbers:** Integer and decimal numbers, supporting suffixes `f, F, d, D` and scientific notation (`e, E`)
*   **Strings:** Single and double-quoted strings with escape sequence support
*   **Comments:** Single-line (`//`) and multi-line (`/* ... */`) comments
*   **Brackets and Parentheses:** `{}`, `[]`, `()`

## Work in Progress and Limitations

**This UDL is a work in progress.** Notepad++'s UDL system has limitations compared to the more advanced textmate grammars or Language Server Protocol (LSP) used in VS Code. Therefore, this UDL has the following limitations:

*   **Complex String Interpolation:** The more complex string interpolation (`${...}`) and verbatim strings (`'''`) are not fully supported. Basic string highlighting is provided, but nested expressions within strings might not be highlighted correctly.
*   **Advanced Regex:** The original Bicep grammar uses complex regular expressions that are difficult or impossible to fully replicate in Notepad++ UDLs.
*   **No Semantic Analysis:** This UDL only provides syntax highlighting based on lexical analysis. It does not provide semantic features like code completion, validation, or go-to-definition.

## Contributing

**Contributions are welcome!** If you find any issues or have improvements, please feel free to open a pull request or submit an issue.

## License

This project is licensed under the [MIT License](LICENSE).
