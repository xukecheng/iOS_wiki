Initializer

# init(after:addition:)

A value describing the addition of the given views to the end of the indicated
group.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        after group: CommandGroupPlacement,
        @ViewBuilder addition: () -> Content
    )

## See Also

### Creating a command group

`init(before: CommandGroupPlacement, addition: () -> Content)`

A value describing the addition of the given views to the beginning of the
indicated group.

`init(replacing: CommandGroupPlacement, addition: () -> Content)`

A value describing the complete replacement of the contents of the indicated
group with the given views.

Initializer

# init(before:addition:)

A value describing the addition of the given views to the beginning of the
indicated group.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        before group: CommandGroupPlacement,
        @ViewBuilder addition: () -> Content
    )

## See Also

### Creating a command group

`init(after: CommandGroupPlacement, addition: () -> Content)`

A value describing the addition of the given views to the end of the indicated
group.

`init(replacing: CommandGroupPlacement, addition: () -> Content)`

A value describing the complete replacement of the contents of the indicated
group with the given views.

Initializer

# init(replacing:addition:)

A value describing the complete replacement of the contents of the indicated
group with the given views.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        replacing group: CommandGroupPlacement,
        @ViewBuilder addition: () -> Content
    )

## See Also

### Creating a command group

`init(after: CommandGroupPlacement, addition: () -> Content)`

A value describing the addition of the given views to the end of the indicated
group.

`init(before: CommandGroupPlacement, addition: () -> Content)`

A value describing the addition of the given views to the beginning of the
indicated group.

