Initializer

# init(text:)

Creates a plain text editor.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(text: Binding<String>)

##  Parameters

`text`

    

A `Binding` to the variable containing the text to edit.

## Discussion

Use a `TextEditor` instance to create a view in which users can enter and edit
long-form text.

In this example, the text editor renders gray text using the 13 point
Helvetica Neue font with 5 points of spacing between each line:

You can define the styling for the text within the view, including the text
color, font, and line spacing. You define these styles by applying standard
view modifiers to the view.

The default text editor doesn’t support rich text, such as styling of
individual elements within the editor’s view. The styles you set apply
globally to all text in the view.

