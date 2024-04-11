Initializer

# init(action:)

Constructs a new help link with the specified action.

macOS 14.0+  visionOS 1.0+

    
    
    init(action: @escaping () -> Void)

##  Parameters

`action`

    

the action to perform when the user clicks the button.

## Discussion

Use this initializer when you want the standard help button appearance with a
custom button action that does not open an article in an Apple Help book.

## See Also

### Creating a help link

`init(destination: URL)`

Constructs a new help link that opens the specified destination URL.

`init(anchor: NSHelpManager.AnchorName)`

Constructs a new help link with the specified anchor in the main app bundle’s
book.

`init(anchor: NSHelpManager.AnchorName, book: NSHelpManager.BookName)`

Constructs a new help link with the specified anchor and book.

Initializer

# init(destination:)

Constructs a new help link that opens the specified destination URL.

macOS 14.0+  visionOS 1.0+

    
    
    init(destination: URL)

##  Parameters

`destination`

    

The URL to open when the button is clicked.

## Discussion

Use this initializer when you want the standard help button appearance that
opens a link to a website.

You can override the default behavior when the button is clicked by setting
the `openURL` environment value with a custom `OpenURLAction`.

## See Also

### Creating a help link

`init(action: () -> Void)`

Constructs a new help link with the specified action.

`init(anchor: NSHelpManager.AnchorName)`

Constructs a new help link with the specified anchor in the main app bundle’s
book.

`init(anchor: NSHelpManager.AnchorName, book: NSHelpManager.BookName)`

Constructs a new help link with the specified anchor and book.

Initializer

# init(anchor:)

Constructs a new help link with the specified anchor in the main app bundle’s
book.

macOS 14.0+  visionOS 1.0+

    
    
    init(anchor: NSHelpManager.AnchorName)

##  Parameters

`anchor`

    

The anchor within the help book to open to.

## Discussion

The main app bundle book name is defined by the `CFBundleHelpBookName` key in
its Info.plist file.

## See Also

### Creating a help link

`init(action: () -> Void)`

Constructs a new help link with the specified action.

`init(destination: URL)`

Constructs a new help link that opens the specified destination URL.

`init(anchor: NSHelpManager.AnchorName, book: NSHelpManager.BookName)`

Constructs a new help link with the specified anchor and book.

Initializer

# init(anchor:book:)

Constructs a new help link with the specified anchor and book.

macOS 14.0+  visionOS 1.0+

    
    
    init(
        anchor: NSHelpManager.AnchorName,
        book: NSHelpManager.BookName
    )

##  Parameters

`anchor`

    

The anchor within the help book to open to.

`book`

    

The specific book name to open.

## See Also

### Creating a help link

`init(action: () -> Void)`

Constructs a new help link with the specified action.

`init(destination: URL)`

Constructs a new help link that opens the specified destination URL.

`init(anchor: NSHelpManager.AnchorName)`

Constructs a new help link with the specified anchor in the main app bundle’s
book.

