Initializer

# init(supportedContentTypes:payloadAction:)

Creates a Paste button that accepts specific types of data from the
pasteboard.

iOS 16.0+  iPadOS 16.0+  macOS 11.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    @MainActor
    init(
        supportedContentTypes: [UTType],
        payloadAction: @escaping ([NSItemProvider]) -> Void
    )

##  Parameters

`supportedContentTypes`

    

The exact uniform type identifiers supported by the button. If the pasteboard
doesn’t contain any of the supported types, the button becomes disabled.

`payloadAction`

    

The handler to call when the user clicks the Paste button and the pasteboard
has items that conform to `supportedContentTypes`. This closure receives an
array of item providers that you use to inspect and load the pasteboard data.

## Discussion

Set the contents of `supportedContentTypes` in order of your app’s preference
for its supported types. The Paste button takes the most-preferred type that
the pasteboard source supports and delivers this to the `payloadAction`
closure.

## See Also

### Creating a paste button

`init<T>(payloadType: T.Type, onPaste: ([T]) -> Void)`

Creates an instance that accepts values of the specified type.

Initializer

# init(payloadType:onPaste:)

Creates an instance that accepts values of the specified type.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    @MainActor
    init<T>(
        payloadType: T.Type,
        onPaste: @escaping ([T]) -> Void
    ) where T : Transferable

##  Parameters

`type`

    

The type that you want to paste via the `PasteButton`.

`onPaste`

    

The handler to call on trigger of the button with at least one item of the
specified `Transferable` type from the pasteboard.

## See Also

### Creating a paste button

`init(supportedContentTypes: [UTType], payloadAction: ([NSItemProvider]) ->
Void)`

Creates a Paste button that accepts specific types of data from the
pasteboard.

Initializer

# init(supportedTypes:payloadAction:)

Creates a Paste button that accepts specific types of data from the
pasteboard.

macOS 10.15–14.4  Deprecated

    
    
    @MainActor
    init(
        supportedTypes: [String],
        payloadAction: @escaping ([NSItemProvider]) -> Void
    )

Deprecated

Use the `init(supportedContentTypes:payloadAction:)` initializer instead.

##  Parameters

`supportedTypes`

    

The exact uniform type identifiers supported by the button. If the pasteboard
doesn’t contain any of the supported types, the button becomes disabled.

`payloadAction`

    

The handler to call when the user clicks the Paste button, and the pasteboard
has items that conform to `supportedTypes`. This closure receives an array of
item providers that you use to inspect and load the pasteboard data.

## Discussion

Set the contents of `supportedTypes` in order of your app’s preference for its
supported types. The Paste button takes the most-preferred type that the
pasteboard source supports and delivers this to the `payloadAction` closure.

## See Also

### Deprecated initializers

`init<Payload>(supportedTypes: [String], validator: ([NSItemProvider]) ->
Payload?, payloadAction: (Payload) -> Void)`

Creates a Paste button that accepts specific types of data from the
pasteboard, performing a custom validation of the data before sending it to
your app.

Deprecated

`init<Payload>(supportedContentTypes: [UTType], validator: ([NSItemProvider])
-> Payload?, payloadAction: (Payload) -> Void)`

Creates a Paste button that accepts specific types of data from the
pasteboard, performing a custom validation of the data before sending it to
your app.

Deprecated

Initializer

# init(supportedTypes:validator:payloadAction:)

Creates a Paste button that accepts specific types of data from the
pasteboard, performing a custom validation of the data before sending it to
your app.

macOS 10.15–14.4  Deprecated

    
    
    @MainActor
    init<Payload>(
        supportedTypes: [String],
        validator: @escaping ([NSItemProvider]) -> Payload?,
        payloadAction: @escaping (Payload) -> Void
    )

Deprecated

Use the `init(supportedContentTypes:validator:payloadAction:)` initializer
instead.

##  Parameters

`supportedTypes`

    

The exact uniform type identifiers supported by the button. If the pasteboard
doesn’t contain any of the supported types, the button becomes disabled.

`validator`

    

A handler that receives those contents of the pasteboard that conform to
`payloadAction`. Load and inspect these items to determine whether to validate
the button. If you load a valid item, return it from this closure. If the
pasteboard doesn’t contain any valid items, return `nil` to invalidate the
button.

`payloadAction`

    

The handler called when the user clicks the button. This closure receives the
preprocessed result of `validator`.

## Discussion

Set the contents of `supportedTypes` in order of your app’s preference for its
supported types. The Paste button takes the most-preferred type that the
pasteboard source supports and delivers this to the `validator` closure.

## See Also

### Deprecated initializers

`init(supportedTypes: [String], payloadAction: ([NSItemProvider]) -> Void)`

Creates a Paste button that accepts specific types of data from the
pasteboard.

Deprecated

`init<Payload>(supportedContentTypes: [UTType], validator: ([NSItemProvider])
-> Payload?, payloadAction: (Payload) -> Void)`

Creates a Paste button that accepts specific types of data from the
pasteboard, performing a custom validation of the data before sending it to
your app.

Deprecated

Initializer

# init(supportedContentTypes:validator:payloadAction:)

Creates a Paste button that accepts specific types of data from the
pasteboard, performing a custom validation of the data before sending it to
your app.

macOS 11.0–14.4  Deprecated

    
    
    @MainActor
    init<Payload>(
        supportedContentTypes: [UTType],
        validator: @escaping ([NSItemProvider]) -> Payload?,
        payloadAction: @escaping (Payload) -> Void
    )

Deprecated

Use `init(payloadType:onPaste:)` instead.

##  Parameters

`supportedContentTypes`

    

The exact uniform type identifiers supported by the button. If the pasteboard
doesn’t contain any of the supported types, the button becomes disabled.

`validator`

    

A handler that receives those contents of the pasteboard that conform to
`supportedContentTypes`. Load and inspect these items to determine whether to
validate the button. If you load a valid item, return it from this closure. If
the pasteboard doesn’t contain any valid items, return `nil` to invalidate the
button.

`payloadAction`

    

The handler called when the user clicks the button. This closure receives the
preprocessed result of `validator`.

## Discussion

Set the contents of `supportedContentTypes` in order of your app’s preference
for its supported types. The Paste button takes the most-preferred type that
the pasteboard source supports and delivers this to the `validator` closure.

## See Also

### Deprecated initializers

`init(supportedTypes: [String], payloadAction: ([NSItemProvider]) -> Void)`

Creates a Paste button that accepts specific types of data from the
pasteboard.

Deprecated

`init<Payload>(supportedTypes: [String], validator: ([NSItemProvider]) ->
Payload?, payloadAction: (Payload) -> Void)`

Creates a Paste button that accepts specific types of data from the
pasteboard, performing a custom validation of the data before sending it to
your app.

Deprecated

