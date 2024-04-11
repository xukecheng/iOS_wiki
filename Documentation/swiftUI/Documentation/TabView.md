Initializer

# init(content:)

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(@ViewBuilder content: () -> Content)

Available when `SelectionValue` is `Int` and `Content` conforms to `View`.

## See Also

### Creating a tab view

`init(selection: Binding<SelectionValue>?, content: () -> Content)`

Creates an instance that selects from content associated with `Selection`
values.

Initializer

# init(selection:content:)

Creates an instance that selects from content associated with `Selection`
values.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        selection: Binding<SelectionValue>?,
        @ViewBuilder content: () -> Content
    )

## See Also

### Creating a tab view

`init(content: () -> Content)`

Available when `SelectionValue` is `Int` and `Content` conforms to `View`.

