Instance Method

# copyable(_:)

Specifies a list of items to copy in response to the system’s Copy command.

macOS 13.0+

    
    
    func copyable<T>(_ payload: @autoclosure @escaping () -> [T]) -> some View where T : Transferable
    

##  Parameters

`payload`

    

A closure that returns an array of items to copy to the Clipboard when someone
issues a Copy command. The items in the array must conform to the
`Transferable` protocol.

## Return Value

A view that adds one or more items to the Clipboard in response to a Copy
command.

## Discussion

Use this modifier to specify one or more items that the system copies to the
Clipboard when someone issues a Copy command while the modified view has
focus. People issue a Copy command by choosing Edit > Copy from the app’s
menu, or by using the Command-C keyboard shortcut. The system enables the Copy
command for your app when it detects copyable content.

For example, the following code enables people to copy all of the strings that
they select in a `List`:

The command copies each item’s representation as specified by the item’s
conformance to the `Transferable` protocol. The above example records
selection using each list item’s corresponding string, and strings conform to
the `Transferable` protocol by default. For more complex cases, you might need
to take additional steps.

For example, the following code displays colors composed from a list of `Item`
instances that contain both a color and its name, as well as an identifier.
The list manages selection using item identifiers:

This example does two things that the previous example didn’t have to:

  * It converts the list of selected item identifiers into a list of selected items for use with the copyable modifier.

  * It ensures that the copyable items conform to the `Transferable` protocol, using the item’s `name` property as the representation.

When someone copies the first item in the list, which appears in the interface
as a red rectangle, and then pastes into a text editor, they get the string
“red”.

Note

To enable people to copy using a custom action — like from a context menu item
— rather than using the system Copy command, update the Clipboard directly
using an `NSPasteboard` or a `UIPasteboard` instance.

## See Also

### Copying transferable items

`func cuttable<T>(for: T.Type, action: () -> [T]) -> some View`

Specifies an action that moves items to the Clipboard in response to the
system’s Cut command.

`func pasteDestination<T>(for: T.Type, action: ([T]) -> Void, validator: ([T])
-> [T]) -> some View`

Specifies an action that adds validated items to a view in response to the
system’s Paste command.

Instance Method

# cuttable(for:action:)

Specifies an action that moves items to the Clipboard in response to the
system’s Cut command.

macOS 13.0+

    
    
    func cuttable<T>(
        for payloadType: T.Type = T.self,
        action: @escaping () -> [T]
    ) -> some View where T : Transferable
    

##  Parameters

`payloadType`

    

The type of items to cut.

`action`

    

A closure that you implement to delete the selected items from the collection,
and return them for addition to the Clipboard. The items must conform to the
`Transferable` protocol.

## Return Value

A view that sends one or more items to the Clipboard in response to a Cut
command.

## Discussion

Use this modifier to remove one or more items from a collection of items and
then move the items to the Clipboard when someone issues a Cut command. People
issue a Cut command by choosing Edit > Cut from the app’s menu, or by using
the Command-X keyboard shortcut. The system enables the Cut command for your
app when it detects cuttable content.

For example, the following code enables people to remove bird names from a
list of birds:

When someone selects “owl” and issues a Cut command, the `action` closure
removes the selected item from the list and returns it. In response, SwiftUI
moves it to the Clipboard. If you want to copy the item without removing it,
use the `copyable(_:)` modifier instead.

Note

To enable people to cut using a custom action — like from a context menu item
— rather than using the system Cut command, update the Clipboard directly
using an `NSPasteboard` or a `UIPasteboard` instance.

## See Also

### Copying transferable items

`func copyable<T>(() -> [T]) -> some View`

Specifies a list of items to copy in response to the system’s Copy command.

`func pasteDestination<T>(for: T.Type, action: ([T]) -> Void, validator: ([T])
-> [T]) -> some View`

Specifies an action that adds validated items to a view in response to the
system’s Paste command.

Instance Method

# pasteDestination(for:action:validator:)

Specifies an action that adds validated items to a view in response to the
system’s Paste command.

macOS 13.0+

    
    
    func pasteDestination<T>(
        for payloadType: T.Type = T.self,
        action: @escaping ([T]) -> Void,
        validator: @escaping ([T]) -> [T] = { $0 }
    ) -> some View where T : Transferable
    

##  Parameters

`payloadType`

    

The type of data that the paste destination accepts. The type must conform to
the `Transferable` protocol.

`action`

    

The action to perform when someone uses the system’s Paste command to paste
one or more items of the payload type. The closure takes one parameter, which
is the array of items to paste.

`validator`

    

A closure that you implement to validate the data to paste. SwiftUI calls this
before it calls the `action` closure, and passes in an array of items to
validate. Inspect the items, and return an array that includes only those from
the input array that you consider valid. The array that you return from this
closure becomes the input to the `action` closure. If you return an empty
array, SwiftUI doesn’t call the `action` closure.

## Return Value

A view that people can paste into using the system Paste command.

## Discussion

Use this modifier to paste one or more items into a view from the Clipboard
when someone issues a Paste command. People issue a Paste command by choosing
Edit > Paste from the app’s menu, or by using the Command-V keyboard shortcut.
The system enables the Paste command for your app when the view in focus
provides a paste destination.

For example, the following code enables people to paste bird names into a
list:

The paste destination handles only pasted content with a type that matches the
`payloadType` that you specify. The list in the above example only accepts
strings.

Use the `validator` closure to restrict the pasted content to items that make
sense in the context of the view. The above example allows people to paste
only strings that match one of a known list of bird names because the list is
meant to contain only birds. You can omit the final closure if you don’t need
to perform any validation.

Note

To enable people to paste using a custom action — like from a context menu
item — rather than using the system Paste command, access the Clipboard
directly using an `NSPasteboard` or a `UIPasteboard` instance.

## See Also

### Copying transferable items

`func copyable<T>(() -> [T]) -> some View`

Specifies a list of items to copy in response to the system’s Copy command.

`func cuttable<T>(for: T.Type, action: () -> [T]) -> some View`

Specifies an action that moves items to the Clipboard in response to the
system’s Cut command.

Instance Method

# onCopyCommand(perform:)

Adds an action to perform in response to the system’s Copy command.

macOS 10.15+

    
    
    func onCopyCommand(perform payloadAction: (() -> [NSItemProvider])?) -> some View
    

##  Parameters

`payloadAction`

    

An action closure returning the `NSItemProvider` items that should be copied
to the Clipboard when the Copy command is triggered. If `action` is `nil`, the
Copy command is considered disabled.

## Return Value

A view that triggers `action` when a system Copy command occurs.

## See Also

### Copying items using item providers

`func onCutCommand(perform: (() -> [NSItemProvider])?) -> some View`

Adds an action to perform in response to the system’s Cut command.

`func onPasteCommand(of: [UTType], perform: ([NSItemProvider]) -> Void) ->
some View`

Adds an action to perform in response to the system’s Paste command.

`func onPasteCommand<Payload>(of: [UTType], validator: ([NSItemProvider]) ->
Payload?, perform: (Payload) -> Void) -> some View`

Adds an action to perform in response to the system’s Paste command with items
that you validate.

Instance Method

# onCutCommand(perform:)

Adds an action to perform in response to the system’s Cut command.

macOS 10.15+

    
    
    func onCutCommand(perform payloadAction: (() -> [NSItemProvider])?) -> some View
    

##  Parameters

`payloadAction`

    

An action closure that should delete the selected data and return
`NSItemProvider` items corresponding to that data, which should be written to
the Clipboard. If `action` is `nil`, the Cut command is considered disabled.

## Return Value

A view that triggers `action` when a system Cut command occurs.

## See Also

### Copying items using item providers

`func onCopyCommand(perform: (() -> [NSItemProvider])?) -> some View`

Adds an action to perform in response to the system’s Copy command.

`func onPasteCommand(of: [UTType], perform: ([NSItemProvider]) -> Void) ->
some View`

Adds an action to perform in response to the system’s Paste command.

`func onPasteCommand<Payload>(of: [UTType], validator: ([NSItemProvider]) ->
Payload?, perform: (Payload) -> Void) -> some View`

Adds an action to perform in response to the system’s Paste command with items
that you validate.

Instance Method

# onPasteCommand(of:perform:)

Adds an action to perform in response to the system’s Paste command.

macOS 11.0+

    
    
    func onPasteCommand(
        of supportedContentTypes: [UTType],
        perform payloadAction: @escaping ([NSItemProvider]) -> Void
    ) -> some View
    

##  Parameters

`supportedContentTypes`

    

The uniform type identifiers that describe the types of content this view can
accept through a paste action. If the Clipboard doesn’t contain any of the
supported types, the Paste command doesn’t trigger.

`payloadAction`

    

The action to perform when the Paste command triggers. The action closure’s
parameter contains items from the Clipboard with the types you specify in the
`supportedContentTypes` parameter.

## Return Value

A view that triggers `action` when a system Paste command occurs.

## Discussion

Pass an array of uniform type identifiers to the `supportedContentTypes`
parameter. Place the higher priority types closer to the beginning of the
array. The Clipboard items that the `action` closure receives have the most
preferred type out of all the types the source supports.

For example, if your app can handle plain text and rich text, but you prefer
rich text, place the rich text type first in the array. If rich text is
available when the paste action occurs, the `action` closure passes that rich
text along.

## See Also

### Copying items using item providers

`func onCopyCommand(perform: (() -> [NSItemProvider])?) -> some View`

Adds an action to perform in response to the system’s Copy command.

`func onCutCommand(perform: (() -> [NSItemProvider])?) -> some View`

Adds an action to perform in response to the system’s Cut command.

`func onPasteCommand<Payload>(of: [UTType], validator: ([NSItemProvider]) ->
Payload?, perform: (Payload) -> Void) -> some View`

Adds an action to perform in response to the system’s Paste command with items
that you validate.

Instance Method

# onPasteCommand(of:validator:perform:)

Adds an action to perform in response to the system’s Paste command with items
that you validate.

macOS 11.0+

    
    
    func onPasteCommand<Payload>(
        of supportedContentTypes: [UTType],
        validator: @escaping ([NSItemProvider]) -> Payload?,
        perform payloadAction: @escaping (Payload) -> Void
    ) -> some View
    

##  Parameters

`supportedContentTypes`

    

The uniform type identifiers that describe the types of content this view can
accept through a paste action. If the Clipboard doesn’t contain any of the
supported types, the Paste command doesn’t trigger.

`validator`

    

A handler that validates the command. This handler receives items from the
Clipboard with the types you specify in the `supportedContentTypes`. Use this
handler to decide whether the items are valid and preprocess them for the
`action` closure. If you return `nil` instead, the Paste command doesn’t
trigger.

`payloadAction`

    

The action to perform when the Paste command triggers.

## Return Value

A view that triggers `action` when the system Paste command is invoked,
validating the Paste command with `validator`.

## Discussion

Pass an array of uniform type identifiers to the `supportedContentTypes`
parameter. Place the higher priority types closer to the beginning of the
array. The Clipboard items that the `validator` closure receives have the most
preferred type out of all the types the source supports.

For example, if your app can handle plain text and rich text, but you prefer
rich text, place the rich text type first in the array. If rich text is
available when the paste action occurs, the `validator` closure passes that
rich text along.

## See Also

### Copying items using item providers

`func onCopyCommand(perform: (() -> [NSItemProvider])?) -> some View`

Adds an action to perform in response to the system’s Copy command.

`func onCutCommand(perform: (() -> [NSItemProvider])?) -> some View`

Adds an action to perform in response to the system’s Cut command.

`func onPasteCommand(of: [UTType], perform: ([NSItemProvider]) -> Void) ->
some View`

Adds an action to perform in response to the system’s Paste command.

